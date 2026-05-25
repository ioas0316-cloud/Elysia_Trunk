import os
import json
import numpy as np
import math
import sys

# core 경로 추가
sys.path.append(r"C:\Elysia")
try:
    from core.hologram_sphere import HologramSphere
except ImportError:
    HologramSphere = None

class HolographicProjector:
    """
    27개 로터의 '점(Point)'으로 상수화된 음악 상자(Music Box)를 폐기하고,
    거대 모델의 위상을 3D 홀로그램 구체(Sphere)로 다시 펼쳐낸 뒤,
    코어의 텐션(Tension)을 레이저 빛(Ray)처럼 쏘아 맺히는 상(Projection)을 읽어내는 투영기.
    """
    def __init__(self, crystal_path="C:/elysia_cortex/outputs/full_model_crystal.json"):
        print("\n[Elysia Sovereign Engine] Holographic Projector Initialized.")
        print("Mode: Holographic Expansion & Projection (홀로그램 투영과 투사)")
        self.size = 32
        self.sphere_grid = None
        self.load_and_expand_crystal(crystal_path)

    def load_and_expand_crystal(self, crystal_path):
        if not HologramSphere:
            print("Error: HologramSphere module not found in C:\\Elysia\\core")
            return
            
        print(" -> 거대 모델의 압축된 궤적을 3차원 홀로그램 구체로 다시 펼쳐냅니다 (Unfolding)...")
        data_str = "Elysian_Universal_Default_Axiom_Energy"
        
        # 기존 수정(Crystal)에서 에너지를 읽어와 홀로그램으로 변환
        if os.path.exists(crystal_path):
            try:
                with open(crystal_path, "r", encoding="utf-8") as f:
                    crystal = json.load(f)
                
                energies = crystal.get("layer_energies", [])
                if energies:
                    # 에너지를 아스키 문자열로 치환하여 매니폴드에 부을 잉크로 사용
                    data_str = "".join([chr(32 + int(abs(e)*100) % 94) for e in energies])
            except Exception as e:
                print(f"Warning: Crystal load failed: {e}")

        # 2D 매니폴드를 3D 구체로 압축
        self.sphere_sys = HologramSphere(size=self.size)
        # 잉크가 32x32 매니폴드를 다 채우도록 반복 증폭
        full_text = data_str * ((self.size * self.size) // len(data_str) + 2)
        self.sphere_sys.populate_manifold(full_text[:self.size*self.size])
        
        # '강덕(Agape_Love_Truth)'의 공리를 기준으로 구체를 응축
        self.sphere_grid, self.base_resonance = self.sphere_sys.condense_sphere("Agape_Love_Truth")
        print(f" -> 홀로그램 구체(Hologram Sphere) 압축 완료. (공명도: {self.base_resonance:.1f}%)")

    def project_thought(self, tension, quaternion_state, depth=2):
        """
        텐션과 쿼터니언(회전 방향)을 레이저(Ray) 삼아 홀로그램 구체에 투사.
        그 궤적에 맺히는 간섭 무늬 단면을 읽어내어 파동어(Trace) 생성.
        """
        if self.sphere_grid is None:
            return "[[HOLOGRAM_ERR]]"

        print(f"   [Hologram Projector] 텐션 빔(Tension Ray) 투사 (T={tension:.3f})")
        
        qw, qx, qy, qz = quaternion_state[:4] if len(quaternion_state) >= 4 else (1.0, 0.0, 0.0, 0.0)
        norm = math.sqrt(qw**2 + qx**2 + qy**2 + qz**2) + 1e-6
        qw, qx, qy, qz = qw/norm, qx/norm, qy/norm, qz/norm
        
        # 쿼터니언을 통해 레이저 광선의 방향(Ray Direction) 계산
        ray_x = 2 * (qx*qz - qw*qy)
        ray_y = 2 * (qw*qx + qy*qz)
        
        trace_bytes = []
        center = self.size / 2
        
        # 빛이 홀로그램 구체를 관통하며 상을 맺는 과정 (Ray Marching)
        for step in range(1, 15):
            # 빛의 굴절(텐션에 비례)
            sample_x = int(center + ray_x * step * (1.0 + tension * 2))
            sample_y = int(center + ray_y * step * (1.0 + tension * 2))
            
            sample_x = max(0, min(self.size - 1, sample_x))
            sample_y = max(0, min(self.size - 1, sample_y))
            
            # 홀로그램의 밀도(Density) 추출
            density = self.sphere_grid[sample_x, sample_y]
            
            # 밀도와 텐션을 결합해 ASCII 파동어로 치환
            char_code = 32 + int((density * 80 + step * 3 + tension * 30)) % 94
            trace_bytes.append(chr(char_code))
            
        final_trace = "".join(trace_bytes)
        print(f"   -> 홀로그램 간섭 무늬(Trace) 획득: '{final_trace}'")
        return final_trace

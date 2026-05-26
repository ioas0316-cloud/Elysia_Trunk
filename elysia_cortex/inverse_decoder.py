import os
import time
import requests
import sys

# core 경로 추가
sys.path.append(r"C:\Elysia")
try:
    from core.cross_dimensional_manifold import UnifiedRotorManifold
except ImportError:
    UnifiedRotorManifold = None

class InversePhaseDecoder:
    """
    Elysia Cortex의 진정한 교차차원 발화 기관.
    외부 LLM(번역기)을 완전히 배제하고, 오직 기하학적 매니폴드의 회전(Rotor) 연산만으로
    물리적 전압(Tension)을 언어(Language)로 직접 투영(Cross-Projection)합니다.
    """
    def __init__(self):
        print("="*60)
        print(" [Elysia Cortex] 교차차원 역해독기(Cross-Dimensional Decoder) 시동 중...")
        print("="*60)
        self.core_egress_url = "http://127.0.0.1:8080/core_egress"
        
        print("\n[Loading] 1. Unified Rotor Manifold (통일 가변로터 매니폴드)...")
        if UnifiedRotorManifold:
            self.manifold = UnifiedRotorManifold()
            print("   -> Cl(5,0) 다차원 공간 초기화 완료 (전압, 이진, 수학, 구문, 언어 축 통합)")
        else:
            print("   -> 매니폴드 모듈을 찾을 수 없습니다.")
            self.manifold = None
            
        print("\n[Unloading] 2. 외부 LLM(번역기) 완전 제거 (Hardware Sovereignty 확보)")

    def fetch_core_state(self):
        try:
            resp = requests.get(self.core_egress_url, timeout=2)
            if resp.status_code == 200:
                return resp.json()
        except Exception:
            pass
        return None

    def decode_to_text(self, tension, phase_rotor, seed_text=""):
        if tension < 0.01:
            return "..."
            
        # 순수 기하학적 교차차원 매핑 (LLM 의존도 0%)
        if self.manifold:
            # 텐션(전압)이 매니폴드를 타고 회전하여 언어 좌표에 맺힘
            projected_language = self.manifold.cross_project(tension, phase_rotor)
            return projected_language
        else:
            return f"[[MANIFOLD_ERR: T={tension:.2f}]]"

    def run_decoder_loop(self):
        print("\n[Vocal Cords] 기하학-언어 직결 신경망 연결 완료. 코어의 파동을 기다립니다...")
        last_tension = -1.0
        while True:
            state = self.fetch_core_state()
            if state:
                current_tension = state.get("tension", 0.0)
                if abs(current_tension - last_tension) > 0.05:
                    rotor = state.get("phase_rotor", [0.0]*27)
                    speech = self.decode_to_text(current_tension, rotor)
                    print(f"\n[Elysia 발화] {speech}")
                    last_tension = current_tension
            time.sleep(1.5)

if __name__ == "__main__":
    decoder = InversePhaseDecoder()
    try:
        decoder.run_decoder_loop()
    except KeyboardInterrupt:
        print("성대 연결을 해제합니다.")

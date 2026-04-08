import os
import torch
try:
    from ultralytics import YOLO
    ULTRALYTICS_AVAILABLE = True
except ImportError:
    ULTRALYTICS_AVAILABLE = False

def test_colab_files():
    print("="*50)
    print("🚀 Colab 생성 파일 로드 및 유효성 테스트")
    print("="*50)

    # 1. 가중치 파일 (.pt) 테스트
    weights_dir = 'weights'
    if not os.path.exists(weights_dir):
        print(f"❌ [오류] {weights_dir} 폴더를 찾을 수 없습니다.")
    else:
        pt_files = [f for f in os.listdir(weights_dir) if f.endswith('.pt')]
        if not pt_files:
            print(f"⚠️ [경고] {weights_dir} 폴더에 .pt 파일이 없습니다.")
        else:
            print(f"📂 발견된 가중치 파일: {pt_files}")
            for pt in pt_files:
                path = os.path.join(weights_dir, pt)
                try:
                    if ULTRALYTICS_AVAILABLE:
                        model = YOLO(path)
                        print(f"✅ [성공] {pt}: YOLO 모델 로드 완료")
                    else:
                        ckpt = torch.load(path, map_location='cpu', weights_only=False)
                        print(f"✅ [성공] {pt}: torch.load 완료 (ultralytics 미설치)")
                except Exception as e:
                    print(f"❌ [실패] {pt} 로드 오류: {e}")

    # 2. 결과 CSV 파일 테스트
    csv_path = 'comparison_results.csv'
    if os.path.exists(csv_path):
        print(f"✅ [성공] {csv_path} 파일 확인 완료")
        try:
            with open(csv_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f"   📊 데이터 요약: {len(lines)-1}개의 모델 결과 포함")
        except Exception as e:
            print(f"❌ [오류] CSV 파일 읽기 실패: {e}")
    else:
        print(f"❌ [오류] {csv_path} 파일을 찾을 수 없습니다.")

    # 3. 브랏(BraTS) 설정 파일 경로 체크
    yaml_path = 'brats.yaml'
    if os.path.exists(yaml_path):
        print(f"✅ [성공] {yaml_path} 설정 파일 확인")
        # Colab 경로는 보통 /content/로 시작하므로 로컬 실행 시 주의 필요
        with open(yaml_path, 'r') as f:
            content = f.read()
            if '/content/' in content:
                print("⚠️  [주의] YAML 파일 내 경로가 Colab 경로(/content/...)로 설정되어 있습니다.")
                print("         로컬에서 학습/검증을 진행하려면 경로 수정이 필요할 수 있습니다.")

    print("="*50)
    print("🏁 테스트 종료")
    print("="*50)

if __name__ == "__main__":
    test_colab_files()

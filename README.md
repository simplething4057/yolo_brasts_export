# 🧠 뇌 MRI 종양 탐지 기반 학습 보조 서비스 
> **BraTS 2021 데이터를 활용한 의료 인공지능 학습 및 종양 탐지 보조 시스템**

---

## 🚀 프로젝트 개요 (Overview)
본 프로젝트는 의료 교육 현장에서 부족한 실제 질환 데이터 시각화 문제를 해결하기 위해 기획되었습니다. 실제 뇌 MRI(BraTS 2021) 데이터를 학습한 YOLOv8 모델을 활용하여, 예비 의료인들이 종양의 위치를 직관적으로 탐지하고 관련 의학 지식을 학습할 수 있는 환경을 제공합니다.

- **대상**: 의과대학생, 방사선과 전공자, 의료 딥러닝 입문자
- **목적**: MRI 슬라이스 이미지 내 종양 탐지 프로세스 이해 및 의학 지식 습득

---

## ✨ 핵심 기능 (Features)

### 🔍 뇌종양 자동 탐지 (F-01, F-02)
- 사용자가 업로드한 MRI 슬라이스(PNG/JPG)에서 실시간 종양 탐지
- YOLOv8 모델을 통한 바운딩 박스 시각화 및 탐지 신뢰도(Confidence Score) 제공
- 원본 이미지와 탐지 결과 이미지의 병렬 비교

### 📚 의료 지식 학습 (F-03, F-05)
- **종양 정보**: 뇌종양의 정의, 종류(Glioma, Meningioma 등) 설명 제공
- **MRI 모달리티**: BraTS 데이터셋의 주요 모달리티(T1, T1ce, T2, FLAIR) 특성 정보 제공
- **모델 성능 정보**: 학습 데이터셋(30명/100명) 및 에포크별 성능 지표 비교

### 💾 탐지 이력 관리 (F-04)
- Supabase(PostgreSQL) 연동을 통한 탐지 이력(이미지명, 신뢰도 등) 데이터베이스 저장

---

## 🛠 기술 스택 (Tech Stack)

- **Frontend**: `Streamlit`
- **AI Model**: `YOLOv8s` (Ultralytics)
- **Database**: `Supabase` (PostgreSQL)
- **Deployment**: `Streamlit Cloud`
- **Language**: `Python 3.10+`

---

## 📂 프로젝트 구조 (Project Structure)
```text
yolo_brats_export/
├── app.py                # 메인 페이지 (서비스 소개 및 탐지 대시보드)
├── pages/
│   ├── 1. 탐지.py         # [Page] 종양 탐지 및 이력 저장
│   └── 2. 학습자료.py     # [Page] 의학 지식 및 모델 성능 비교
├── utils/
│   ├── database.py       # Supabase 연동 로직
│   └── detector.py       # YOLOv8 추론 래퍼
├── weights/              # 학습된 모델 가중치 (.pt)
├── brats.yaml            # 모델 설정 파일
├── requirements.txt      # 배포용 의존성 라이브러리 목록
└── README.md             # 프로젝트 문서화
```

---

## 📊 모델 성능 요약 (Model Performance)

| 데이터 규모 | Epoch | mAP@0.5 | Precision | Recall | 비고 |
| :--- | :---: | :---: | :---: | :---: | :--- |
| 30명 | 50 | **0.911** | 0.943 | 0.836 | 최적 탐지 모델 |
| 30명 | 100 | 0.884 | 0.946 | 0.821 | - |
| 100명 | 100 | 0.889 | 0.911 | **0.852** | 의료 관점 권장 |

---

## ⚙️ 시작하기 (How to Run)

### 1단계: 저장소 복제 (Clone Repository)
```bash
git clone https://github.com/사용자이름/저장소명.git
cd yolo_brats_export
```

### 2단계: 가상환경 설정 및 의존성 설치
```bash
python -m venv venv
source venv/Scripts/activate  # Windows
pip install -r requirements.txt
```

### 3단계: 환경 변수 설정
`.streamlit/secrets.toml` 파일을 생성하여 Supabase 접속 정보를 입력합니다.
```toml
[supabase]
url = "YOUR_SUPABASE_URL"
key = "YOUR_SUPABASE_KEY"
```

### 4단계: 실행
```bash
streamlit run app.py
```

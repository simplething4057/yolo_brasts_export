# 🏥 Brain MRI 종양 탐지 & 의학 교육 플랫폼

본 프로젝트는 BraTS 2021 데이터셋과 YOLOv8 모델을 활용하여, 인공지능 기반의 뇌종양(Glioma) 탐지와 의료진/학습자를 위한 실전 판독 트레이닝 환경을 제공하는 Streamlit 애플리케이션입니다.

---

## 📸 주요 구동 화면 (Demonstration)

### 1. AI 종합 분석 (Box Detection & Heatmap)
AI가 종양을 탐지한 영역(Bounding Box)과 판단의 근거가 되는 히트맵(Grad-CAM)을 동시에 제공하여 신뢰할 수 있는 판독을 지원합니다.
![AI Analysis Demo](assets/screenshots/ai_analysis_demo.png)

### 2. 정석 실전 판독 트레이닝 (4-Step)
의료 교육 표준에 따른 판독 프로세스(Raw MRI -> Diagnosis -> AI Comparison -> GT Mask/Explanation)를 제공합니다.
![Training Demo](assets/screenshots/training_demo.png)

---

## 🌐 배포 가이드 (Deployment)

### 1. Streamlit Cloud 배포
본 앱은 Streamlit Cloud를 통해 배포 가능합니다. 배포 시 **Dashboard > Settings > Secrets**에 아래 정보를 반드시 입력해야 합니다.

```toml
# Streamlit Secrets (Secrets.toml 내용 복사)
SUPABASE_URL = "YOUR_SUPABASE_URL"
SUPABASE_KEY = "YOUR_SUPABASE_ANON_KEY"
```

### 2. 환경 변수 관리 (.env)
로컬 실행 시에는 프로젝트 루트 폴더에 `.env` 파일을 생성하고 Supabase 정보를 입력하세요.
- `SUPABASE_URL`: Supabase 프로젝트 URL
- `SUPABASE_KEY`: API Key (Anon/Public)

### 3. 대용량 파일 관리 (Git LFS)
YOLO 가중치 파일(`.pt`)과 NIfTI 데이터셋은 용량이 크므로, 원활한 Push를 위해 Git LFS(Large File Storage) 사용을 권장합니다.

---

## 🚀 핵심 기능 상세

### 🔬 3D NIfTI 의료 영상 분석
- **3D Volume Visualization**: `.nii.gz` 원본 데이터를 로드하여 뇌의 모든 단면(Z-axis) 탐색.
- **Multi-Modality**: T1, T2, FLAIR, T1ce 영상을 실시간으로 대조하며 종양과 부종의 범위를 판별.

### 🧬 설명 가능한 AI (Explainable AI)
- **Grad-CAM Heatmap**: AI가 종양을 결정하는 데 결정적인 영향을 준 핵심 픽셀을 컬러맵으로 시각화하여 의료적 판단의 근거를 제시.

---

## 📂 프로젝트 구조
```text
├── app.py                # 메인 페이지 (네비게이션 및 서비스 안내)
├── pages/                # 서브 페이지 (탐지, 대시보드, 트레이닝 등)
├── weights/              # YOLOv8 학습 모델 가중치 (.pt)
├── assets/
│   ├── data/             # BraTS 2021 NIfTI 환자별 데이터 (000~100)
│   └── screenshots/      # README용 이미지
├── utils/                # AI 탐지기 및 데이터 처리 유틸리티
└── requirements.txt      # 프로젝트 의존성
```

## 📚 데이터 출처 및 인용 (Citation)
본 프로젝트는 **BraTS 2021 (RSNA-ASNR-MICCAI Brain Tumor Segmentation challenge)** 데이터를 공식적으로 활용합니다.
- Baid, U., et al. "The RSNA-ASNR-MICCAI BraTS 2021 Benchmark on Brain Tumor Segmentation." arXiv preprint arXiv:2107.02314 (2021).

---

## 🛠️ 개발 환경 구축
```bash
# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 라이브러리 설치
pip install -r requirements.txt

# 웹 앱 실행
streamlit run app.py
```

## ⚖️ License & Disclaimer
- **License**: MIT License
- **Disclaimer**: 본 애플리케이션은 의학 교육 및 AI 연구 보조용으로 개발되었습니다. 실제 임상 진단 시에는 반드시 전문의의 판단을 우선시해야 합니다.

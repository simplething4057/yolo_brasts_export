# 🏥 Brain MRI 종양 탐지 & 의학 교육 플랫폼

본 프로젝트는 BraTS 2021 데이터셋과 YOLOv8 모델을 활용하여, 인공지능 기반의 뇌종양(Glioma) 탐지와 의료진/학습자를 위한 실전 판독 트레이닝 환경을 제공하는 Streamlit 애플리케이션입니다.

---

## 📸 주요 구동 화면 (Demonstration)

### 1. AI 종합 분석 (Box Detection & Heatmap)
AI가 종양을 탐지한 영역(Bounding Box)과 판단의 근거가 되는 히트맵(Grad-CAM)을 동시에 제공합니다.
![AI Analysis Demo](assets/screenshots/ai_analysis_demo.png)

### 2. 정석 실전 판독 트레이닝 (4-Step)
학습자가 직접 진단하고 전문의의 정답(GT Mask) 및 모달리티 분석과 대조하는 전문 프로세스를 제공합니다.
![Training Demo](assets/screenshots/training_demo.png)

---

## 🚀 최신 업데이트 핵심 기능

### 1. 3D NIfTI 의료 영상 분석 지원
- **3D Volume Visualization**: `.nii.gz` 원본 데이터를 로드하여 뇌의 모든 단면(Z-axis)을 자유롭게 탐색.
- **Multi-Modality**: T1, T2, FLAIR, T1ce 영상을 실시간 동기화하여 비교 분석.

### 2. 정석 4단계 실전 판독 트레이닝
1. **MRI 분석**: 초기 육안 판독.
2. **자가 진단**: 학습자 판단 및 뇌엽(Lobe) 위치 기록.
3. **AI 종합 분석**: YOLOv8 탐지 결과 + **Grad-CAM 히트맵** (XAI).
4. **정답 및 해설**: 전문의 정답(**GT Mask Overlay**) + 4-Modality 학습 리포트.

### 3. 설명 가능한 AI (Explainable AI)
- **Grad-CAM Heatmap**: AI가 종양을 판단할 때 주목한 픽셀을 컬러맵으로 시각화하여 판단 근거 제시.

---

## 📂 프로젝트 구조
```text
├── app.py                # 메인 페이지 (서비스 안내)
├── pages/                # 서브 페이지
│   ├── 4. 실전 판독 연습.py  # 3D/XAI 통합 트레이닝 (핵심)
│   └── ...
├── assets/
│   ├── data/             # BraTS 2021 NIfTI 환자 폴더
│   └── screenshots/      # 구동 화면 이미지 저장 경로
└── requirements.txt      # 프로젝트 의존성
```

## 🛠️ 설치 및 실행 방법

1. **가상환경 설정 및 라이브러리 설치**
```bash
pip install -r requirements.txt
```

2. **애플리케이션 실행**
```bash
streamlit run app.py
```

## 📦 주요 기술 스택
- **Framework**: Streamlit
- **AI Model**: YOLOv8 (Ultralytics), PyTorch
- **Imaging**: Nibabel, OpenCV, Pillow
- **Analysis**: XAI (Grad-CAM), Multi-modality Correlation

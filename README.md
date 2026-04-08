# 🧠 뇌 MRI 종양 탐지 및 의학지식 학습 시스템 (WHO CNS5 기반)
> **BraTS 2021 데이터를 활용한 의료 인공지능 탐지 보조 및 최신 중추신경계 진단 표준(WHO CNS5) 학습 시스템**

---

## 🚀 프로젝트 개요 (Overview)
본 프로젝트는 예비 의료인 및 AI 연구자를 위한 **'의료 AI 학습 및 탐지 보조 대시보드'**입니다. 단순히 종양을 탐지하는 것을 넘어, **2021년 개정된 최신 WHO 중추신경계 종양 분류(CNS5)** 지침에 따른 전문적인 의학 지식을 인터랙티브하게 학습할 수 있는 환경을 제공합니다.

- **대상**: 의과대학생, 수련의, 의료 인공지능 입문자
- **목적**: 최신 의학 표준(WHO CNS5)에 기반한 진단 역량 강화 및 AI 탐지 프로세스 이해

---

## ✨ 핵심 기능 (Features)

### 🔍 초정밀 뇌종양 자동 탐지 (F-01, F-02)
- **YOLOv8s 엔진**: BraTS 2021 고해상도 MRI 데이터를 기반으로 학습된 실시간 탐지 모델.
- **상세 메트릭**: 종양의 바운딩 박스(Center X, Y, W, H) 및 신뢰도 점수를 데이터 테이블 형태로 즉시 제공.
- **시각화 분석**: 원본 영상과 탐지 결과의 병렬 비교를 통해 판독의 정확성 지원.

### 📚 WHO CNS5 기반 전문 학습 가이드 (F-03, 고도화항목)
- **진단 패러다임 변화**: 4판(2016) 대비 5판(2021)의 핵심 개정 사항(통합 진단, 분자학적 변이 등) 상세 수록.
- **7대 주요 종양 심층 분석**: 
    - **교종(Glioma)**: IDH-mutant/wildtype 분류 등 분자 기반 진단 체계.
    - **수막종, 뇌하수체 종양(PitNET), 전이성 뇌종양, 신경초종, 수모세포종, 림프종**의 특징 및 하위 유형.
- **MRI 판독 포인트**: Dural tail, Ring enhancement, Ice-cream cone sign 등 각 질환별 결정적 영상 지표(Radiologic point).

### 📊 학술적 근거 및 데이터 분석 (F-05)
- **최신 연구 레퍼런스**: Louis et al. (2021) 등 WHO CNS5의 근거가 된 학술 연구 자동 연동.
- **모델 성능 지표**: 데이터셋 규모(30명/100명) 및 에포크에 따른 mAP, Precision, Recall 비교 분석.

### 💾 글로벌 데이터베이스 연동 (F-04)
- **Supabase Cloud**: 탐지 이력(이미지 속성, 결과값)을 클라우드 DB에 실시간 기록하여 향후 데이터 분석의 기초 마련.

---

## 🛠 기술 스택 (Tech Stack)

- **Frontend/UI**: `Streamlit` (Interactive Dashboard)
- **Deep Learning**: `YOLOv8s` (Ultralytics), `PyTorch`
- **Database**: `Supabase` (PostgreSQL)
- **External API**: WHO CNS Classification Standards (2021)
- **Deployment**: `Streamlit Cloud`

---

## 📂 프로젝트 구조 (Project Structure)
```text
yolo_brats_export/
├── app.py                # 메인 엔트리 및 서비스 가이드
├── pages/
│   ├── 1. 탐지.py         # 실시간 MRI 탐지 및 DB 로그 기록
│   └── 2. 학습자료.py     # WHO CNS5 기반 전문 의학지식 학습 페이지
├── utils/
│   ├── database.py       # Supabase Client Wrapper
│   └── detector.py       # YOLOv8 Inference Logic (Caching 적용)
├── weights/              # 최적화된 YOLOv8 가중치 데이터
├── assets/               # 시각화 학습용 MRI 샘플 이미지
├── requirements.txt      # 프로젝트 의존성 관리
└── README.md             # 프로젝트 상세 명세
```

---

## 📊 모델 성능 성능 (Benchmark)

| 평가지표 | 30명 (50ep) | 100명 (100ep) | 특징 |
| :--- | :---: | :---: | :--- |
| **mAP@0.5** | **0.911** | 0.889 | 소규모 데이터에서 높은 정밀도 |
| **Recall** | 0.836 | **0.852** | 대규모 데이터에서 탐지 누락 방지 성능 수위 |

---

## 🎓 운영 정책 및 레퍼런스
- 본 서비스의 진단 기준은 **WHO Classification of Tumors of the Central Nervous System (5th ed., 2021)**을 준수합니다.
- 연구 근거: [Neuro-Oncology 23(8), 2021](https://academic.oup.com/neuro-oncology/article/23/8/1231/6311214)

import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="뇌종양 학습 보조 서비스",
    page_icon="🧠",
    layout="wide"
)

@st.cache_resource
def load_model():
    return YOLO('./weights/model_30p_ep50.pt')

model = load_model()

# 사이드바
st.sidebar.title("🧠 뇌종양 학습 보조")
st.sidebar.markdown("BraTS 2021 기반 YOLOv8 탐지 모델")

# 메인 페이지
st.title("뇌 MRI 종양 탐지 시스템")
st.markdown("MRI 슬라이스 이미지를 업로드하면 종양 위치를 자동으로 탐지합니다.")

col1, col2 = st.columns(2)

with col1:
    st.subheader("이미지 업로드")
    uploaded = st.file_uploader(
        "MRI 슬라이스 이미지 (PNG, JPG)",
        type=['png', 'jpg', 'jpeg']
    )

    if uploaded:
        image = Image.open(uploaded).convert('RGB')
        st.image(image, caption='업로드된 이미지', use_column_width=True)

with col2:
    st.subheader("탐지 결과")

    if uploaded:
        with st.spinner('탐지 중...'):
            results = model.predict(
                source=image,
                conf=0.3,
                save=False,
                verbose=False
            )

            result_img = results[0].plot()
            result_img = Image.fromarray(result_img[..., ::-1])
            st.image(result_img, caption='탐지 결과', use_column_width=True)

            boxes = results[0].boxes

            if len(boxes) == 0:
                st.info("종양이 탐지되지 않았습니다.")
            else:
                conf = boxes.conf[0].item()
                st.success(f"종양 탐지됨")

                # 수치 표시
                m1, m2, m3 = st.columns(3)
                m1.metric("신뢰도", f"{conf:.1%}")
                m2.metric("탐지 개수", len(boxes))
                m3.metric("모델", "YOLOv8s")

# 학습 정보 섹션
st.divider()
st.subheader("종양 학습 정보")

tab1, tab2, tab3 = st.tabs(["종양이란?", "MRI 모달리티", "탐지 지표"])

with tab1:
    st.markdown("""
    **뇌종양(Brain Tumor)**이란 뇌 조직에서 비정상적인 세포가 증식하여
    형성된 종괴를 말합니다.

    - **교종(Glioma)**: 가장 흔한 악성 뇌종양
    - **수막종(Meningioma)**: 뇌막에서 발생하는 종양
    - **전이성 뇌종양**: 다른 부위 암이 뇌로 전이된 경우
    """)

with tab2:
    st.markdown("""
    **BraTS 데이터셋의 4가지 MRI 모달리티**

    | 모달리티 | 특징 |
    |---|---|
    | T1 | 해부학적 구조 파악 |
    | T1ce | 조영증강, 종양 경계 명확 |
    | T2 | 부종 영역 확인 |
    | FLAIR | 병변 감지에 민감 |
    """)

with tab3:
    st.markdown("""
    **모델 성능 지표**

    | 지표 | 값 | 의미 |
    |---|---|---|
    | mAP@0.5 | 0.911 | 종양 탐지 정확도 |
    | Precision | 0.943 | 탐지 정밀도 |
    | Recall | 0.836 | 종양 검출률 |
    """)
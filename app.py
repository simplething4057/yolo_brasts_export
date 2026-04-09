import streamlit as st
import os

# 페이지 설정
st.set_page_config(
    page_title="서비스 안내 - 뇌 MRI AI 학습 시스템",
    page_icon="🧠",
    layout="wide"
)

# [수직형 레이아웃 개편]
# 1. 메인 타이틀
st.title("🧠 뇌 MRI 신경교종 탐지 및 학습 보조 시스템")
st.markdown("---")

# 2. 서비스 소개
st.header("1. 서비스 안내")
st.write("""
본 서비스는 **BraTS 2021** 의료 데이터셋을 학습한 인공지능(YOLOv8) 모델을 통해 
뇌 MRI 속 **신경교종(Glioma)**의 세부 영역을 탐지하고, 최신 의학 지식인 **WHO CNS5(2021)** 표준을 
학습할 수 있는 교육용 에듀테크 플랫폼입니다.
""")

# 3. 기술적 제약 사항 (핵심 인지 사항)
st.error("❗ **탐지 범위 기술적 제약 안내**\n\n"
         "현재 탑재된 AI 모델은 **신경교종(Glioma)** 특화 모델입니다. \n"
         "- **탐지 가능**: 괴사 핵심부(NCR), 부종 영역(ED), 조영증강 종양(ET)\n"
         "- **탐지 불가**: 수막종, 뇌하수체 종양, 신경초종 등 (학습 자료로는 제공되나 AI가 자동으로 탐지하지는 않음)")

# 4. 시각 자료 (가이드 이미지)
sample_path = os.path.join("assets", "modalities_sample.png")
if os.path.exists(sample_path):
    st.image(sample_path, caption="AI가 분석하는 4가지 MRI 모달리티 특징", use_container_width=True)

# 5. 상세 이용 방법
st.header("2. 페이지별 이용 방법")
with st.container():
    st.markdown("""
    - **📊 데이터 대시보드**: 축적된 탐지 데이터를 통해 모델의 성능을 검증하고 통계를 확인합니다.
    - **📝 실전 판독 연습**: 가상 증례(Case Study)를 통해 직접 MRI를 판독하고 AI 및 정답과 비교 학습합니다.
    """)

# 6. 빠른 이동 (하단 버튼)
st.write("")
st.header("3. 바로가기")
c1, c2, c3, c4 = st.columns(4)
with c1:
    if st.button("🔍 MRI 탐지 & 분석", use_container_width=True):
        st.switch_page("pages/1. MRI 탐지 & 분석.py")
with c2:
    if st.button("📚 학습자료", use_container_width=True):
        st.switch_page("pages/2. 학습자료.py")
with c3:
    if st.button("📊 데이터 데시보드", use_container_width=True):
        st.switch_page("pages/3. 데이터 데시보드.py")
with c4:
    if st.button("📝 실전 판독 연습", use_container_width=True):
        st.switch_page("pages/4. 실전 판독 연습.py")

st.divider()
st.caption("© 2026 Brain MRI AI Brain-Learning Project. Reference: WHO CNS5 (2021) & BraTS 2021 Dataset.")
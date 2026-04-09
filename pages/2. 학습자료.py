import streamlit as st
import os

# 페이지 설정
st.set_page_config(page_title="의학 교육 자료", page_icon="📚", layout="wide")

st.title("📚 뇌종양 진단 및 분류 체계 학습")
st.markdown("""
본 섹션에서는 WHO CNS5 분류 체계에 따른 주요 뇌종양의 특징과 영상학적 차이점을 학습합니다.
MRI 판독 시 종양의 위치, 조영 증강 패턴, 주변 조직 침범 정도를 파악하는 것이 중요합니다.
""")

# [학습용 영상 매핑 - URL 안정화]
tumor_samples = {
    "신경교종 (Glioma)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/41/Glioblastoma_Macro.jpg",
        "desc": "조영제 주입 시 링 형태의 조영 증강과 중심부 괴사, 그리고 광범위한 주변부 부종이 특징입니다."
    },
    "수막종 (Meningioma)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Meningioma_MRI_T1_with_contrast.jpg",
        "desc": "뇌막(Dura)에서 발생하는 가장 흔한 양성 종양으로, 경계가 뚜렷하며 균일하고 강한 조영 증강을 보입니다."
    },
    "뇌하수체 종양 (Pituitary Tumor)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Pituitary_adenoma_MRI.jpg",
        "desc": "안장(Sella) 부위에서 발생하며, 시교차(Optic chiasm)를 위로 압박하는 '눈사람' 모양의 성장이 관찰되기도 합니다."
    },
    "전이성 뇌종양 (Metastasis)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Brain_Metastasis_-_MRI_-_axial_T1_with_Contrast.png",
        "desc": "원발성 암세포가 혈류를 타고 전이된 것으로, 주로 회백질-백질 경계부에서 다발성 결절 형태로 나타납니다."
    }
}

tab1, tab2 = st.tabs(["📋 종양 분류 체계", "🖼️ 영상학적 특징 대조"])

with tab1:
    st.header("1. WHO 뇌종양 분류 (CNS5)")
    st.info("2021년 개정된 WHO CNS5 분류는 조직학적 특징뿐만 아니라 분자유전학적 특징(IDH 변이 등)을 핵심 진단 기준으로 삼습니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 주요 신경교종 (Gliomas)")
        st.write("- **Glioblastoma**, IDH-wildtype (4등급)")
        st.write("- **Astrocytoma**, IDH-mutant (2-4등급)")
        st.write("- **Oligodendroglioma**, IDH-mutant (2-3등급)")
    with col2:
        st.write("### 비신경교종 및 양성 종양")
        st.write("- **Meningioma** (수막종, 1등급)")
        st.write("- **Pituitary Adenoma** (뇌하수체 선종)")
        st.write("- **Schwannoma** (신경초종, 1등급)")

with tab2:
    st.header("2. MRI 영상 패턴 학습")
    for tumor, data in tumor_samples.items():
        with st.expander(f"🔍 {tumor} 판독 예시 모니터링"):
            c1, c2 = st.columns([1, 1])
            with c1:
                # URL 직접 로딩 시도
                st.image(data["url"], caption=f"{tumor} 대표 영상", use_container_width=True)
            with c2:
                st.write(f"**진단 핵심 소견**: {data['desc']}")
                st.markdown("""
                - **MRI 시퀀스별 특징**:
                  - **T1ce**: 혈관 장벽 파괴 정도 및 고신호 증강 확인
                  - **FLAIR**: 고형 종양 주변부의 저신호/고신호 부종 여부 판정
                """)

st.divider()
st.sidebar.markdown("### 👨‍⚕️ 판독 실력을 높이는 TIP")
st.sidebar.warning("임상 현장에서는 MRI 외에도 환자의 병력, 연령, 위치 정보를 결합하여 진단합니다. 예를 들어 다발성 결절인 경우 전이를, 뇌막에 붙은 경우 수막종을 우선 고려합니다.")

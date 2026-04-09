import streamlit as st
import os

# 페이지 설정
st.set_page_config(page_title="의학 교육 자료", page_icon="📚", layout="wide")

st.title("📚 뇌종양 진단 및 분류 체계 학습")
st.markdown("""
본 섹션에서는 WHO CNS5 분류 체계에 따른 주요 뇌종양의 특징과 영상학적 차이점을 학습합니다.
MRI 판독 시 종양의 위치, 조영 증강 패턴, 주변 조직 침범 정도를 파악하는 것이 중요합니다.
""")

# [학습용 영상 매핑 - 로컬 경로 및 대체 웹 URL]
tumor_samples = {
    "신경교종 (Glioma)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/41/Glioblastoma_Macro.jpg", # 예시
        "desc": "조영제 주입 시 링 형태의 증강과 심한 주변 부종이 특징입니다."
    },
    "수막종 (Meningioma)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/Meningioma_MRI_T1_with_contrast.jpg/600px-Meningioma_MRI_T1_with_contrast.jpg",
        "desc": "뇌막에서 발생하는 양성 종양으로, 균일한 조영 증강과 'dural tail' 징후가 보입니다."
    },
    "뇌하수체 종양 (Pituitary Tumor)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fa/Pituitary_adenoma_MRI.jpg/600px-Pituitary_adenoma_MRI.jpg",
        "desc": "터키장(Sella turcica) 부근에서 발생하며 시교차 압박으로 인한 시야 결손을 유발할 수 있습니다."
    },
    "전이성 뇌종양 (Metastasis)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Brain_Metastasis_-_MRI_-_axial_T1_with_Contrast.png/600px-Brain_Metastasis_-_MRI_-_axial_T1_with_Contrast.png",
        "desc": "원발 암(폐, 유방 등)에서 전이되어 발생하며, 주로 회백질 경계부에서 다발성으로 관찰됩니다."
    }
}

tab1, tab2 = st.tabs(["📋 종양 분류 체계", "🖼️ 영상학적 특징 대조"])

with tab1:
    st.header("1. WHO 뇌종양 분류 (CNS5)")
    st.info("2021년 개정된 WHO CNS5 분류는 조직학적 특징뿐만 아니라 분자유전학적 특징(IDH 변이 등)을 핵심 진단 기준으로 삼습니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 주요 신경교종 (Gliomas)")
        st.write("- **Glioblastoma**, IDH-wildtype")
        st.write("- **Astrocytoma**, IDH-mutant")
        st.write("- **Oligodendroglioma**, IDH-mutant, 1p/19q-codeleted")
    with col2:
        st.write("### 비신경교종 및 양성 종양")
        st.write("- **Meningioma** (수막종)")
        st.write("- **Pituitary Adenoma** (뇌하수체 선종)")
        st.write("- **Schwannoma** (신경초종)")

with tab2:
    st.header("2. MRI 영상 패턴 학습")
    for tumor, data in tumor_samples.items():
        with st.expander(f"🔍 {tumor} 판독 예시"):
            c1, c2 = st.columns([1, 1.5])
            with c1:
                st.image(data["url"], caption=f"{tumor} 대표 영상", use_container_width=True)
            with c2:
                st.write(f"**진단 포인트**: {data['desc']}")
                st.markdown("""
                - **T1ce**: 종양의 핵심부 확인
                - **T2/FLAIR**: 주변부 침윤 및 부종 확인
                """)

st.divider()
st.sidebar.markdown("### 👨‍⚕️ 판독 팁")
st.sidebar.warning("조영 증강(Enhancement)이 강할수록 대개 악성 등급이 높은 경향이 있으나, 수막종 같은 양성 종양도 강한 증강을 보일 수 있으므로 위치와 모양을 종합적으로 판단해야 합니다.")

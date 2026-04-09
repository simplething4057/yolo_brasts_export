import streamlit as st
import os

# 페이지 설정
st.set_page_config(page_title="의학 교육 자료", page_icon="📚", layout="wide")

st.title("📚 뇌종양 전문 판독 학습 가이드")
st.markdown("""
본 가이드는 뇌 MRI 판독을 시작하는 학습자를 위해 WHO CNS5 표준 분류와 주요 MRI 시퀀스별 특징을 정리한 자료입니다.
""")

# [이미지 및 데이터 정의]
modalities = {
    "T1W (T1-Weighted)": "해부학적 구조를 가장 잘 보여주며, 뇌척수액(CSF)이 검게 보입니다.",
    "T1ce (Contrast Enhanced)": "조영제를 사용하여 혈관-뇌 장벽(BBB)이 손상된 종양 부위를 밝게 보여줍니다.",
    "T2W (T2-Weighted)": "부종과 뇌척수액을 밝게 보여주며, 병변 확인에 필수적입니다.",
    "FLAIR (Fluid Attenuated Inversion Recovery)": "T2W에서 뇌척수액 신호를 억제하여, 종양 주변부의 '부종(Edema)'을 가장 명확히 식별하게 합니다."
}

tumor_samples = {
    "신경교종 (Glioma)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/4/41/Glioblastoma_Macro.jpg",
        "desc": "고등급(GBM)의 경우 중심부 괴사와 뚜렷한 링 형태의 조영 증강, 광범위한 침윤성 부종이 특징입니다."
    },
    "수막종 (Meningioma)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Meningioma_MRI_T1_with_contrast.jpg",
        "desc": "뇌막에서 발생하는 강한 조영 증강 종양으로, 뇌 조직을 밖에서 안으로 압박하는 양상을 보입니다."
    },
    "뇌하수체 종양 (Pituitary Tumor)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/fa/Pituitary_adenoma_MRI.jpg",
        "desc": "Sella 내 위치하며, 시교차를 압박하여 시야 결손을 유발합니다."
    },
    "전이성 뇌종양 (Metastasis)": {
        "url": "https://upload.wikimedia.org/wikipedia/commons/1/1b/Brain_Metastasis_-_MRI_-_axial_T1_with_Contrast.png",
        "desc": "주로 다발성으로 발생하며, 종양 크기에 비해 주변 부종(Vasogenic edema)이 매우 심한 것이 특징입니다."
    }
}

# [메인 탭 구성]
tabs = st.tabs(["📋 종양 분류 체계", "🌓 MRI 모달리티 특징", "🖼️ 종양별 영상 대조"])

# --- Tab 1: 종양 분류 ---
with tabs[0]:
    st.header("1. WHO CNS5 뇌종양 분류")
    st.info("2021년 개정된 가이드라인은 분자 생물학적 표지자(IDH, 1p/19q 등)를 진단의 필수 요소로 포함합니다.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("신경교종 계열 (Gliomas)")
        st.markdown("""
        - **Glioblastoma (Grade 4)**: 가장 악성도가 높으며 급격한 진행
        - **Astrocytoma (Grade 2-4)**: IDH 변이 여부에 따라 예후 차이
        - **Oligodendroglioma**: 1p/19q 동시 결실이 특징
        """)
    with col2:
        st.subheader("기타 주요 종양")
        st.markdown("""
        - **Meningioma**: 뇌막에서 발생하는 흔한 양성 종양
        - **Pituitary Adenoma**: 호르몬 이상 및 시야 장애 유발
        - **Schwannoma**: 청신경 등 말초 신경 초에서 발생
        """)

# --- Tab 2: 모달리티 특징 (복구) ---
with tabs[1]:
    st.header("2. MRI 시퀀스별 영상학적 특징")
    st.markdown("MRI는 각 시퀀스별로 강조하는 물리적 특성이 달라, 이를 종합하여 판독해야 합니다.")
    
    m_cols = st.columns(2)
    for i, (m_name, m_desc) in enumerate(modalities.items()):
        with m_cols[i % 2]:
            with st.container(border=True):
                st.write(f"### {m_name}")
                st.write(m_desc)
                if "T1ce" in m_name:
                    st.success("🎯 **Key**: 종양의 활동성 구역 및 BBB 파괴 확인")
                elif "FLAIR" in m_name:
                    st.warning("🎯 **Key**: 종양 주변부 침윤 및 부종(Edema) 식별")

# --- Tab 3: 종양별 영상 대조 ---
with tabs[2]:
    st.header("3. 임상 사례별 영상 대조 분석")
    st.write("각 질환별 실제 MRI 양상을 대조하며 판독 포인트를 익히십시오.")
    
    for tumor, data in tumor_samples.items():
        with st.expander(f"🔍 {tumor} 상세 판독 사례"):
            c1, c2 = st.columns([1.2, 1])
            with c1:
                st.image(data["url"], caption=f"{tumor} Case Study", use_container_width=True)
            with c2:
                st.markdown(f"**신호 강도 특성**: \n{data['desc']}")
                st.info("💡 **판독 팁**: 종양의 경계가 뚜렷한지, 주변 조직과 유착되어 있는지 확인하십시오.")

st.divider()
st.sidebar.markdown("### 🚑 학습 긴급 도움말")
st.sidebar.info("BraTS 데이터셋 트레이닝 시에는 T1ce와 FLAIR의 대조가 가장 중요합니다. T1ce에서 밝은 부분은 종양의 '핵심'이며, FLAIR에서 밝은 부분은 종양의 '영향권(부종)'입니다.")

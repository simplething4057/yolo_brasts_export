import streamlit as st
import pandas as pd
import os

# 페이지 설정
st.set_page_config(page_title="WHO CNS5 종합 진단 가이드", page_icon="🔬", layout="wide")

# 스타일링 (가독성 향상)
st.markdown("""
<style>
    .reportview-container .main .block-container { padding-top: 2rem; }
    .stAlert { margin-top: 1rem; }
    .main-header { color: #1E88E5; font-size: 2.5rem; font-weight: bold; margin-bottom: 0.5rem; }
    .sub-header { color: #43A047; font-size: 1.8rem; font-weight: bold; margin-top: 2rem; }
    .mri-point { background-color: #f0f4f7; padding: 10px; border-radius: 5px; border-left: 5px solid #1976d2; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">🧠 중추신경계 종양 분류 5판(WHO CNS5) 종합 가이드</div>', unsafe_allow_html=True)
st.markdown("본 가이드는 **WHO CNS5 (2021)**의 최신 진단 분류 체계와 MRI 판독 핵심 포인트를 상세히 다룹니다.")

# 탭 구성: 개요 / 주요 종양(7군) / 판독 가이드
tab_info, tab_glioma, tab_mening_pit, tab_extra, tab_mri = st.tabs([
    "📂 진단 패러다임 & 양상", 
    "🧬 교종(Glioma) 상세", 
    "🏢 수막종 & 뇌하수체 종양", 
    "🌿 기타 종양 (수모/신경초/림프/전이)",
    "📸 MRI 판독 핵심 포인트"
])

with tab_info:
    st.header("⚖️ 양성 vs 악성: CNS5의 새로운 시각")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("1. 양성 종양 (Benign)")
        st.write("""
        - **세포학적 특성**: 증식 속도가 느리고 주변 조직으로의 침윤이 적습니다.
        - **위험성**: 조직학적으로 양성이라도 두개골 내 압력을 높이거나 주요 뇌신경을 압박하면 임상적으로 위험할 수 있습니다.
        - **예**: CNS WHO Grade 1 (수막종 등)
        """)
    with col2:
        st.subheader("2. 악성 종양 (Malignant)")
        st.write("""
        - **세포학적 특성**: 침윤성(Infiltrative)이 강하여 정상 뇌세포 사이를 파고듭니다.
        - **위험성**: 경계가 불명확하여 완전 절제가 어렵고 재발률이 매우 높습니다.
        - **예**: CNS WHO Grade 3-4 (교모세포종 등)
        """)
    
    st.divider()
    st.subheader("📢 CNS4(2016) → CNS5(2021) 주요 개정 원칙")
    st.markdown("""
    - **통합 진단(Integrated Diagnosis)**: 조직검사(모양) 결과와 분자 유전자 검사 결과를 결합하여 최종 진단.
    - **아라비아 숫자 등급제**: I, II, III, IV 표기법을 **1, 2, 3, 4**로 전면 교체.
    - **분리 분류**: 성인형과 소아형 교종 카테고리의 명확한 분리.
    - **필수 마커**: IDH 유전자 변이 여부가 성인 교종 진단의 '첫 단계'가 됨.
    """)

with tab_glioma:
    st.header("🧬 신경교종 (Glioma): CNS5의 핵심")
    st.write("신경아교세포에서 발생하는 종양으로, CNS5에서는 **성인형 미만성 교종**을 3가지 유형으로 확정했습니다.")
    
    with st.expander("1. 성상세포종 (Astrocytoma, IDH-mutant)", expanded=True):
        st.markdown("""
        - **특징**: IDH 유전자에 변이가 있는 교종입니다.
        - **하위 등급**: Grade 2, 3, 4로 분류됩니다.
        - **핵심 유전 마커**: **ATRX 손실, TP53 변이**가 흔히 동반됩니다.
        - **특이사항**: CNS5에서는 **CDKN2A/B 결실**이 있는 경우 조직이 깨끗해 보여도 바로 **Grade 4**로 진단합니다.
        """)
        st.info("💡 **MRI 포인트**: 고등급(4)일 경우 중앙 괴사와 환상 조영 증강(Ring enhancement)이 나타납니다.")

    with st.expander("2. 핍지교종 (Oligodendroglioma, IDH-mutant & 1p/19q-codeleted)"):
        st.markdown("""
        - **특징**: IDH 변이와 더불어 **1p/19q 유전자의 공손실**이 동시에 확인되어야만 진단 가능합니다.
        - **하위 등급**: Grade 2, 3만 존재합니다.
        - **MRI 포인트**: 종양 내에 **석회화(Calcification)**가 흔히 발견되며, 피질 침범이 잦습니다.
        """)

    with st.expander("3. 교모세포종 (Glioblastoma, IDH-wildtype)"):
        st.markdown("""
        - **특징**: **IDH 변이가 없는(Wild-type)** 가장 치명적인 악성 종양입니다.
        - **등급**: 항상 **Grade 4**입니다.
        - **분자학적 하위 특성**: EGFR 증폭, TERT 프로모터 변이 등이 확인되면 진단 확정.
        - **MRI 포인트**: **괴사(Necrosis)** 중심부와 주변의 강한 **부종(Edema)**이 특징입니다.
        """)

with tab_mening_pit:
    col_m, col_p = st.columns(2)
    
    with col_m:
        st.header("🏢 수막종 (Meningioma)")
        st.write("뇌를 감싸는 수막에서 발생하는 가장 흔한 종양입니다.")
        st.markdown("""
        - **특징**: 대부분 양성(Grade 1)이나 5판에서는 유전자 특성(NF2 등)에 따라 등급을 더 세밀화했습니다.
        - **하위 유형**: 수막세포형, 섬유성형(Grade 1), 비정형성(Grade 2), 역형성(Grade 3) 등.
        - **MRI 판별 핵심**:
          - **Dural Tail Sign**: 종양 근처 뇌막이 꼬리처럼 두꺼워짐.
          - **CSF Cleft**: 뇌 조직과 종양 사이의 뇌척수액 틈새.
        """)

    with col_p:
        st.header("🧪 뇌하수체 종양 (Pituitary Neuroendocrine Tumor, PitNET)")
        st.write("CNS5에서는 '선종(Adenoma)'이라는 용어 대신 **PitNET**이라는 용어를 권고하기 시작했습니다.")
        st.markdown("""
        - **특징**: 호르몬 분비 여부에 따라 기능성/비기능성으로 나뉩니다.
        - **하위 유형**: 유즙분비호르몬 세포형, 성장호르몬 세포형 등 전사인자 기반 분류.
        - **MRI 판별 핵심**:
          - **Snowman Shape**: 안장(Sella) 부위가 좁고 위로 솟아오른 눈사람 모양.
          - **시신경 교차 압박** 확인이 가장 중요합니다.
        """)

with tab_extra:
    with st.expander("🩺 전이성 뇌종양 (Metastasis)"):
        st.markdown("""
        - **특징**: 폐암, 유방암 등이 뇌로 퍼진 경우. 뇌종양 중 발생 빈도가 가장 높습니다.
        - **MRI 판별**: 다발성(Multiple)으로 나타나는 경우가 많으며, **종양 크기에 비해 부종(Edema)이 매우 광범위**합니다.
        """)

    with st.expander("👂 신경초종 (Schwannoma)"):
        st.markdown("""
        - **특징**: 신경을 싸고 있는 슈반 세포에서 발생. 전정신경(청신경) 양 쪽에서 발생 시 신경섬유종증 2형 의심.
        - **MRI 판별**: 내이도(IAC) 입구에서 **Ice-cream cone 모양**으로 관찰됩니다.
        """)

    with st.expander("👶 수모세포종 (Medulloblastoma)"):
        st.markdown("""
        - **특징**: 소아 제4뇌실 근처에서 발생하는 악성 종양.
        - **하위 유형(분자군)**: WNT-activated, SHH-activated, Group 3, Group 4 (생존율이 극명히 다름).
        - **MRI 판별**: 소뇌 중앙 부위의 고형 종양, 수뇌증 동반 확인.
        """)

    with st.expander("🩸 림프종 (Primary CNS Lymphoma)"):
        st.markdown("""
        - **특징**: 뇌의 림프 조직에서 발생. 면역력 저하 환자에게 빈번.
        - **MRI 판별**: 뇌실 주변에 **짙은 조영 증강**을 보이며, 확산 강조 영상(DWI)에서 강한 신호를 보임.
        """)

with tab_mri:
    st.header("📸 MRI 모달리티별 판독 전략 (PRD 기반)")
    
    st.markdown('<div class="mri-point">', unsafe_allow_html=True)
    st.subheader("1. T1-CE (조영 증강)")
    st.write("- **핵심**: 혈뇌장벽(BBB)이 깨진 부위를 보여줌.")
    st.write("- **판별**: 강한 테두리 증강 → 교모세포종(Grade 4), 균일한 전체 증강 → 수막종/림프종.")
    
    st.subheader("2. T2 & FLAIR (부종 및 침윤)")
    st.write("- **핵심**: 종양 주변의 **부종(Edema)**과 **침윤 범위** 파악.")
    st.write("- **판별**: FLAIR에서 하얗게 보이는 범위가 넓을수록 주변 조직으로 많이 퍼진 악성일 확률이 높음.")
    
    st.subheader("3. T1 (구조)")
    st.write("- **핵심**: 종양 내 출혈이나 석회화(일부) 등 기본적인 해부학적 변형 확인.")
    st.markdown('</div>', unsafe_allow_html=True)

    st.divider()
    # 요약 테이블
    summary_data = {
        "종양 종류": ["교모세포종", "수막종", "전이암", "신경초종"],
        "MRI 결정적 징후": ["중앙 괴사 + 테두리 증강", "Dural Tail Sign (꼬리 징후)", "작은 종양 + 거대 부종", "내이도 Ice-cream 모양"],
        "CNS5 주요 마커": ["IDH-wildtype", "NF2 변이 연관", "원발암 이력", "NF2 유전자 관련"]
    }
    st.table(summary_data)

st.divider()
st.caption("Reference: WHO Classification of Tumors, 5th Edition (CNS5, 2021) & Diagnostic Radiology Guidelines")

import streamlit as st
import os

# 페이지 설정
st.set_page_config(page_title="의학 교육 자료", page_icon="📚", layout="wide")

st.title("뇌종양 전문 판독 학습 가이드 (상세 심화 버전)")
st.markdown("""
본 가이드는 전문가 수준의 판독 역량 강화를 위해 최신 WHO CNS5(2021) 분류 체계와 MRI 영상의 물리학적 특성을 상세히 다룹니다.
""")

# [이미지 경로 정의]
ASSETS_DIR = "assets"
MODALITIES_IMG = os.path.join(ASSETS_DIR, "modalities_sample.png")
TUMOR_IMG = os.path.join(ASSETS_DIR, "tumor_sample.png")

# [메인 탭 구성]
tabs = st.tabs(["WHO CNS5 상세 분류", "MRI 시퀀스 임상 의미", "종양별 정밀 판독 포인트"])

# --- Tab 1: 상세 분류 (세로형 가로 컬럼 제거) ---
with tabs[0]:
    st.header("1. WHO 중추신경계 종양 분류 체계 (WHO CNS5, 2021)")
    st.success("최근의 뇌종양 진단은 육안적인 세포 모양보다 '분자 유전학적 표지자'가 치료 방향과 예후를 결정하는 데 핵심적인 역할을 합니다.")
    
    st.markdown("### 성인형 미만성 신경교종 (Diffuse Gliomas)")
    with st.container(border=True):
        st.markdown("""
        **1. Glioblastoma, IDH-wildtype (Grade 4)**
        - 특징: 성인에서 가장 흔하고 파괴적인 악성 뇌종양입니다. 
        - 유전학: IDH 변이가 없는 것이 특징이며, 미만성 침윤 성향이 매우 강합니다.
        - 예후: 조기 발견 시에도 재발 위험이 높으며 적극적인 수술과 항암 방사선 치료가 복합적으로 요구됩니다.
        """)
        
    with st.container(border=True):
        st.markdown("""
        **2. Astrocytoma, IDH-mutant (Grade 2, 3, 4)**
        - 특징: IDH 유전자 변이가 있는 종양으로, GBM에 비해 상대적으로 좋은 예후를 보입니다.
        - 진단: 세포 밀도 및 핵의 비정형성에 따라 등급이 매겨집니다.
        """)

    with st.container(border=True):
        st.markdown("""
        **3. Oligodendroglioma, IDH-mutant & 1p/19q-codeleted (Grade 2, 3)**
        - 특징: '계란 프라이' 모양의 세포가 관찰되는 것이 고전적 특징입니다.
        - 키워드: 1p/19q 동시 결실이 확인되어야만 확진이 가능하며, 화학요법에 대한 반응성이 매우 우수합니다.
        """)

    st.divider()
    st.markdown("### 주요 비신경교종 그룹 (Non-Glial Tumors)")
    
    with st.container(border=True):
        st.markdown("""
        **1. Meningioma (수막종)**
        - 발생: 뇌를 싸고 있는 '지주막 세포'에서 기원하는 가장 흔한 뇌외 종양입니다.
        - 성향: 대부분의 경우 서서히 자라는 양성(Grade 1)이나, 간혹 등급 2, 3의 악성 양상을 보이기도 합니다.
        """)

    with st.container(border=True):
        st.markdown("""
        **2. Pituitary Adenoma (뇌하수체 선종)**
        - 발표: 안장(Sella) 내부에서 발생하는 내분비 종양입니다.
        - 증상: 호르몬 과다 분비(거인증, 유루증 등) 또는 시신경 교차 압박으로 인한 시야 장애를 유발합니다.
        """)

    with st.container(border=True):
        st.markdown("""
        **3. Brain Metastasis (전이성 뇌종양)**
        - 경로: 폐암, 유방암 등이 혈류를 타고 뇌로 전이된 경우입니다.
        - 양상: 다발성인 경우가 많으며, 종양 세포 주위로 극심한 '혈관성 부종'이 동반되는 것이 진단의 단세입니다.
        """)

# --- Tab 2: 시퀀스 임상 의미 (세로형 배치) ---
with tabs[1]:
    st.header("2. MRI 시퀀스별 임상적 가치와 판독 원리")
    st.write("MRI의 각 시퀀스는 물리학적 신호가 달라, 이를 '멀티 파라미터'로 분석해야 정확한 진단이 가능합니다.")
    
    if os.path.exists(MODALITIES_IMG):
        st.image(MODALITIES_IMG, caption="MRI 모달리티 대조 가이드 (T1, T1ce, T2, FLAIR)", use_container_width=True)
    
    st.divider()
    
    st.markdown("### 조영 증강의 원리 (T1ce)")
    st.info("""
    종양 세포가 자라면서 정상적인 혈관-뇌 장벽(BBB)을 파괴하거나 신생 혈관을 만듭니다. 
    이때 조영제가 혈관 밖으로 유출되어 종양 부위를 밝게(High Signal) 만듭니다. 
    이는 종양의 '활동성'과 '악성도'를 직접적으로 반영하는 가장 중요한 지표입니다.
    """)
    
    st.markdown("### 기본 해부학 (T1 / T2)")
    with st.container(border=True):
        st.write("- T1: 해부학적 해상도가 좋아 종양의 정확한 해부학적 위치를 파악할 때 사용합니다.")
        st.write("- T2: 뇌척수액과 수분을 밝게 보여주어 병변의 액체 성분을 식별합니다.")

    st.markdown("### 부종(Edema)의 식식별 (FLAIR)")
    st.warning("""
    FLAIR는 T2 영상에서 뇌척수액의 밝은 신호를 검게 눌러버리는 기술입니다. 
    결과적으로 뇌척수액이 아닌 종양 주변의 병적인 부종(Vasogenic Edema)이나 미세한 침윤 구역만을 밝게 도드라지게 보여줍니다. 
    고등급 종양일수록 이 FLAIR 고신호 영역이 넓게 나타나는데, 이는 수술 범위를 결정하는 결정적인 근거가 됩니다.
    """)

# --- Tab 3: 정밀 판독 포인트 (세로형 배치) ---
with tabs[2]:
    st.header("3. 임상 사례별 정밀 판독 포인트 (Diagnostic Pearls)")
    
    if os.path.exists(TUMOR_IMG):
        st.image(TUMOR_IMG, caption="주요 종양별 MRI 시결 시각적 특징 대조", use_container_width=True)
    
    st.divider()
    
    st.markdown("### Glioma / GBM 판독")
    with st.container(border=True):
        st.write("- 중심 괴사: 악성도가 높을수록 중심부에 피가 통하지 않아 썩은(검은) 부위가 생깁니다.")
        st.write("- Ring Enhancement: 괴사 주변으로 테를 두른 듯한 조영 증강이 나타납니다.")
        st.write("- 미만성 침윤: 육안으로 보이는 종양 너머로 이미 암세포가 퍼져 있을 확률이 매우 높습니다.")

    st.markdown("### Meningioma 판독")
    with st.container(border=True):
        st.write("- Dural Tail Sign: 종양 근처의 뇌막이 꼬리처럼 두꺼워져 있는 고유한 특징입니다.")
        st.write("- Extra-axial: 뇌 실질 밖에서 뇌를 안으로 밀어내는 '압박' 양상을 확인하세요.")

    st.markdown("### Pituitary Adenoma 판독")
    with st.container(border=True):
        st.write("- Snowman Sign: 터키장 내부에서 위로 솟구치며 '눈사람' 혹은 '8자' 모양으로 보입니다.")
        st.write("- 시교차 압박: 바로 위의 시신경이 눌려 있는지 보는 것이 임상적으로 가장 중요합니다.")

    st.markdown("### Metastasis 판독")
    with st.container(border=True):
        st.write("- 다발성 결절: 한 군데가 아니라 여러 군데 점처럼 박혀 있다면 전이를 의심해야 합니다.")
        st.write("- 과도한 부종: 종양은 작은데 주변 부종이 뇌의 절반을 차지할 정도로 심한 것이 특징입니다.")

st.sidebar.markdown("### 판독 교육 전문가 가이드")
st.sidebar.info("""
MRI 판독의 핵심은 '대조'입니다. 
T1ce에서 보이는 종양의 '형체'와 FLAIR에서 보이는 종양의 '영향권'을 항상 동시에 비교하십시오. 
그 간격이 넓을수록 종양의 침습성이 높다는 뜻입니다.
""")

import streamlit as st
import pandas as pd
import os

# 페이지 설정
st.set_page_config(page_title="WHO CNS5 전문 학습 모듈", page_icon="🎓", layout="wide")

# 이미지 경로 설정
IMAGE_PATHS = {
    "glioma": os.path.join("assets", "tumor_sample.png"),
    "meningioma": r"C:\Users\USER\.gemini\antigravity\brain\cfca39f9-8897-4f72-a54e-c345b32f849d\meningioma_sample_png_1775653524093.png",
    "pituitary": r"C:\Users\USER\.gemini\antigravity\brain\cfca39f9-8897-4f72-a54e-c345b32f849d\pituitary_pitnet_sample_png_1775653624283.png",
    "others": r"C:\Users\USER\.gemini\antigravity\brain\cfca39f9-8897-4f72-a54e-c345b32f849d\schwannoma_metastasis_sample_png_1775653752599.png",
    "modalities": os.path.join("assets", "modalities_sample.png")
}

# 사이드바 레이아웃
st.sidebar.title("📖 학습 목차")
main_category = st.sidebar.radio(
    "주제를 선택하세요",
    ["1. WHO CNS5 개정 패러다임", "2. 종양별 진단분류체계", "3. 학습 데이터 및 모델 리포트"]
)

# --- 1. WHO CNS5 개정 패러다임 ---
if main_category == "1. WHO CNS5 개정 패러다임":
    st.header("중추신경계 종양 분류 5판 (WHO Classification of Tumors of the Central Nervous System, 5th Edition)")
    
    st.subheader("🚩 주요 개정 내역 상세 (4판 vs 5판)")
    with st.container():
        st.markdown("""
        #### 1) 진단 명명법의 변화 (Nomenclature)
        - ~~조직학적 소견 중심의 단일 진단명~~ $\rightarrow$ **통합 진단(Integrated Diagnosis) 의무화**
        - ~~로마 숫자 등급 표기 (Grade I, II, III, IV)~~ $\rightarrow$ **아라비아 숫자 표기 (Grade 1, 2, 3, 4)**
        
        #### 2) 등급 시스템의 혁신 (Grading)
        - ~~종양 전체에 적용되는 보편적 등급~~ $\rightarrow$ **유형 내 등급(Within-type Grading) 도입**
        - **분자적 마커에 의한 즉각적 등급 부여**: 
            - ~~모양만으로 등급 결정~~ $\rightarrow$ **CDKN2A/B 결실 확인 시 즉시 4등급 진단**

        #### 3) 명칭의 삭제 및 변경
        - ~~교모세포종, IDH-변이형 (Glioblastoma, IDH-mutant)~~ $\rightarrow$ **폐기 (성상세포종, IDH-변이형으로 통합)**
        - ~~뇌하수체 선종 (Pituitary Adenoma)~~ $\rightarrow$ **뇌하수체 신경내분비종양 (Pituitary Neuroendocrine Tumor, PitNET)**
        """)

# --- 2. 종양별 진단분류체계 (상세 의학 정보 강화) ---
elif main_category == "2. 종양별 진단분류체계":
    st.header("종양군별 상세 진단 분류")
    
    tumor_type = st.selectbox(
        "확인하고 싶은 종양군을 선택하세요",
        ["신경교종 (Glioma)", "수막종 (Meningioma)", "뇌하수체 종양 (Pituitary Neuroendocrine Tumor)", "기본 신경초종/전이성/기타"]
    )

    st.divider()
    st.subheader(f"{tumor_type}")

    # 데이터 매핑 (의학용어 병기 및 상세 내용 강화)
    if tumor_type == "신경교종 (Glioma)":
        data = {
            "symptoms": "종양의 위치에 따라 다르나 주로 심한 두통, 오심(Nausea) 및 구토(Vomiting), 발작(Seizure), 성격 변화 및 인지 기능 저하가 나타납니다.",
            "causes": "대부분 명확한 외부 요인보다는 유전자 변이(IDH 변이, ATRX 손실 등)와 세포 분학적 오류에 기인합니다.",
            "subtypes": """
            - **성상세포종 (Astrocytoma, IDH-mutant)**: 별 모양의 아교세포에서 발생하며, Grade 2에서 4까지 진행됩니다. 유전자 변이 여부에 따라 예후가 결정됩니다.
            - **핍지교종 (Oligodendroglioma, IDH-mutant and 1p/19q-codeleted)**: 신경 수초를 만드는 세포에서 발생하며, 특징적인 유전자 공손실을 보이고 대개 진행이 느립니다.
            - **교모세포종 (Glioblastoma, IDH-wildtype)**: 가장 흔하고 악랄한 4등급 종양으로, 매우 빠른 침윤성과 괴사를 보이며 치료 저항성이 강합니다.
            """,
            "img": IMAGE_PATHS["glioma"],
            "img_cap": "[신경교종] 중앙 괴사와 환상 조영 증강 (Ring Enhancement) 현상",
            "guide": "테두리 조영 증강(Ring enhancement)은 악성도가 높은 교모세포종의 핵심 징후입니다."
        }
    elif tumor_type == "수막종 (Meningioma)":
        data = {
            "symptoms": "종양이 서서히 자라므로 초기 증상은 미미하나, 뇌를 압박함에 따라 국소 마비, 시야 장애, 후각 상실 등이 나타날 수 있습니다.",
            "causes": "22번 염색체(NF2 유전자)의 결손과 연관이 깊으며, 드물게 과거 방사선 노출 이력이 원인이 되기도 합니다.",
            "subtypes": """
            - **수막세포형 수막종 (Meningothelial Meningioma)**: 가장 흔한 양성(Grade 1)으로 경계가 명확하고 수술적 제거 시 예후가 매우 좋습니다.
            - **비정형성 수막종 (Atypical Meningioma)**: Grade 2로 분류되며, 양성보다 세포 분열이 활발하여 재발 위험이 상대적으로 높습니다.
            - **역형성 수막종 (Anaplastic/Malignant Meningioma)**: Grade 3의 악성 종양으로 뇌 조직을 직접 침범하며 전이가 발생할 수 있습니다.
            """,
            "img": IMAGE_PATHS["meningioma"],
            "img_cap": "[수막종] 뇌막 유래의 균일한 조영 증강 및 꼬리 징후 (Dural Tail Sign)",
            "guide": "Dural Tail Sign은 주변 뇌막이 꼬리처럼 두꺼워지는 현상으로 수막종의 결정적 지표입니다."
        }
    elif tumor_type == "뇌하수체 종양 (Pituitary Neuroendocrine Tumor)":
        data = {
            "symptoms": "호르몬 과다 분비로 인한 유즙 분비, 거인증(Acromegaly) 혹은 호르몬 부족 증상이 나타나며, 시신경 압박 시 양측성 반맹(Bitemporal Hemianopsia)이 발생합니다.",
            "causes": "뇌하수체 세포의 단일 클론성 증식으로 발생하며, 드물게 다발성 내분비 종양증(MEN1)과 같은 유전적 요인이 작용합니다.",
            "subtypes": """
            - **기능성 종양 (Functioning Tumor)**: 프로락틴, 성장호르몬 등을 과다 분비하여 신체 대사 이상을 직접적으로 유발합니다.
            - **비기능성 종양 (Non-functioning Tumor)**: 호르몬 분비는 없으나 크기가 커지면서 주변 신경과 뇌하수체를 압박하는 질량 효과(Mass Effect)를 보입니다.
            """,
            "img": IMAGE_PATHS["pituitary"],
            "img_cap": "[뇌하수체 종양] 안장 입구에서 잘록해진 후 위로 솟은 눈사람 (Snowman Sign) 양상",
            "guide": "눈사람 모양은 종양이 좁은 입구를 통과해 위로 확장되었음을 시사하며 시력 장애와 직결됩니다."
        }
    else:
        data = {
            "symptoms": "신경초종은 청력 상실 및 이명을, 전이암은 갑작스러운 마비나 발작을, 수모세포종은 소아의 보행 장애를 유발합니다.",
            "causes": "전이암은 타 장기의 암세포 혈류 이동이 원인이며, 신경초종은 신경초 세포의 비정상 증식(NF2 관련) 때문입니다.",
            "subtypes": """
            - **전이성 뇌종양 (Brain Metastasis)**: 폐암, 유방암 등이 원발암이며 뇌의 여러 곳에 다발성으로 나타나는 특징이 있습니다.
            - **신경초종 (Schwannoma)**: 주로 뇌신경 껍질에서 발생하며 전정신경(청신경) 부위에서 아이스크림 콘 모양으로 관찰됩니다.
            - **수모세포종 (Medulloblastoma)**: 소아 소뇌에서 발생하는 매우 공격적인 배아 종양으로 분자학적 분류가 매우 중요합니다.
            """,
            "img": IMAGE_PATHS["others"],
            "img_cap": "[기타] 좌: 신경초종의 아이스크림 모양 / 우: 전이암의 다발성 병변과 심한 부종",
            "guide": "전이암은 물리적 크기보다 주변의 부종(Peritumoral Edema)이 훨씬 넓게 형성되는 불균형적 특징이 있습니다."
        }

    # 수직형 배치
    st.markdown(f"**증상 특징**: {data['symptoms']}")
    st.markdown(f"**주요 원인**: {data['causes']}")
    st.write("")
    st.markdown("**진단 하위유형 및 특징**:")
    st.write(data['subtypes'])

    if os.path.exists(data['img']):
        st.write("---")
        st.image(data['img'], caption=data['img_cap'], use_container_width=True)
        st.write("---")

    with st.expander("🔍 전문 영상판독 가이드 및 용어 설명", expanded=True):
        st.write(data['guide'])

# --- 3. 학습 데이터 및 모델 리포트 ---
elif main_category == "3. 학습 데이터 및 모델 리포트":
    st.header("학습 데이터 및 모델 리포트")
    if os.path.exists(IMAGE_PATHS["modalities"]):
        st.image(IMAGE_PATHS["modalities"], caption="MRI 4대 기법별 시각적 차이 (T1, T1ce, T2, FLAIR)", use_container_width=True)
    if os.path.exists('comparison_results.csv'):
        st.dataframe(pd.read_csv('comparison_results.csv'), use_container_width=True)

st.divider()
st.caption("Reference: WHO Classification of Tumors, 5th Edition (CNS5, 2021)")

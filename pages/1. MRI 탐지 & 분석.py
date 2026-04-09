import streamlit as st
from PIL import Image
import numpy as np
import os
from utils.detector import BrainTumorDetector
from utils.database import save_detection_result

# 페이지 설정
st.set_page_config(page_title="MRI 탐지 & 분석 - 뇌 MRI", page_icon="🔍", layout="wide")

# 모델 초기화
@st.cache_resource
def get_detector():
    return BrainTumorDetector('weights/model_30p_ep50.pt')

detector = get_detector()

st.title("🔍 뇌 MRI 종양 탐지 및 분석")
st.error("❗ **탐지 범위 제약**: 현재 모델은 **교종(Glioma)** 관련 3가지 영역(NCR, ED, ET)만 탐지 가능합니다. 학습 자료에 명시된 수막종, 뇌하수체 종양 등은 탐지 대상이 아님을 유의해 주세요.")
st.markdown("MRI 슬라이스 이미지를 업로드하여 AI 모델이 학습한 종양 위치를 확인하세요.")

# 레이아웃 구성
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("🖼️ MRI 이미지 업로드")
    uploaded_file = st.file_uploader("이미지 파일 선택 (PNG, JPG, JPEG)", type=['png', 'jpg', 'jpeg'])
    
    if uploaded_file:
        image = Image.open(uploaded_file).convert('RGB')
        st.image(image, caption="업로드된 원본 이미지", use_container_width=True)
        detect_button = st.button("종양 탐지 시작 🚀", use_container_width=True)

with col2:
    st.subheader("🎯 탐지 결과 시각화")
    if uploaded_file and detect_button:
        with st.spinner("이미지를 분석하고 있습니다..."):
            img_array = np.array(image)
            results = detector.predict(img_array)
            res_plotted = results[0].plot()
            res_image = Image.fromarray(res_plotted[..., ::-1])
            st.image(res_image, caption="탐지 알고리즘 적용 결과", use_container_width=True)
            
            summary = detector.get_summary(results)
            if summary["detected"]:
                st.success(f"✅ 종양이 탐지되었습니다! (총 {summary['count']}개)")
                m1, m2 = st.columns(2)
                top_conf = summary["boxes"][0]["confidence"]
                m1.metric("최고 신뢰도", f"{top_conf:.1%}")
                m2.metric("탐지 개수", f"{summary['count']}개")

                st.write("---")
                st.subheader("📋 탐지 상세 정보 (종양 좌표)")
                detail_data = []
                for idx, box_info in enumerate(summary["boxes"]):
                    x, y, w, h = box_info["bbox"]
                    detail_data.append({
                        "ID": f"Tumor_{idx+1}",
                        "Confidence": f"{box_info['confidence']:.2%}",
                        "Center X": round(x, 1),
                        "Center Y": round(y, 1),
                        "Width": round(w, 1),
                        "Height": round(h, 1)
                    })
                st.table(detail_data)

                with st.expander("💾 데이터베이스 기록 상태"):
                    db_res = save_detection_result(
                        image_name=uploaded_file.name,
                        detection_count=summary['count'],
                        max_confidence=top_conf,
                        details=summary['boxes']
                    )
                    if db_res:
                        st.info("📊 탐지 이력이 Supabase에 성공적으로 기록되었습니다.")
            else:
                st.info("🧐 종양이 탐지되지 않았습니다.")
                save_detection_result(uploaded_file.name, 0, 0.0, [])
    else:
        st.info("왼쪽에서 이미지를 업로드하고 탐지 시작 버튼을 눌러주세요.")

st.divider()
with st.expander("ℹ️ 이용 안내"):
    st.markdown("""
    - 본 서비스는 BraTS 2021 데이터셋으로 학습된 YOLOv8 모델을 기반으로 합니다.
    - 탐지 결과는 학습 보조용이며, 실제 의학적 진단은 전문의와 상담하시기 바랍니다.
    """)

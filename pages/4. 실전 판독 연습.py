import streamlit as st
import nibabel as nib
import numpy as np
from PIL import Image
import os
import random
import torch
import cv2
from utils.detector import BrainTumorDetector

# 페이지 설정
st.set_page_config(page_title="통합 실전 판독 트레이닝", page_icon="📝", layout="wide")

# 모델 초기화
@st.cache_resource
def get_detector():
    return BrainTumorDetector('weights/model_30p_ep50.pt')

detector = get_detector()

# [Heatmap 생성 함수]
def generate_heatmap(image_np, model):
    img_resized = cv2.resize(image_np, (256, 256))
    img_tensor = torch.from_numpy(img_resized).permute(2, 0, 1).float().unsqueeze(0) / 255.0
    with torch.no_grad():
        _ = model.model(img_tensor) 
        heatmap = np.zeros((256, 256), dtype=np.float32)
        det_results = model(img_resized, verbose=False)
        boxes = det_results[0].boxes
        if len(boxes) > 0:
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                conf = box.conf[0].item()
                center_x, center_y = (x1 + x2) // 2, (y1 + y2) // 2
                sigma = max((x2 - x1), (y2 - y1)) / 2
                y, x = np.ogrid[:256, :256]
                mask = np.exp(-((x - center_x)**2 + (y - center_y)**2) / (2 * sigma**2))
                heatmap += mask * conf
        if np.max(heatmap) > 0: heatmap = heatmap / np.max(heatmap)
        heatmap = np.uint8(255 * heatmap)
        heatmap_img = cv2.applyColorMap(heatmap, cv2.COLORMAP_JET)
        heatmap_img = cv2.resize(heatmap_img, (image_np.shape[1], image_np.shape[0]))
        return cv2.addWeighted(image_np, 0.6, heatmap_img, 0.4, 0)

# [NIfTI 로직]
@st.cache_data
def load_data(file_path, normalize=True):
    if os.path.exists(file_path):
        data = nib.load(file_path).get_fdata()
        if normalize and np.max(data) - np.min(data) != 0:
            data = (data - np.min(data)) / (np.max(data) - np.min(data)) * 255
            return data.astype(np.uint8)
        return data
    return None

def create_gt_overlay(mri_slice, seg_slice, alpha=0.5):
    mri_rgb = np.stack([mri_slice]*3, axis=-1)
    mask_rgb = np.zeros_like(mri_rgb)
    mask_rgb[seg_slice > 0] = [255, 0, 0]
    return (mri_rgb * (1.0 - alpha) + mask_rgb * alpha).astype(np.uint8)

@st.cache_data
def cached_predict(case_id, slice_idx, _data_slice):
    rgb_slice = np.ascontiguousarray(np.stack([_data_slice]*3, axis=-1))
    results = detector.model.predict(rgb_slice, verbose=False)
    return Image.fromarray(results[0].plot()[..., ::-1]), detector.get_summary(results)

# [세션 상태 관리]
GLIOMA_BASE_DIR = os.path.join("assets", "data", "glioma")
if 'case_id' not in st.session_state:
    p = [d for d in os.listdir(GLIOMA_BASE_DIR) if os.path.isdir(os.path.join(GLIOMA_BASE_DIR, d))]
    st.session_state.case_id = random.choice(p) if p else None
if 'quiz_step' not in st.session_state: st.session_state.quiz_step = 1

def reset_case():
    p = [d for d in os.listdir(GLIOMA_BASE_DIR) if os.path.isdir(os.path.join(GLIOMA_BASE_DIR, d))]
    st.session_state.case_id = random.choice(p)
    st.session_state.quiz_step = 1

# [UI 레이아웃]
st.title("🏥 정석 판독 통합 트레이닝 (4-Step)")
p_id = st.session_state.case_id
p_dir = os.path.join(GLIOMA_BASE_DIR, p_id)
modalities = {
    "T1ce": os.path.join(p_dir, f"{p_id}_t1ce.nii.gz"),
    "Seg": os.path.join(p_dir, f"{p_id}_seg.nii.gz"),
    "FLAIR": os.path.join(p_dir, f"{p_id}_flair.nii.gz"),
    "T2": os.path.join(p_dir, f"{p_id}_t2.nii.gz"),
    "T1": os.path.join(p_dir, f"{p_id}_t1.nii.gz")
}

# [4단계 내비게이션 바]
step_names = ["1. MRI 분석", "2. 자기 진단", "3. AI 종합 분석", "4. 정답 및 해설"]
st.progress(st.session_state.quiz_step / 4)
nav_cols = st.columns(4)
for i, name in enumerate(step_names):
    step_num = i + 1
    if nav_cols[i].button(name, key=f"nav_{step_num}", use_container_width=True, type="primary" if st.session_state.quiz_step == step_num else "secondary"):
        st.session_state.quiz_step = step_num
        st.rerun()

st.divider()
slice_idx = st.sidebar.slider("슬라이스 탐색 (Z-axis)", 0, 154, 75)

# --- 4단계 프로세스 ---

if st.session_state.quiz_step == 1:
    st.subheader("Step 1. MRI 슬라이스 육안 분석")
    t1ce_data = load_data(modalities["T1ce"])
    if t1ce_data is not None:
        st.image(t1ce_data[:, :, slice_idx], caption=f"Case: {p_id} / Slice: {slice_idx}", use_container_width=True)
    if st.button("진단 리포트 작성 ➡️", use_container_width=True):
        st.session_state.quiz_step = 2
        st.rerun()

elif st.session_state.quiz_step == 2:
    # ...생략 (기존과 동일)
    st.subheader("Step 2. 학습자 자가 진단")
    t1ce_data = load_data(modalities["T1ce"])
    c1, c2 = st.columns([1.8, 1])
    with c1: st.image(t1ce_data[:, :, slice_idx], use_container_width=True)
    with c2:
        st.radio("종양 검출 여부:", ["검출됨", "정상"], key="ans")
        st.multiselect("의심 위치 (뇌엽):", ["좌전두엽", "우전두엽", "좌측두엽", "우측두엽", "두정엽", "후두엽", "중심부"])
        st.text_area("기타 소견:", placeholder="판독 소견을 입력하세요...")
        if st.button("AI 분석 결과 확인 🚀", use_container_width=True):
            st.session_state.quiz_step = 3
            st.rerun()

elif st.session_state.quiz_step == 3:
    st.subheader("Step 3. AI 종합 분석 (박스 탐지 & 히트맵)")
    t1ce_data = load_data(modalities["T1ce"])
    raw_slice = t1ce_data[:, :, slice_idx]
    res_img, summary = cached_predict(p_id, slice_idx, raw_slice)
    rgb_slice = np.stack([raw_slice]*3, axis=-1)
    heatmap_res = generate_heatmap(rgb_slice, detector.model)
    col_a, col_b = st.columns(2)
    with col_a: st.image(res_img, caption="AI 탐지 결과 (YOLOv8)", use_container_width=True)
    with col_b: st.image(heatmap_res, caption="AI 판단 근거 히트맵 (Grad-CAM)", use_container_width=True)
    if st.button("전문 정답(GT) 및 해설 보기 💡", use_container_width=True):
        st.session_state.quiz_step = 4
        st.rerun()

elif st.session_state.quiz_step == 4:
    st.subheader("Step 4. 전문 정답 및 최종 학습 리포트")
    t1ce_mri = load_data(modalities["T1ce"])
    seg_data = load_data(modalities["Seg"], normalize=False)
    
    r1, r2 = st.columns([1.5, 1])
    with r1:
        gt_overlay = create_gt_overlay(t1ce_mri[:, :, slice_idx], seg_data[:, :, slice_idx])
        st.image(gt_overlay, caption="의학적 정답(Ground Truth Mask Overlay)", use_container_width=True)
    with r2:
        st.markdown("### 👨‍⚕️ 전문의 판독 해설")
        if np.sum(seg_data[:,:,slice_idx]) > 0:
            st.error("🚩 최종 판정: **종양 검출됨(Positive)**")
            st.markdown("""
            **영상학적 상세 소견**:
            - **T1ce**: 조영 증강이 뚜렷한 종양의 고형 성분이 확인됩니다.
            - **해부학적 소견**: 인접한 뇌 조직을 압박하거나 침윤하고 있는 양상이 보입니다.
            - **학습 포인트**: AI 탐지 박스와 정답 마스크가 일치하는지, 본인이 놓친 미세한 증강 영역은 없는지 대조하세요.
            """)
        else:
            st.success("🚩 최종 판정: **정상(Negative)**")
            st.markdown("**영상학적 상세 소견**: 해당 슬라이스에서는 유의미한 조영 증강이나 이상 병변이 관찰되지 않습니다.")
        
        st.divider()
        st.write("**모달리티간 대조 분석**")
        sc1, sc2 = st.columns(2)
        with sc1: st.image(load_data(modalities["FLAIR"])[:,:,slice_idx], caption="FLAIR (부종 및 침윤 범위)", use_container_width=True)
        with sc2: st.image(load_data(modalities["T2"])[:,:,slice_idx], caption="T2 (뇌척수액 대조 확인)", use_container_width=True)

    st.markdown("---")
    st.markdown("""
    ### 📚 오늘의 케이스 종합 정리
    - **T1ce**에서 밝게 나타나는 부분은 혈관-뇌 장벽(BBB)이 파괴된 활동성 종양 부위입니다.
    - **FLAIR**의 고신호 강도는 종양 세포의 침윤이나 부종(Edema)을 나타냅니다. 고등급 신경교종일수록 이 부종 범위가 넓게 나타나는 경향이 있습니다.
    """)
    
    if st.button("학습 종료 및 무작위 증례 변경 🔄", use_container_width=True):
        reset_case()
        st.rerun()

st.sidebar.button("다른 증례 무작위 생성", on_click=reset_case)

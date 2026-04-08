import streamlit as st
from supabase import create_client, Client

def get_supabase_client() -> Client:
    """
    Streamlit secrets에서 정보를 가져와 Supabase 클라이언트를 생성합니다.
    """
    try:
        url = st.secrets["supabase"]["url"]
        key = st.secrets["supabase"]["key"]
        return create_client(url, key)
    except Exception as e:
        st.error(f"Supabase 설정 로드 실패: {e}")
        return None

def save_detection_result(image_name: str, confidence: float, detected: bool, bbox: list = None):
    """
    탐지 결과를 Supabase 'detections' 테이블에 저장합니다.
    """
    client = get_supabase_client()
    if not client:
        return

    data = {
        "image_name": image_name,
        "confidence": float(confidence),
        "detected": detected
    }

    # 바운딩 박스 정보가 있을 경우 추가 (x, y, w, h 가 순서대로 들어있다고 가정)
    if bbox and len(bbox) == 4:
        data.update({
            "bbox_x": float(bbox[0]),
            "bbox_y": float(bbox[1]),
            "bbox_w": float(bbox[2]),
            "bbox_h": float(bbox[3])
        })

    try:
        response = client.table("detections").insert(data).execute()
        return response
    except Exception as e:
        print(f"DB 저장 오류: {e}")
        return None

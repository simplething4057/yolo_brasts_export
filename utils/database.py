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
        # secrets가 설정되지 않았을 때는 에러를 띄우지 않고 None 반환 (사용자 혼동 방지)
        return None

def save_detection_result(image_name: str, detection_count: int, max_confidence: float, details: list):
    """
    탐지 결과를 Supabase 'detections' 테이블에 저장합니다.
    SQL 테이블 구조와 일치하도록 매핑합니다.
    """
    client = get_supabase_client()
    if not client:
        return None

    data = {
        "image_name": image_name,
        "detection_count": int(detection_count),
        "max_confidence": float(max_confidence),
        "details": details  # 탐지된 객체들의 상세 정보 (좌표 등)를 JSON 형태로 저장
    }

    try:
        response = client.table("detections").insert(data).execute()
        return response
    except Exception as e:
        # 에러 발생 시 Streamlit 화면에 출력하여 디버깅 지원
        st.sidebar.error(f"DB 저장 오류: {e}")
        return None

def fetch_detection_history(limit: int = 100):
    """
    Supabase 'detections' 테이블에서 최근 탐지 이력을 가져옵니다.
    """
    client = get_supabase_client()
    if not client:
        return None

    try:
        response = client.table("detections").select("*").order("created_at", desc=True).limit(limit).execute()
        return response.data
    except Exception as e:
        st.error(f"데이터 조회 오류: {e}")
        return []

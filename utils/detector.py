import streamlit as st
from ultralytics import YOLO
import numpy as np

class BrainTumorDetector:
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = self.load_model()

    @st.cache_resource
    def load_model(_self):
        """
        모델을 캐싱하여 반복 로드를 방지합니다.
        """
        return YOLO(_self.model_path)

    def predict(self, image, conf=0.3):
        """
        이미지에서 종양을 탐지하고 결과를 반환합니다.
        """
        results = self.model.predict(
            source=image,
            conf=conf,
            save=False,
            verbose=False
        )
        return results

    def get_summary(self, results):
        """
        추론 결과에서 주요 정보를 추출합니다.
        """
        if not results:
            return None
            
        boxes = results[0].boxes
        count = len(boxes)
        
        summary = {
            "count": count,
            "detected": count > 0,
            "boxes": []
        }
        
        if count > 0:
            for box in boxes:
                # [x, y, w, h, conf, cls] 형태 추출
                xywh = box.xywh[0].tolist() # 중심x, 중심y, 너비, 높이
                confidence = float(box.conf[0].item())
                summary["boxes"].append({
                    "bbox": xywh,
                    "confidence": confidence
                })
        
        return summary

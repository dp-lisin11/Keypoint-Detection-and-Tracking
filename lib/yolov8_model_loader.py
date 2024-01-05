from ultralytics import YOLO
import cv2

class YOLOv8ModelLoader:
    def __init__(self, model_path='yolov8m.pt'):
        self.model = YOLO(model_path)

    def detect_objects(self, frame):
        # Run YOLOv8 object detection on the frame
        detections = self.model.predict(frame)
        
        # Process detections and extract relevant information
        objects = []
        for detection in detections:
            try:
                box=detection[0].boxes
                bbox=detection[0].boxes.xyxy
                confidence=detection[0].boxes.conf.item()
                class_name = detection[0].names[box.cls[0].item()]
                
                # Append the detected object information to the result list
                objects.append({
                    'class': class_name,
                    'confidence': confidence,
                    'bbox': bbox.tolist()  # Convert NumPy array to list
                })
            except Exception as e:
                print(e)
            
            #print(detection)
        return objects
    
    
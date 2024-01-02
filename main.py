from camera_streamer import CameraStreamer
from yolov8_model_loader import YOLOv8ModelLoader
from keypoint_detection_model_loader import KeypointDetectionModelLoader
from analysis_module import AnalysisModule

def main():
    camera_streamer = CameraStreamer()  # 0 for default webcam, replace it with the IP address for IP cameras
    yolo_model_loader = YOLOv8ModelLoader()
    keypoint_model_loader =KeypointDetectionModelLoader()
    analysis_module = AnalysisModule(camera_streamer, keypoint_model_loader, yolo_model_loader)
    analysis_module.start_analysis('output.json')
    

if __name__ == "__main__":
    main()

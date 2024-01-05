from camera_streamer import CameraStreamer
from yolov8_model_loader import YOLOv8ModelLoader
from keypoint_detection_model_loader import KeypointDetectionModelLoader
from analysis_module import AnalysisModule
from Pose_detection import PoseDetectionModelLoader

def main():  
    # 0 for default webcam, replace it with the IP address for IP cameras
    camera_streamer = CameraStreamer(0)
    pose_loader=PoseDetectionModelLoader()
    
    # Loading the models
    yolo_model_loader = YOLOv8ModelLoader()
    keypoint_model_loader =KeypointDetectionModelLoader()
    
    # Start analysis and store results in json file
    analysis_module = AnalysisModule(camera_streamer, keypoint_model_loader, yolo_model_loader,pose_loader)
    analysis_module.start_analysis('output.json')
    
if __name__ == "__main__":
    main()

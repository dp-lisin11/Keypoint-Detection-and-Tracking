import json


class AnalysisModule:
    def __init__(self, camera_loader, keypoint_model_loader, yolo_model_loader):
        self.camera_loader = camera_loader
        self.keypoint_model_loader = keypoint_model_loader
        self.yolo_model_loader = yolo_model_loader
        # self.pose_loader = pose_loader

    def start_analysis(self, output_file):
        with open(output_file, 'w') as json_file:
            while True:
                # Get the frame from camera_streamer and start streaming
                frame = self.camera_loader.get_frame()
                self.camera_loader.start_streaming()
                
                # Run YOLOv8 object detection
                yolo_objects = self.yolo_model_loader.detect_objects(frame)
                
                # Run human body keypoint detection
                keypoints = self.keypoint_model_loader.detect_keypoints(frame)
                
                # Save results to JSON
                results = {"YOLOv8Result": yolo_objects, "KeyPointResult": keypoints}
                json.dump(results, json_file)
                

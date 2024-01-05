# Keypoint Detection and Tracking
## Overview
This project consists of two modules: Camera Streamer and Analysis. The Camera Streamer module captures video streams from different sources, including webcams and IP cameras, and provides a method for starting the streaming process. The Analysis module utilizes the Camera Streamer module and integrates YOLOv8 object detection and MediaPipe keypoint detection to analyze frames from the camera stream. The analysis results are saved in a JSON file.

## Modules
#### 1. Camera Streamer
Usage:
```python
# Import the module
from camera_streamer import CameraStreamer

# Initialize the Camera Streamer
streamer = CameraStreamer()

# Start streaming from the default camera (Webcam)
streamer.start_streaming()
```
#### 2. Analysis
Usage:
```python
# Import the module
from analysis import AnalysisModule

# Initialize the Analysis Module with the Camera Streamer
analysis_module = AnalysisModule()

# Start the analysis process
analysis_module.start_analysis()
```

## YOLOv8 Model Loader
The YOLOv8 Model Loader is responsible for loading the YOLOv8 object detection model and making predictions on frames from the camera stream.

Usage:
```python
# Import the YOLOv8 Model Loader
from yolo_model_loader import YOLOv8ModelLoader

# Initialize the YOLOv8 Model Loader
yolo_loader = YOLOv8ModelLoader()

# Detect objects in a frame
frame = cv2.imread('example_frame.jpg')  # Replace with actual frame
objects = yolo_loader.detect_objects(frame)
print(objects)
```
Example Output:
```python

[{
    'class': 'person',
    'confidence': 0.95,
    'bbox': [x_min, y_min, x_max, y_max]
},
...
]
```
## MediaPipe Keypoint Detection
The MediaPipe Keypoint Detection is responsible for detecting and tracking body keypoints in frames from the camera stream.

Usage:
```python
# Import the MediaPipe Keypoint Detection
from keypoint_detection_model_loader import KeypointDetectionModelLoader

# Initialize the Keypoint Model Loader
keypoint_loader = KeypointDetectionModelLoader()

# Detect keypoints in a frame
frame = cv2.imread('example_frame.jpg')  # Replace with actual frame
keypoints = keypoint_loader.detect_keypoints(frame)
print(keypoints)
```
Example Output:
```python
[{
    'landmark_index': 0,
    'x': 0.638852,
    'y': 0.671197,
    'z': 0.129959,
    'visibility': 0.9999997615814209,
    'presence': 0.9999984502792358
},
...
]
```

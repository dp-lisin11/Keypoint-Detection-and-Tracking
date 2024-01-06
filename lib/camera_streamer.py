import cv2
import time
from ultralytics import YOLO
import mediapipe as mp
from keypoint_detection_model_loader import KeypointDetectionModelLoader
import numpy
#from Pose_detection import PoseDetectionModelLoader

keypoint_detector = KeypointDetectionModelLoader()
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

class CameraStreamer:
    def __init__(self, source=0):
        self.source = source
        self.cap = cv2.VideoCapture(source)   
        self.start_time = time.time()
        self.frame_count = 0
        self.model = YOLO('yolov8m.pt')
        #self.pose_loader=PoseDetectionModelLoader()

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            print("Failed to grab frame")
        return frame

    def start_streaming(self):
        while True:
            frame = self.get_frame()
            if frame is None:
                break
            
            # Calculate FPS
            self.frame_count += 1
            elapsed_time = time.time() - self.start_time
            fps = self.frame_count / elapsed_time

            # Display FPS on the frame
            cv2.putText(frame, f"FPS: {fps:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            """
            The following code is to open object detection window
            """
            self.model(source=frame, show=True, conf=0.4, save=False)
            
            """
            The following code is to view landmarks in the camera stream
            """
            results = mp_pose.Pose(static_image_mode=True).process(frame)   
            circle_radius = int(.007 * frame.shape[1])
            # Specifies the drawing style for the 'landmarks'.
            point_spec = mp_drawing.DrawingSpec(color=(220, 100, 0), thickness=-1, circle_radius=circle_radius)
            # Draws the 'landmarks' on the image.
            mp_drawing.draw_landmarks(frame,
                              landmark_list=results.pose_landmarks,
                              landmark_drawing_spec=point_spec)       
           
            keypoints = keypoint_detector.detect_keypoints(frame)
            if keypoints is not None:
                mp.solutions.drawing_utils.draw_landmarks(frame, results.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)

            if keypoint_detector.has_crossed_line(frame,line_end=(640, 200),line_start=(0, 200)) and results.pose_landmarks:
                cv2.line(frame, (0, 200), (640, 200), (0, 0, 255), 2)
                print("Line crossed")
            cv2.line(frame, (0, 200), (640, 200), (0, 255, 0), 2)
        

           # Display the frame
            cv2.imshow('Keypoints and Line Crossing', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()

    def release_camera(self):
        self.cap.release()


if __name__ == "__main__":
    camera_streamer = CameraStreamer()  
    camera_streamer.start_streaming()
    camera_streamer.release_camera()

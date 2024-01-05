import cv2
import time
from ultralytics import YOLO
<<<<<<< HEAD
#from Pose_detection import PoseDetectionModelLoader
=======
>>>>>>> 52f7293aaae04c5d8880a282099ff11a6ffcd89d

class CameraStreamer:
    def __init__(self, source=0):
        self.source = source
        self.cap = cv2.VideoCapture(source)   
        self.start_time = time.time()
        self.frame_count = 0
<<<<<<< HEAD
        self.model = YOLO('yolov8m.pt')
        #self.pose_loader=PoseDetectionModelLoader()
=======
        self.model=YOLO('yolov8m.pt')
>>>>>>> 52f7293aaae04c5d8880a282099ff11a6ffcd89d

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

<<<<<<< HEAD
            # Display the frame
            self.model(source=frame, show=True, conf=0.4, save=True)           
            ## self.pose_loader.detectPose(frame ,frame, draw=True, display=True) -> use for viewing keypoints
=======
            # Display the frame by running inference on the source
            results=self.model(source=frame, show=True, conf=0.4, save=True)
>>>>>>> 52f7293aaae04c5d8880a282099ff11a6ffcd89d

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

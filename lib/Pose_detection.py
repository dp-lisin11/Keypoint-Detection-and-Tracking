import cv2
import mediapipe as mp
import matplotlib.pyplot as plt


# Initialize mediapipe pose class.
mp_pose = mp.solutions.pose

# Setup the Pose function for videos - for video processing.
pose_video = mp_pose.Pose(static_image_mode=True, min_detection_confidence=0.7,
                          min_tracking_confidence=0.7)

# Initialize mediapipe drawing class - to draw the landmarks points.
mp_drawing = mp.solutions.drawing_utils
class PoseDetectionModelLoader:
    def __init__(self):
        self.mp_pose = mp_pose.Pose()
        self.results = None
        self.pose_video=pose_video
        
        
    def detectPose(self, frame,pose_video, draw=False, display=False):
        original_image = frame.copy()  
        image_in_RGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        resultant = self.pose_video.process(image_in_RGB)
        if resultant.pose_landmarks and draw:    
    
            mp_drawing.draw_landmarks(image=original_image, landmark_list=resultant.pose_landmarks,
                                  connections=mp_pose.POSE_CONNECTIONS,
                                  landmark_drawing_spec=mp_drawing.DrawingSpec(color=(255,255,255),
                                                                               thickness=3, circle_radius=3),
                                  connection_drawing_spec=mp_drawing.DrawingSpec(color=(49,125,237),
                                                                               thickness=2, circle_radius=2))

        if display:        
                plt.figure(figsize=[22,22])
                plt.subplot(121);plt.imshow(frame[:,:,::-1]);plt.title("Input Image");plt.axis('off');
                plt.subplot(122);plt.imshow(original_image[:,:,::-1]);plt.title("Pose detected Image");plt.axis('off');
        else:    
            return original_image
   
import cv2
import mediapipe as mp
import json

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

class KeypointDetectionModelLoader:
    def __init__(self):
        self.mp_pose = mp_pose.Pose()
        self.results = None

    def detect_keypoints(self, frame):
        # Convert the frame to RGB for Mediapipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run human body keypoint detection and tracking using MediaPipe
        self.results = self.mp_pose.process(rgb_frame)

        # Process keypoints and extract relevant information
        landmarks_info = []

        if self.results.pose_landmarks:
            for i, landmark in enumerate(self.results.pose_landmarks.landmark):
                landmarks_info.append({
                    "Landmark #{}".format(i): {
                        "x": landmark.x,
                        "y": landmark.y,
                        "z": landmark.z,
                        "visibility": landmark.visibility,
                        "presence": landmark.presence
                    }
                })

        return {"Landmarks": landmarks_info}



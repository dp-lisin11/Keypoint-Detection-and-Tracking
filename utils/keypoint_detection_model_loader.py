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
        print(landmarks_info)
        return {"Landmarks": landmarks_info}
    
    
    """
    This function returns True if a person has crossed the line, False otherwise.
    line_start and line_end: coordinates can be changed as per requirements
    """
    def has_crossed_line(self, frame, line_end, line_start):
    # Get the coordinates of the detected pose landmarks
        img=frame.copy()
        results = mp_pose.Pose(static_image_mode=True).process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        if results.pose_landmarks:
            landmarks = results.pose_landmarks.landmark
    
        else:
            print("No pose landmarks detected.")
            return False  # Or handle the case differently
        
    # Choose a suitable keypoint to track (foot)
        rfoot_x = int(landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].x * img.shape[1])
        rfoot_y = int(landmarks[mp_pose.PoseLandmark.RIGHT_FOOT_INDEX.value].y * img.shape[0])
        lfoot_x = int(landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x * img.shape[1])
        lfoot_y = int(landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y * img.shape[0])

    # Check if the foot is below the line and has crossed it horizontally
        if (rfoot_y > line_end[1] and rfoot_x > line_start[0] and rfoot_x < line_end[0]) or (lfoot_y > line_end[1] and lfoot_x > line_start[0] and lfoot_x < line_end[0]):
            return True
    
        return False
        


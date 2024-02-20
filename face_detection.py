import cv2
import mediapipe as mp
import numpy as np

mp_face_detection = mp.solutions.face_detection
mp_drawing = mp.solutions.drawing_utils

# Create a face detector instance with the video mode:
options = mp_face_detection.FaceDetectionOptions(
    min_detection_confidence=0.2)
with mp_face_detection.FaceDetection(min_detection_confidence=0.2) as detector:
    # Use OpenCV's VideoCapture to load the input video.
    cap = cv2.VideoCapture('res\vid\people-detection.mp4')

    # Load the frame rate of the video using OpenCV's CV_CAP_PROP_FPS
    fps = cap.get(cv2.CAP_PROP_FPS)

    while cap.isOpened():
        # Loop through each frame in the video using VideoCapture#read()
        ret, frame = cap.read()
        if not ret:
            break

        # Convert the frame received from OpenCV to a MediaPipe's Image object.
        mp_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(
            format=mp.ImageFormat.SRGB, 
            width=frame.shape[1], 
            height=frame.shape[0], 
            input_frame=mp_frame)

        # Run face detection
        results = detector.process(mp_image)

        # Print face detection results to the console
        if results.detections:
            for detection in results.detections:
                print(f"Detection confidence: {detection.confidence:.2f}")
                print(f"Bounding box: {detection.location_data.relative_bounding_box}")
                print("-------------------")

        # Display the frame with face detection annotations
        annotated_frame = frame.copy()
        if results.detections:
            for detection in results.detections:
                mp_drawing.draw_detection(annotated_frame, detection)

        cv2.imshow('Face Detection', annotated_frame)

        if cv2.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import numpy as np
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
import pyfirmata
D0=2
D1=3
D2=4
D3=5
port=input("enter port")
com="COM"+port
print(com)
board=pyfirmata.Arduino(com)
# Load the MediaPipe Pose model
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# url = 'http://192.168.29.17:8080/video'
# Open the webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    # Recolor the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Detect pose landmarks
    results = pose.process(frame_rgb)

    # Initialize counts for left, right, and front regions
    left_count, right_count, front_count = 0, 0, 0

    if results.pose_landmarks:
        # Extract pose landmarks
        landmarks = results.pose_landmarks.landmark

        # Get x-coordinate of each landmark
        for landmark in landmarks:
            landmark_x = int(landmark.x * frame.shape[1])

            # Check if the landmark is in the left region
            if landmark_x < frame.shape[1] / 3:
                left_count += 1
            # Check if the landmark is in the right region
            elif landmark_x > 2 * frame.shape[1] / 3:
                right_count += 1
            # Check if the landmark is in the front region
            else:
                front_count += 1

        # Determine the dominant region
        if left_count > right_count and left_count > front_count:
            orientation_text = "Left"
            board.digital[D0].write(1)
            board.digital[D1].write(0)
            board.digital[D2].write(0)
            board.digital[D3].write(1)

        elif right_count > left_count and right_count > front_count:
            orientation_text = "Right"
            board.digital[D0].write(0)
            board.digital[D1].write(1)
            board.digital[D2].write(1)
            board.digital[D3].write(0)
        else:
            orientation_text = "Front"
            board.digital[D0].write(1)
            board.digital[D1].write(0)
            board.digital[D2].write(1)
            board.digital[D3].write(0)

        # Display the orientation text
        cv2.putText(frame, orientation_text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    else:
        # If no pose is detected, display "Stop"
        cv2.putText(frame, "Stop", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        board.digital[D0].write(0)
        board.digital[D1].write(0)
        board.digital[D2].write(0)
        board.digital[D3].write(0)
    # Render the pose landmarks on the frame
    if results.pose_landmarks:
        mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Display the frame
    cv2.imshow('MediaPipe Feed', frame)
    black_bg = np.zeros_like(frame)
    cv2.imshow('Landmarks Only',black_bg)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
pose.close()
board.digital[D0].write(0)
board.digital[D1].write(0)
board.digital[D2].write(0)
board.digital[D3].write(0)
cap.release()
cv2.destroyAllWindows()

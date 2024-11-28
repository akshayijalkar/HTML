#Required libraries
import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands 
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Initialize webcam
video_capture = cv2.VideoCapture(0)

# Get screen size for scaling
screen_width, screen_height = pyautogui.size()

# Variables to track hand position for gestures
prev_x, prev_y = 0, 0
gesture_state = None  # Track current gesture (None, open hand, fist)
last_move_time = time.time()

# Threshold for minimal movement to register
movement_threshold = 30  # Increase the movement threshold to ignore small fluctuations

# Zoom gesture variables
thumb_index_distance_prev = 0  # Previous distance between thumb and index finger
zoom_threshold = 50  # Adjust this threshold based on your hand size

# Fire gesture state
is_fist = False

# Function to check if the hand is in a fist position
def is_fist(landmarks):
    # Check if all the fingers are curled in (i.e., forming a fist)
    thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Check if the fingers are curled by comparing the tip positions with their bases
    if (index_tip.y > landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y and
        middle_tip.y > landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y and
        ring_tip.y > landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y and
        pinky_tip.y > landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y and
        thumb_tip.y > landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y):
        return True
    return False

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Flip the frame horizontally for a better mirror effect
    frame = cv2.flip(frame, 1)

    # Convert to RGB (MediaPipe requires RGB input)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect hands
    results = hands.process(rgb_frame)

    # Convert back to BGR for OpenCV
    frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            # Draw hand landmarks
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            # Get coordinates of the thumb and index finger tips (Landmarks 4 and 8)
            thumb_tip = landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_finger_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

            # Get the coordinates of thumb and index finger tips
            thumb_x, thumb_y = int(thumb_tip.x * frame.shape[1]), int(thumb_tip.y * frame.shape[0])
            index_x, index_y = int(index_finger_tip.x * frame.shape[1]), int(index_finger_tip.y * frame.shape[0])

            # Calculate the distance between the thumb and index finger tips for zoom
            thumb_index_distance = np.sqrt((thumb_x - index_x)**2 + (thumb_y - index_y)**2)

            # Zoom in or out based on the thumb and index distance change
            if thumb_index_distance > thumb_index_distance_prev + zoom_threshold:
                pyautogui.scroll(10)  # Zoom in (scroll up)
            elif thumb_index_distance < thumb_index_distance_prev - zoom_threshold:
                pyautogui.scroll(-10)  # Zoom out (scroll down)

            thumb_index_distance_prev = thumb_index_distance  # Update the previous distance

            # Fire gesture detection (check if the hand is in a fist position)
            if is_fist(landmarks):
                if not is_fist:  # Only trigger the action once per fist detection
                    print("Fist detected! Firing action...")
                    pyautogui.click()  # Simulate a click action (firing action)
                    is_fist = True
            else:
                is_fist = False

            # Get coordinates of the tip of the index finger (Landmark 8)
            wrist = landmarks.landmark[mp_hands.HandLandmark.WRIST]
            wrist_x, wrist_y = int(wrist.x * frame.shape[1]), int(wrist.y * frame.shape[0])

            # Calculate movement (for smooth mouse control)
            screen_x = np.interp(index_x, [0, frame.shape[1]], [0, screen_width])
            screen_y = np.interp(index_y, [0, frame.shape[0]], [0, screen_height])

            # Calculate the movement distance
            movement_distance = np.sqrt((screen_x - prev_x)**2 + (screen_y - prev_y)**2)

            # Only update the mouse position if the movement exceeds the threshold
            if movement_distance > movement_threshold:
                pyautogui.moveTo(screen_x, screen_y)

            # Control the frequency rate (only update mouse every 0.1 seconds)
            current_time = time.time()
            if current_time - last_move_time > 0.1:  # Limit to 10 updates per second
                prev_x, prev_y = screen_x, screen_y
                last_move_time = current_time

            # Update previous hand position for smooth scrolling
            prev_x, prev_y = wrist_x, wrist_y

    # Show the frame with landmarks
    cv2.imshow("Hand Gesture Mouse Control", frame)

    # Exit on pressing 'ESC'
    if cv2.waitKey(1) & 0xFF == 27:  # ESC key to exit
        break

# Release and close the webcam
video_capture.release()
cv2.destroyAllWindows()

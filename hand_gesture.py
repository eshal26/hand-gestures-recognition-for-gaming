import cv2
import numpy as np
import mediapipe as mp
import pyautogui

# Initialize Mediapipe Hand module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Function to map hand landmarks to gestures
def get_gesture(hand_landmarks):
    thumb_is_open = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].x
    index_is_open = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_DIP].y
    middle_is_open = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_DIP].y
    ring_is_open = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_DIP].y
    pinky_is_open = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP].y < hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_DIP].y

    fingers_open = [thumb_is_open, index_is_open, middle_is_open, ring_is_open, pinky_is_open]

    if all(fingers_open):
        return 'open_hand'
    elif not any(fingers_open):
        return 'closed_fist'
    elif fingers_open.count(True) == 1:
        return 'left'
    elif fingers_open.count(True) == 2:
        return 'right'
    else:
        return 'unknown'

def control_game(gesture):
    if gesture == 'left':
        pyautogui.press('left')
        print("Left gesture detected")
    elif gesture == 'right':
        pyautogui.press('right')
        print("Right gesture detected")
    elif gesture == 'open_hand':
        pyautogui.press('up')
        print("Open hand detected")
    elif gesture == 'closed_fist':
        pyautogui.press('down')
        print("Closed fist detected")
    else:
        print("Unknown gesture detected")
          
def main():
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
        while True:         
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            result = hands.process(frame_rgb)

            if result.multi_hand_landmarks:
                for hand_landmarks in result.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                    gesture = get_gesture(hand_landmarks)
                    control_game(gesture)

            cv2.imshow('Hand Gesture Control', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
         
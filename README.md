# Hand Gesture Control for PC Games

This project allows you to control a PC game using hand gestures detected via a webcam. The hand gestures are recognized using Mediapipe, a library for efficient and accurate hand tracking, and the corresponding game actions are performed using the `pyautogui` library.

## Features
- **Hand Detection**: Uses Mediapipe to detect and track hand landmarks in real-time.
- **Gesture Recognition**: Recognizes specific hand gestures (open hand, closed fist, and finger counts) and maps them to game controls.
- **Game Control**: Simulates key presses (left, right, space, and up) to control the game based on recognized gestures.

## Requirements
- Python 
- OpenCV
- Mediapipe
- PyAutoGUI
- NumPy

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/eshal26/hand-gestures-recognition-for-gaming.git
    cd hand-gesture-recongnition-for-gaming
    ```

2. Install the required packages:
    ```sh
    pip install opencv-python mediapipe pyautogui numpy
    ```

## Usage
1. Run the script:
    ```sh
    python hand_gesture.py
    ```

2. Ensure your webcam is connected and working.

3. Use the following gestures to control the game:
    - **Open Hand**: Simulates the 'space' key (e.g., jump).
    - **Closed Fist**: Simulates the 'up' key (e.g., move up).
    - **One Finger**: Simulates the 'left' key (e.g., move left).
    - **Two Fingers**: Simulates the 'right' key (e.g., move right).

4. Press 'q' to quit the application.


## Acknowledgments
- [Mediapipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)

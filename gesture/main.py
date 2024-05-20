# just run the program and use it 
# add more functionalites according to your need
import cv2
import mediapipe as mp
import pyautogui

gesture_recognition_active = True  # Set the initial value
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

def process_frame(frame, hands, prev_x, prev_y):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for landmarks in results.multi_hand_landmarks:
            handedness = results.multi_handedness[results.multi_hand_landmarks.index(landmarks)].classification[0].label
            mp_drawing.draw_landmarks(frame, landmarks, mp_hands.HAND_CONNECTIONS)

            index_tip = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            index_mid = landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP]

            if handedness == "Left":
                mcp_x = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].x
                mcp_y = landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_MCP].y

                cursor_x = int(mcp_x * screen_width)
                cursor_y = int(mcp_y * screen_height)

                pyautogui.moveTo(cursor_x, cursor_y, duration=0.01)

                if index_tip.y >= index_mid.y:
                    pyautogui.click()

            elif handedness == "Right":
                x, y = int(index_tip.x * screen_width), int(index_tip.y * screen_height)
                if prev_x is not None and prev_y is not None:
                    dx = x - prev_x
                    dy = y - prev_y

                    if abs(dx) > abs(dy):
                        if dx > 50:
                            pyautogui.press('right')
                        elif dx < -50:
                            pyautogui.press('left')
                    else:
                        if dy > 50:
                            pyautogui.press('down')
                        elif dy < -50:
                            pyautogui.press('up')

                prev_x = x
                prev_y = y

    return frame, prev_x, prev_y

def start_gesture_recognition():
    global gesture_recognition_active
    prev_x, prev_y = None, None

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    with mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7) as hands:

        while gesture_recognition_active:
            ret, frame = cap.read()
            if not ret:
                print("Error: Failed to capture image.")
                break

            frame = cv2.flip(frame, 1)
            frame, prev_x, prev_y = process_frame(frame, hands, prev_x, prev_y)
            cv2.imshow("Gesture Recognition", frame)

            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_gesture_recognition()

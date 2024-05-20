<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <header>
        <h1>Gesture Recognition Program</h1>
    </header>
    <div class="container">
        <section>
            <h2>Features</h2>
            <ul>
                <li>Real-time Gesture Recognition: Uses your webcam to track hand movements.</li>
                <li>Mouse Control: Move the cursor and perform clicks with hand gestures.</li>
                <li>Keyboard Control: Simulate arrow key presses based on hand movements.</li>
            </ul>
        </section>
        <section>
            <h2>How It Works</h2>
            <ol>
                <li><strong>Capture Video:</strong> The program captures video frames from your webcam.</li>
                <li><strong>Process Frames:</strong> Each frame is processed to detect hand landmarks using MediaPipe.</li>
                <li><strong>Gesture Interpretation:</strong>
                    <ul>
                        <li><strong>Left Hand:</strong>
                            <ul>
                                <li>Move the cursor by moving the middle finger's MCP joint.</li>
                                <li>Click by tapping with the index finger.</li>
                            </ul>
                        </li>
                        <li><strong>Right Hand:</strong>
                            <ul>
                                <li>Simulate arrow key presses based on the direction of the index finger's movement.</li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li><strong>Perform Actions:</strong> Cursor movements, clicks, and key presses are simulated using PyAutoGUI.</li>
            </ol>
        </section>
        <section>
            <h2>Prerequisites</h2>
            <p>Ensure you have the following libraries installed:</p>
            <pre><code>pip install opencv-python mediapipe pyautogui</code></pre>
        </section>
        <section>
            <h2>Usage</h2>
            <p>To start the gesture recognition program, simply run the Python script:</p>
            <pre><code>python gesture_recognition.py</code></pre>
        </section>
        <section class="commands">
            <h3>Stopping the Program</h3>
            <p>To stop the program, press the <code>q</code> key.</p>
        </section>
        <section>
            <h2>Code Explanation</h2>
            <h3>Main Function</h3>
            <p>The main function <code>start_gesture_recognition()</code> initializes the webcam and starts the gesture recognition loop.</p>
            <pre><code>if __name__ == "__main__":
    start_gesture_recognition()</code></pre>
            <h3>Processing Frames</h3>
            <p>The <code>process_frame()</code> function processes each video frame to detect hand landmarks and interpret gestures.</p>
            <pre><code>def process_frame(frame, hands, prev_x, prev_y):
    # Process the frame to detect hand landmarks and interpret gestures
    ...</code></pre>
            <h3>Gesture Interpretation</h3>
            <p>Depending on the detected hand (left or right), gestures are interpreted to perform actions:</p>
            <ul>
                <li><strong>Left Hand:</strong>
                    <ul>
                        <li>Move the cursor by moving the middle finger's MCP joint.</li>
                        <li>Click by tapping with the index finger.</li>
                    </ul>
                </li>
                <li><strong>Right Hand:</strong>
                    <ul>
                        <li>Simulate arrow key presses based on the direction of the index finger's movement.</li>
                    </ul>
                </li>
            </ul>
        </section>
    </div>
    <footer>
        <p>&copy; 2024 Gesture Recognition Program</p>
    </footer>
</body>
</html>

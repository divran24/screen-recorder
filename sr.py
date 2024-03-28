import pyautogui
import cv2
import numpy as np
import time

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*'XVID') 
filename = "recording.avi"
fps = 60.0
out = cv2.VideoWriter(filename, codec, fps, resolution)

cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

prev_time = time.time()  # Store the previous time

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow('Live', frame)
    
    # Check for key press
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:  # 'q' or 'Esc' key
        break

    # Delay to maintain desired frame rate
    current_time = time.time()
    elapsed_time = current_time - prev_time
    delay = max(1.0 / fps - elapsed_time, 0)
    time.sleep(delay)
    prev_time = current_time

out.release()
cv2.destroyAllWindows()

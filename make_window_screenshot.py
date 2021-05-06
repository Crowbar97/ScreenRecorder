import time

import cv2
import numpy as np
import pyautogui
import mss

from utils import exec_shell_cmd, get_window_geometry, bring2front


# script for debugging
def make_window_screenshot(window_name, output_file_path='screenshot.png'):
    # Step 1: getting geometry of the target window
    window_id, left, top, width, height = get_window_geometry(window_name)

    # Step 2: bringing target window to the front
    # NOTE: this may take some time after the system call
    bring2front(window_id)
    # time.sleep(1)

    # Step 3: making screenshot the target window
    # by it's position and dimensions
    # The screen part to capture
    # NOTE: in case of repeating screenshots
    # this context need to create out of loop
    # for better performance!
    with mss.mss() as sct:
        region = {'top': int(top), 'left': int(left), 'width': int(width), 'height': int(height)}
        # region = {'top': 0, 'left': 0, 'width': 300, 'height': 300}
        print(region)
        # Grab the data
        img = sct.grab(region)

    frame = np.array(img)
    cv2.imwrite(output_file_path, frame)


if __name__ == '__main__':
    make_window_screenshot(window_name='Home')
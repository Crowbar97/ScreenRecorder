### Screen recorder
This repository contains useful scripts for making video records of the screen areas or specific windows

### Installation
```bash
# creating environment
conda create --name screen-recorder python=3.6
conda activate screen-recorder

# installing dependencies
pip install opencv-python
conda install -c conda-forge pyautogui
```

### Navigation
- `make_window_screenshot.py` -- script for testing your system by making test screenshot of the specific window
- `record_frame.py` -- for recording specified screen frame
- `record_window.py` -- for recording specified window
- `utils.py` -- script with aux methods


### How it works
Target window video recording algorithm:
- scince we can record only specific rectangle on our screen, first we obtain target window position and it's width and height for defining this rectangle
- next we define condition for stopping video recording, in our case we will record target window until it exist
- video recording implemented as cycle, where on each iteration we perform next steps:
    - checking target window exist
    - bringing target window to the front to make sure it isn't overlapped by other windows
    - making screenshot
- lastly we compile all screenshots in a video file

bring window to the front (if not), and get screenshot
size and position of the target window is calculated only in first time

problem: frequent bringing window to front may interferes with your work on computer

### Current problems to solve:
- very slow screenshot rate? Need to find library for getting screenshots faster than pyautogui?
- currently need to manually specify configuration for each running system
- sometimes pyautogui don't remove hidden screenshot temporary files

### Complementary
Other Linux utilities that may be helpful:
- xdotool
- xwininfo
- xprop
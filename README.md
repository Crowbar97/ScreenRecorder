### Screen recorder
This repository contains useful scripts for making video records of the screen areas or specific windows

### Installation
```bash
# creating environment
conda create --name screen-recorder python=3.6
conda activate screen-recorder

# installing dependencies
pip install opencv-python
```

### Navigation
- `window_recorder.py` -- the only script you need for target window video recording
- `frames2video.py` -- for compiling video from collected screenshots manually
- `utils.py` -- script with aux methods
- the rest scripts are **deprecated**


### How it works
Under the hood `window_recorder.py` uses system calls of the `import` utility to have ability of making screenshots of any open windows, _even overlapped_ by another windows.


### Upcoming tasks:
- try to speed up current implementation for better FPS


### Complementary
Linux utilities that may be helpful:
- wmctrl
- import
- xwd
- xdotool
- xwininfo
- xprop
- OBS
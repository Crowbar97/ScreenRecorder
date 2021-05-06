import mss
import mss.tools


with mss.mss() as sct:
    # The screen part to capture
    region = {'top': 0, 'left': 0, 'width': 400, 'height': 300}

    # Grab the data
    img = sct.grab(region)

    # Save to the picture file
    mss.tools.to_png(img.rgb, img.size, output='dummy.png')
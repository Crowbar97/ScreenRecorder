import win32gui
import win32ui
from ctypes import windll
from PIL import Image

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible( hwnd ):
        print (hex(hwnd), win32gui.GetWindowText( hwnd ))

win32gui.EnumWindows( winEnumHandler, None )

# NOTE: need exact window name
hwnd = win32gui.FindWindow(None, 'File Explorer')

# Change the line below depending on whether you want the whole window
# or just the client area. 
left, top, right, bot = win32gui.GetClientRect(hwnd)
# left, top, right, bot = win32gui.GetWindowRect(hwnd)

# NOTE: seems like win32 libs are set to use
# Full HD 1920 * 1080 monitor resolution,
# so if you using 4K 3840 * 2160 then you
# need to scale w and h values:
w_scale = 3840 // 1920
h_scale = 2160 // 1080
w = (right - left) * w_scale
h = (bot - top) * h_scale

hwndDC = win32gui.GetWindowDC(hwnd)
mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
saveDC = mfcDC.CreateCompatibleDC()

saveBitMap = win32ui.CreateBitmap()
saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

saveDC.SelectObject(saveBitMap)

# Change the line below depending on whether you want the whole window
# or just the client area. 
result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
# result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 0)
print(result)

bmpinfo = saveBitMap.GetInfo()
bmpstr = saveBitMap.GetBitmapBits(True)

print(bmpinfo)
print(type(bmpstr))

im = Image.frombuffer(
    'RGB',
    (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
    bmpstr, 'raw', 'BGRX', 0, 1)

win32gui.DeleteObject(saveBitMap.GetHandle())
saveDC.DeleteDC()
mfcDC.DeleteDC()
win32gui.ReleaseDC(hwnd, hwndDC)

if result == 1:
    #PrintWindow Succeeded
    im.save("test.png")
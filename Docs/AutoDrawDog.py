#! python
import time, pyautogui
time.sleep(5)

try :
    for i in range(30, 620, 4):
        for j in range(80, 650, 4):
            # Recognition color
            pixelColor = pyautogui.screenshot().getpixel((i, j))
            if pixelColor != (255, 255, 255):
                pyautogui.click(i+700, j) 
                pyautogui.dragTo(i+700+10, j+10) 
except KeyboardInterrupt:
    print('\nDone.')
    
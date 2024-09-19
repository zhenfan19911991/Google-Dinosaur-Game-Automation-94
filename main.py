import time
import pyautogui
import cv2
from PIL import ImageGrab, Image
from mss import mss
import numpy as np

# img = pyautogui.screenshot(region = (1060, 30, 60, 60))
# img.save('sc1.png')
# img.save('sc2.png')

pyautogui.PAUSE = 0
pyautogui.MINIMUM_DURATION = 0
pyautogui.MINIMUM_SLEEP = 0

try:
    region = pyautogui.locateOnScreen('sc2.png', confidence=0.9)
except pyautogui.ImageNotFoundException:
    try:
        region = pyautogui.locateOnScreen('sc1.png', confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print('Could not find the game screen')


topRightX = region[0] + region[2]+10 # left + width
topRightY = region[1] # top
game_region = (topRightX-1130, topRightY, 1130, 830) # the game screen is always 640 x 480

low_block_location = (300+game_region[0], game_region[1]+536)
#low_block_region = (low_block_location[0], low_block_location[1], low_block_location[0]+2, low_block_location[1]+2 )
# cap = ImageGrab.grab(bbox=low_block_region)
# cap.show()
# cap.getpixel((1,1))

high_block_location = (280+game_region[0], game_region[1]+463)
#high_block_region = (high_block_location[0], high_block_location[1],high_block_location[0]+2, high_block_location[1]+2)


close_block_location = (481+game_region[0], game_region[1]+384)
#close_block_region = (close_block_location[0], close_block_location[1], close_block_location[0]+2, close_block_location[1]+2)


pyautogui.moveTo(game_region[0]+574,game_region[1]+330)
pyautogui.click()
pyautogui.press('up')
game_on = True

def capture_screenshot(block_location):
    with mss() as sct:
        monitor = {
            "top": block_location[1],  # Top coordinate
            "left": block_location[0],  # Left coordinate
            "width": 2,  # Width of the area
            "height": 2  # Height of the area
        }
        sct_img = sct.grab(monitor)
        # Convert to PIL/Pillow Image
        return int(np.array(sct_img)[0, 0, 0])


while game_on:
    if capture_screenshot(low_block_location) == 73:
        pyautogui.keyDown('up')
    if capture_screenshot(high_block_location) == 73:
        pyautogui.keyDown('up')
    if capture_screenshot(close_block_location) == 73:
        game_on = False



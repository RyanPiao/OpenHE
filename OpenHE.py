import cv2 as cv
import mediapipe as mp
import numpy as np
import os
import time
from windowcapture import WindowCapture
import HandTrackingModule as htm

## Get windowCapture Name
# WindowCapture.list_window_names()
# exit()

# WindowCapture Loop
#loop_time = time()
pTime = 0
cTime = 0
detector = htm.handDetector()

# initialize the WindowCapture class
wincap = WindowCapture('BONEWORKS')
while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    img = detector.findHands(screenshot, draw=True )
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    
    cv.imshow("Computer Vision", img)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

    
print('Done.')
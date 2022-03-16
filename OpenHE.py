import cv2 as cv
import mediapipe as mp
import numpy as np
import os
import time
from windowcapture import WindowCapture
import HandTrackingModule

## Get windowCapture Name
# WindowCapture.list_window_names()
# exit()

# WindowCapture Loop
pTime = 0
cTime = 0

# initialize the WindowCapture and HandTrackingModule class
detector = HandTrackingModule.handDetector()
wincap = WindowCapture('BONEWORKS')


while(True):
    # get an updated image of the game
    screenshot = wincap.get_screenshot()
    img = detector.findHands(screenshot, draw=True )
    #Get FPS
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[4])
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    #Display FPS
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)
    #Quit the capture window
    cv.imshow("Game Capture", img)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
print('Done.')
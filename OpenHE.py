import cv2 as cv
import mediapipe as mp
import numpy as np
import os
import time
import HandTrackingModule
from windowcapture import WindowCapture
from pywinauto import Desktop
import math

## Let user select the active VR game window.
# Get name for all active windows
opened_windows = Desktop(backend="uia").windows()
captured_window_names= [w.window_text() for w in opened_windows]
# Let user pick the game window.
window_name_index=WindowCapture.let_user_pick(captured_window_names)
game_window_name = captured_window_names[window_name_index]
print('Selected Game window: ' + game_window_name)

## For WindowCapture Loop - initial values
pTime = 0
cTime = 0

## Initialize the WindowCapture and HandTrackingModule class
detector = HandTrackingModule.handDetector()
wincap = WindowCapture(game_window_name)

while(True):
    ## get an updated image of the game
    screenshot = wincap.get_screenshot()
    img = detector.findHands(screenshot, draw=True )

    ## Get Hand Landmark and cricial points.
    lmList = detector.findPosition(img, draw=False)
    
    if len(lmList) != 0:
        t1_1, t1_2, t1_3 = lmList[4][1], lmList[4][2], lmList[4][3]
        t2_1, t2_2, t2_3 = lmList[2][1], lmList[2][2], lmList[2][3]
        # Index Finger
        i1_1, i1_2, i1_3 = lmList[8][1], lmList[8][2], lmList[8][3]
        i2_1, i2_2, i2_3 = lmList[5][1], lmList[5][2], lmList[5][3]       
        # Middle Finger
        m1_1, m1_2, m1_3 = lmList[12][1], lmList[12][2], lmList[12][3]
        m2_1, m2_2, m2_3 = lmList[9][1], lmList[9][2], lmList[9][3]
        # Ring Finger
        r1_1, r1_2, r1_3 = lmList[16][1], lmList[16][2], lmList[16][3]
        r2_1, r2_2, r2_3 = lmList[13][1], lmList[13][2], lmList[13][3]
        # Pinky
        p1_1, p1_2, p1_3 = lmList[20][1], lmList[20][2], lmList[20][3]
        p2_1, p2_2, p2_3 = lmList[17][1], lmList[17][2], lmList[17][3]

        t_len = math.hypot(t2_1-t1_1,t2_2-t1_2)
        i_len = math.hypot(i2_1-i1_1,i2_2-i1_2)
        m_len = math.hypot(m2_1-m1_1,m2_2-m1_2)
        r_len = math.hypot(r2_1-r1_1,r2_2-r1_2)
        p_len = math.hypot(p2_1-p1_1,p2_2-p1_2)
        print(t_len,i_len,m_len,r_len,p_len)

    ## Calculate FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    
    ## Display FPS on captured window
    cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3)

    ## Quit the capture window
    cv.imshow("Game Capture", img)
    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
print('Done.')
import cv2 as cv
import time
import HandTrackingModule
from windowcapture import WindowCapture
from pywinauto import Desktop

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

    #Test Print the finger id, finger angle, side of hand.
    if len(lmList) != 0:
        print(lmList)

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
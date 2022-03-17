import cv2 as cv
import mediapipe as mp
import time
import numpy as np

# class creation
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5,modelComplexity=1,trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.modelComplex = modelComplexity
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands,self.modelComplex,
                                        self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils # it gives small dots onhands total 20 landmark points

    def findHands(self,img,draw=True):
        # Send rgb image to hands
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB) # process the frame
    #     print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:

                if draw:
                    #Draw dots and connect them
                    self.mpDraw.draw_landmarks(img,handLms,
                                                self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self,img, draw=True):
        """Lists the position/type of hand, and finger angles."""
        lmlist = []
        joint_list = [[4,3,1], [8,7,5], [12,11,9], [16,15,13], [20,19,17]]
        # check wether any landmark was detected
        if self.results.multi_hand_landmarks:
            #Which hand are we talking about
            for idx, classification in enumerate(self.results.multi_handedness):
                # Left hand or Right hand, that is quesion.
                # Index=0 -> Left | Index=1 -> Right
                index = classification.classification[0].index
            for num, hand in enumerate(self.results.multi_hand_landmarks):
                #Loop through joint sets 
                for joint in joint_list:
                    a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y]) # First coord
                    b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y]) # Second coord
                    c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y]) # Third coord
                    radians = np.arctan2(c[1] - b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
                    angle = np.abs(radians*180.0/np.pi)
                    if angle > 180.0:
                        angle = 360-angle
                    # Get finger id, finger angle, side of hand.
                    lmlist.append([num,angle,index])
        return lmlist

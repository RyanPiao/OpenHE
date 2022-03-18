import cv2 as cv
import mediapipe as mp
import time
import numpy as np
import random

# class creation
class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.8,modelComplexity=1,trackCon=0.5):
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
        """Lists the position/type of landmarks
        we give in the list and in the list ww have stored
        type and position of the landmarks.
        List has all the lm position"""
        lmlist = []
        joint_list = [[4,3,2], [8,7,5], [12,10,9], [16,14,13], [20,18,17]]
        # check wether any landmark was detected
        if self.results.multi_hand_landmarks:
            #Which hand are we talking about
            for idx, classification in enumerate(self.results.multi_handedness):
                # Left hand or Right hand, that is quesion.
                # Index=0 -> Left | Index=1 -> Right
                index = classification.classification[0].index
            for num, hand in enumerate(self.results.multi_hand_landmarks):
                w = np.array([hand.landmark[0].x, hand.landmark[0].y, hand.landmark[0].z]) # wrist coord
                # Check if there is previous wrist coord exist, if not set current one to previous one.
                if not('wp' in globals()): 
                    global wp
                    wp = w
                else:
                    change_in_w = np.divide(np.subtract(w,wp),wp) # Percentage change wrist coord.
                    wp = w # update new wrist coord to previous coord.

                    # If change in wrist coord is greater than a certain threshold, next action will be taken. 
                    if (change_in_w>[0.001,0.001,0.001]).all():
                        print(change_in_w)
                        #Loop through joint sets 
                        # for joint in joint_list:
                        #     a = np.array([hand.landmark[joint[0]].x, hand.landmark[joint[0]].y, hand.landmark[joint[0]].z]) # First coord
                        #     b = np.array([hand.landmark[joint[1]].x, hand.landmark[joint[1]].y, hand.landmark[joint[1]].z]) # Second coord
                        #     c = np.array([hand.landmark[joint[2]].x, hand.landmark[joint[2]].y, hand.landmark[joint[2]].z]) # Third coord
                        #     # Calculate angle between three points using their 3D coordinates
                        #     ba = a - b
                        #     bc = c - b
                        #     cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                        #     angle = np.arccos(cosine_angle)
                        #     # Put figer id, calculated angle, and side of hand into a list.
                        #     lmlist.append([num,angle,index])
        return lmlist

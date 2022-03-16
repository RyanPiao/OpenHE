# OpenHE
This is Open**H**aptic**E**ngine, OpenHE is a universal haptic(Grip) feedback build for OpenGloveDriver. OpenHE is able to reconize in-game characters' hand by utilize opencv and mediapipe, use the captured hand data to track postion of fingers in real time. With OpenGloveDriver and hardware, OpenHE is able to send back calculated figure postion and stop stepper motor in the right postion to mimic Grip feedback. 

**Update0**

1.  It is capable to track postion of fingers from webcam in real time, and use hand guesture to control system volumn. (See my other repo for examples.)
2.  Successfully capture video stream from VR games.

![Update0](https://github.com/RyanPiao/WindowCapture/blob/main/screenshots/WindowCapture.png)

**Update1**
Successfully capture in-game characters' hand from Boneworks.
![Update1](https://github.com/RyanPiao/WindowCapture/blob/main/screenshots/in-game-hand-tranking.png)

**What is next?**
Base on mediapipe hand landmark model, get critical points from hand poses. Then use that data to calculate app appropriate location for stepper motor to stop. I will explain in detials why I this apporach in future update. 

![Hand Landmark Model](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png) \

 The basic idea:
 1. I will get two end points from each finger, calculate the distance between those end points, let's call it endpointrange. 
    - For example, I will take distance from 2 and 4 for the thumb(see figure above).
 3. When the value of endpointrange not change anymore in the game, in reality, the glove's stepper motor will stop right there. 
 4. Therefore, your finger could not move future. This will creat a Grip feedback. 
 5. In the future update, I will also include  some predition where and how the hand move to improve the Grip feedback. 

# OpenHE
This is Open**H**aptic**E**ngine, OpenHE is a universal haptic(Force) feedback build for OpenGloveDriver. OpenHE is able to recognize in-game characters' hands by utilizing OpenCV and mediapipe, using the captured hand data to track positions of fingers in real-time. With OpenGloveDriver and hardware, OpenHE is able to send back the calculated figure position and stop the stepper motor in the right postion to mimic force feedback. 

**Update0**

1.  It is capable to track positions of fingers from the webcam in real-time, and using hand gestures to control the system volume. (See my other repo for examples.)
2.  Successfully capture video stream from VR games.

![Update0](https://github.com/RyanPiao/WindowCapture/blob/main/screenshots/WindowCapture.png)

**Update1**
Successfully captured in-game characters' hands from Boneworks.
![Update1](https://github.com/RyanPiao/WindowCapture/blob/main/screenshots/in-game-hand-tranking.png)

**What is next?**
Based on mediapipe hand landmark model, get critical points from hand poses. Then use that data to calculate app appropriate location for the stepper motor to stop. I will explain in details why I this approach in future updates. 

![Hand Landmark Model](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png) 

The basic idea:
1. I will get two endpoints from each finger, calculate the distance between those endpoints, let's call it endpoint_range. The endpoint_range is constantly tracked.
 - For example, I will take distance from 2 and 4 for the thumb(see figure above).
2. When the value of endpoint_range does not change anymore in the game (or hit a threshold), in reality, the glove's stepper motor will stop right there. Therefore, your finger could not move future. This will create threshold force feedback. 
3. Send force feedback via a Named Pipe to the driver. 
4. Even futher,I can use a classifier to predict the hand pose. It keeps track of the previous predictions and then predicts the finger position to be the most common pose in the pass. It will reduce latency.

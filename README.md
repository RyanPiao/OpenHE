# OpenHE
This is Open**H**aptic**E**ngine, OpenHE is a universal haptic(Force) feedback build for OpenGloveDriver. OpenHE is able to recognize in-game characters' hands by utilizing OpenCV and mediapipe, using the captured hand data to track positions of fingers in real-time. With OpenGloveDriver and Lucidglove hardware, OpenHE is able to send back the calculated finger position and stop the stepper motor in the right postion to mimic force feedback. 

# What is OpenGloveDriver and Lucidglove?
A SteamVR (OpenVR) driver for VR Gloves and DIY Hardware. 

- **About the OpenGloveDriver: [OpenGloveDriver](https://github.com/LucidVR/opengloves-driver).** 

- **About the LucidGloves: [LucidGloves](https://github.com/LucidVR/lucidgloves).** 

# Update 0

1.  It is capable to track positions of fingers from the webcam in real-time, and using hand gestures to control the system volume. (See my other repo for examples.)
2.  Successfully capture video stream from VR games.

![Update0](https://github.com/RyanPiao/WindowCapture/blob/main/screenshots/WindowCapture.png)

# Update 1
Successfully captured landmarks from in-game characters' hands, this is screenshot from Boneworks.
![Update1](https://github.com/RyanPiao/WindowCapture/blob/main/screenshots/in-game-hand-tranking.png)

**What is next?**
Based on mediapipe hand landmark model, get critical points from hand poses. Then use that data to calculate app appropriate location for the stepper motor to stop. I will explain in details why I this approach in future updates. 

![Hand Landmark Model](https://google.github.io/mediapipe/images/mobile/hand_landmarks.png) 

The basic idea:
1. I will get two endpoints from each finger, calculate the distance between those endpoints, let's call it endpoint_range. The endpoint_range is constantly tracked.
 - For example, I will take distance from 2 and 4 for the thumb(see figure above).
2. When the value of endpoint_range does not change anymore in the game (or hit a threshold), in reality, the glove's stepper motor will stop right there. Therefore, your finger could not move future. This will mimic force feedback. 
3. Send force feedback via a Named Pipe to the OpenGloveDriver. 
 - **pygloves can be used here: [pygloves](https://github.com/PerlinWarp/pygloves).** 
4. Even futher,I can use a classifier to predict the hand pose. It keeps track of the previous predictions and then predicts the finger position to be the most common pose in the pass. Hopefully, It will reduce latency.

# Update 2
- scucessfully track and calculated all endpoint_range for left hand.\
![demo](https://github.com/RyanPiao/OpenHE/blob/main/screenshots/handtrankingdemo.gif)
- It might be too blur to see the small text from the gif. :( 
- It is basically when my in-game characters close fingers, the endpoint_range will gets smaller. 
- When my in-game characters hold on to something, the characters' hand will stop closing. 
- Based on that, I can figure out where is the point the stepper motor should stop. 
- I can send back that information to OpenGloveDriver to stop the stepper motor in the right place.

### Part A
### Play with different sense-making algorithms.

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Contour: contour is very similar to the edge detection in computer vision, and it essentially sketch the contour of the image. One potential application might be painting tutorial/assistant. The software can break down the painting process into 2 steps: first it assist the painting of the contour, then it assist the painting of the entire image.

![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%205/screen_shots/contour.png)

Face Detection: back to my design in lab1, where people waiting for the elevator will be alerted if someone is getting out of the elevator at the current floor (https://github.com/xuqianzhi/Interactive-Lab-Hub/tree/Fall2021/Lab%201). Face detection can be very well applied in this design as a sensing algorithm to detect whether someone is in the elevator or not.

![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%205/screen_shots/face-detection.png)

Object Detection: since object detection is capable of counting the number of objects in a image, it can be very useful in any kind of autonomous motion to avoid collision.

![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%205/screen_shots/object-detect.png)

Optical Flow: optical flow is very useful for motion detection, and it can be used in a security camera to monitor certain things. For example, some algorithm can be implemented to detect whether there is a possibility that your dog has escaped from the house by checking the last time a motion exist in the scene.

![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%205/screen_shots/optical-flow.png)


#### MediaPipe

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***

Screenshots:
![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%205/screen_shots/hand_tracking.png)

The hand/body detection can be used in Virtual Reality/Augmented Reality interaction in general, for example your hand that are being tracked can be used to pickup and move a virtual apple.


#### Teachable Machines

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***

ScreenShot:
![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%205/screen_shots/teachable_machine.png)

The nice thing about teachable machine is that you can train it to identify customizable things. This way you can train it to identify many different things, such as a water bottle, a speaker, etc.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

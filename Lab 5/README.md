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

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***

Pan detector: a detector to detect the existance of a pan on the stove, and make decision on turning on/off the hood, light, etc.

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do?
1. When does it fail?
1. When it fails, why does it fail?
1. Based on the behavior you have seen, what other scenarios could cause problems?

If you train the model to recognize a sauce pan, then when you put a wok/dutch oven on the stove, the model fail to recognize that as a pan

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system?
1. How bad would they be impacted by a miss classification?
1. How could change your interactive system to address this?
1. Are there optimizations you can try to do on your sense-making algorithm.

The user of the system should not be aware of the uncertainty of the system, and it should walk toward the kitchen with confidence that the lights and hood will be turned on. Any of the uncertainty will cause extreme annoyance, and the user should just prefer using a physical button to switch them. 

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

The Pan Detector can be used to detect whether the user have started cooking, and automatically switch on/off the stove/hood. 

Assuming the model is trained with a saute pan, the good environment is when the user actually want to start cooking with a saute pan, but a bad environment is when the user is cooking with some other pan, such as dutch oven or wok; another bad environment is stove is used as a storage space and the user only wish to leave the pan on the stove without intention of cooking. If instead of using teachable machine, we use other framework such as OpenCV object detection, then the good environment stay the same, but a bad environment is when other object (e.g. a plate) is placed on the stove but the user has no intention to start cooking. Those bad environment is also when the Pan Detector will break.

The Pan Detector may come in handy when the user really wish to cook, but it feels annoying if: 1. the user wish to cook but the system fail to detect and fail to switch on the stove/hood; 2. the user has no intention to cook but the stove/hood.

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

https://youtu.be/5PJMz4wX-OI

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

Instead of trying to identify a pan, wok, dutch oven, etc using a trained model, it is actually easier and more reasonable to identify if there's no pan at at using simple object detection. This is to consider the following 2 use cases where it does not necessarily make sense to turn on the hood and light everytime the user place a pan on the stove:

1. Cooking != hood on, the user could be simply boiling something and does not need the hood to be on.  

2. Pan on the stove != cooking, the user could sometimes leave the pan on the stove as a temporary storage. 

Considering those 2 use cases, it might be really annoying if the hood is on everytime when the user have no such intention. However, when there's no pan on the stove (for a certain period of time, such as 10 mins), it must mean that the stove should be off.

Therefore, for part 2, I am using the OpenCV object detection, and the design is to automatically switch off the hood/light if there are no pan on the stove for over 10 mins (for demo, I will count 10 secs instead of 10 mins).

**\*\*\*Include a short video demonstrating the finished result.\*\*\***

https://youtu.be/e5BqFuwti4g

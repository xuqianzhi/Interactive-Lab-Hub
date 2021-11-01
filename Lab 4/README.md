# Ph-UI!!!

For this lab, I'm designing a device that would generate random recipe for you when you don't know what to eat for your lunch/dinner.

### Part C
### Physical considerations for sensing

**\*\*\*Draw 5 sketches of different ways you might use your sensor, and how the larger device needs to be shaped in order to make the sensor useful.\*\*\***
![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%204/sketch_part1_1.jpg)
![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%204/sketch_part1_2.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

The first thought is just to push a button and let the device decide for you. However, people do have different feelings on each day, i.e. although the user might not know exactly what to eat, there might be a general category of food that the user would prefer. E.g., if the user don't have good appetite, the user might want to go with vegetarian foods only. That lead from 1st sketch to the 2nd sketch.

So how many categories should there be? The 2nd sketch allows a fixed number of category. But what if the software gets updated along time, and the number of category keeps increasing? Then we need a scrollview! This leads to 3rd - 5th sketch.

**\*\*\*Pick one of these designs to prototype.\*\*\***

I will pick the sketch #4 because it seems like the most intuitive design that the user would understand how to use without much explanation.


### Part D
### Physical considerations for displaying information and housing parts
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%204/sketch_part1_3.jpg)

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***

Although having a long wire between the joystick and the screen allows a more flexible control experience, when I'm thinking about the use cases, I don't really see a need for that. Just based on imagination, I think it make more sense to design the product just into one integrated box, and it the box just serves a single purpose of inspiring people what to eat for their lunch/dinner.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

I will pick design 3, where the joystick is on top of the screen.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

As explained above, this ensure the integrity of the design and gives user just a single box. Leaving the joystick inside the box may be hard for user to manipulate, and my design of choice seem to be provide user a easy manipulation. 

**\*\*\*Document your rough prototype.\*\*\***

The design, as expected, seem to provide a easy manipulation experience. However, applying too much pressure to the joystick sometimes crushes the box, and some reinforcement need to be done to stabilize the box a bit further.


LAB PART 2

### Part 2

Following exploration and reflection from Part 1, complete the "looks like," "works like" and "acts like" prototypes for your design, reiterated below.

### Part F
### Record

Document all the prototypes and iterations you have designed and worked on! Again, deliverables for this lab are writings, sketches, photos, and videos that show what your prototype:
* "Looks like": shows how the device should look, feel, sit, weigh, etc.
* "Works like": shows what the device can do
* "Acts like": shows how a person would interact with the device

I got a very good peer feedback that suggested me to apply this device at a restaurant/foodtruck instead of for home cooking. Therefore, for part 2, I am changing my use case scenario to be at restaurants, and my device would take people's general preference/demand, and suggest people random dishes that lies in the selected category. I am also adding a selection option that allow users to choose between slow cooking and fast cooking dishes, since people may be in a rush and just want a quick meal at a restaurant.

The device is like a little hand-held device that allows users to handle easily. This is to consider the possibility that people might want to pass this around the table and make decision for multiple people. Also, not everyone would want to get suggestion from this device, so it does not make sense to mount this device at a fixed position (e.g. at the table).

Here's the YouTube link: https://youtu.be/lKliSBksKrI

The device only allow user to scroll up, scroll down, and press the button to continue to the next page. The screen is well indicated, and it seems fairly intuitive among all test users (it was tested on 3 users).

All code lies in Lab4/my_control.py

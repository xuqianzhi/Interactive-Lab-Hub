
# Lab 3 Part 1

\*\***Write your own shell file to use your favorite of these TTS engines to have your Pi greet you by name.**\*\*
https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%203/my_text2speech.sh

\*\***Write your own shell file that verbally asks for a numerical based input (such as a phone number, zipcode, number of pets, etc) and records the answer the respondent provides.**\*\*

https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%203/my_speech2text.sh

### Storyboard

\*\***Post your storyboard and diagram here.**\*\*

![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%203/sketch_part1.jpg)

\*\***Please describe and document your process.**\*\*

This design, Aribo, is a voice-command music player. It supports functionality of play the music, volumn adjustment, and stop the music.

### Acting out the dialogue

https://www.youtube.com/watch?v=LridFtBDbWQ

\*\***Describe if the dialogue seemed different than what you imagined when it was acted out, and how.**\*\*

One edge case is "never mind", where user ask Aribo to play the music, but instantly regret the decision and want to tell Aribo "never mind, actually don't play it". In this case, we might need to design extra voice command to implement this.

### Wizarding with the Pi (optional)
In the [demo directory](./demo), you will find an example Wizard of Oz project. In that project, you can see how audio and sensor data is streamed from the Pi to a wizard controller that runs in the browser.  You may use this demo code as a template. By running the `app.py` script, you can see how audio and sensor data (Adafruit MPU-6050 6-DoF Accel and Gyro Sensor) is streamed from the Pi to a wizard controller that runs in the browser `http://<YouPiIPAddress>:5000`. You can control what the system says from the controller as well!

\*\***Describe if the dialogue seemed different than what you imagined, or when acted out, when it was wizarded, and how.**\*\*

# Lab 3 Part 2

For Part 2, you will redesign the interaction with the speech-enabled device using the data collected, as well as feedback from part 1.

## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
3. Make a new storyboard, diagram and/or script based on these reflections.

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

*Include videos or screencaptures of both the system and the controller.*

## Test the system
Try to get at least two people to interact with your system. (Ideally, you would inform them that there is a wizard _after_ the interaction, but we recognize that can be hard.)

Answer the following:

### What worked well about the system and what didn't?
\*\**your answer here*\*\*

### What worked well about the controller and what didn't?

\*\**your answer here*\*\*

### What lessons can you take away from the WoZ interactions for designing a more autonomous version of the system?

\*\**your answer here*\*\*


### How could you use your system to create a dataset of interaction? What other sensing modalities would make sense to capture?

\*\**your answer here*\*\*


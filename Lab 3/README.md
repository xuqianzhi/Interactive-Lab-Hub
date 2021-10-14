
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

# Lab 3 Part 2
## Prep for Part 2

1. What are concrete things that could use improvement in the design of your device? For example: wording, timing, anticipation of misunderstandings...
  * When the user change their mind in the middle of speaking, the user is capable of saying "never mind" and speak of a new decision
2. What are other modes of interaction _beyond speech_ that you might also use to clarify how to interact?
  * it's been suggested by many people that volumn and play/pause control should be done by button, so button control will be added
3. Make a new storyboard, diagram and/or script based on these reflections.
  ![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%203/sketch_part2_1.jpg)
  ![alt text](https://github.com/xuqianzhi/Interactive-Lab-Hub/blob/Fall2021/Lab%203/sketch_part2_2.jpg)

## Prototype your system

The system should:
* use the Raspberry Pi 
* use one or more sensors
* require participants to speak to it. 

*Document how the system works*

System would ask: what song would you like to play

option 1: state song name directly

option 2: state song A name, but change mind and play song B

option 3: state song A name, but change mind and stop playing

option 4: stop playing

*Include videos or screencaptures of both the system and the controller.*
https://youtu.be/kTdjX3j4Rqo

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


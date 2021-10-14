#!/usr/bin/env python3

from vosk import Model, KaldiRecognizer
import subprocess
import sys
import os
import wave
import json

if not os.path.exists("model"):
    print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
    exit (1)

wf = wave.open(sys.argv[1], "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    print ("Audio file must be WAV format mono PCM.")
    exit (1)

model = Model("model")
# You can also specify the possible word list
never_mind = "never mind "
numb = "numb "
from_the_inside = "from the inside "

def speak(filename):
    command = "./" + filename
    subprocess.call(command, shell=True)

rec = KaldiRecognizer(model, wf.getframerate(), never_mind + numb + from_the_inside)

while True:
    data = wf.readframes(4000)
    user_input = None
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        print(rec.Result())
        res = json.loads(rec.Result())
        user_input = res['text']
    else:
        print(rec.PartialResult())
        res = json.loads(rec.PartialResult())
        user_input = res['partial']
    if user_input:
        if never_mind in user_input:
            user_input.split(never_mind)[1]
        if numb in user_input:
            speak("song_playing.sh")
        elif from_the_inside in user_input:
            speak("song_playing.sh")

print(rec.FinalResult())

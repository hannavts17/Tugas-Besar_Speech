from gtts import gTTS


tts = gTTS(text="welcome to my website", lang='en')
tts.save("record.mp3")
print("Text Converted Successfully ")

import pyttsx3


engine = pyttsx3.init()

engine.say("welcome to geekscoders website ")
engine.setProperty('rate', 120)
engine.setProperty('volume', 0.9)
engine.runAndWait()
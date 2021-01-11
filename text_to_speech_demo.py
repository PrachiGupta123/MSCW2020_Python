"""
WAP to convert written text into speech

Step1:Import Functionality (GTTS) -  Google Text To Speech Functionality
Step2:Call Constructor
Step3:Output
"""
import gtts
import os
MyText = "Welcome to this online session on Python - I hope you are learning something New."
MyValue = gtts.gTTS(text = MyText,lang = 'en',slow = False)

MyValue.save("MySpeech.mp3")
os.system("MySpeech.mp3")

import gtts
import os
MyText = "Welcome to this online session on Python - I hope you are learning something New. Don't forget to have fun while coding."
MyValue = gtts.gTTS(text = MyText,lang = 'en',slow = True)

MyValue.save("MySpeech1.mp3")
os.system("MySpeech1.mp3")


#Python program to convert text to speech

#Pip install pyttsx3

# import pyttsx3

# text_speech=pyttsx3.init()

# for i in range(3):

#     sentence=input("Enter the Text: ")

#     if("Vignesh" in sentence):

#         word="Hello Mr.Vignesh The Boss"

#         text_speech.say(word)

#     else:
        
#         text_speech.say(sentence)

# text_speech.runAndWait()


#Python program to convert text to speech Another Method

#pip install gTTS

from gtts import gTTS

import os

mytext="Always be happy nanba life is very short"

language='en'

myobj=gTTS(text=mytext,lang=language,slow=True)

myobj.save('./Master.mp3')

# Playing the converted file
os.system("mpg321 welcome.mp3")


import os
import openai
import time
import speech_recognition as sr
import pyttsx3
import numpy as np
import pyttsx3

class _TTS:

    engine = None
    rate = None
    def __init__(self):
        self.engine = pyttsx3.init()


    def start(self,text_):
        self.engine.say(text_)
        self.engine.runAndWait()
		
		
openai.api_key = os.getenv('OPENAI_API_KEY')
r = sr.Recognizer()
engine = pyttsx3.init()
voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)

def listen_for(source):
    print("Listening...")

    while True:
        try:
            response_text = "test"
            print(f"OpenAI response: {response_text}")
			
            # Speak the response
            tts = _TTS()
            tts.start(response_text)
            del(tts)			
            print("Point 1")
			
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
			

# Use the default microphone as the audio source
with sr.Microphone() as source:
    listen_for(source)
print("Point 2")

# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext1 = "Hello. What is the capital of Hungary?"
mytext2 = "Hello. What is the maximum of integer numbers 2 and 5"
mytext3 = "Please turn on the switch"
mytext4 = "Please turn off the switch"
mytext5 = "Please turn on the switch labeled left"
mytext6 = "Please turn off the switch labeled left"
mytext7 = "Please press the button labeled forward"

# Language in which you want to convert 
language = 'en'

myobj1 = gTTS(text=mytext7, lang=language, slow=True) 
myobj1.save("Please press the button labeled forward.mp3") 


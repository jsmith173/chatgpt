# Import the required module for text 
# to speech conversion 
from gtts import gTTS 

# This module is imported so that we can 
# play the converted audio 
import os 

# The text that you want to convert to audio 
mytext1 = "Hello. What is the capital of Hungary?"
mytext2 = "Hello. What is the maximum of integer numbers 2 and 5"

# Language in which you want to convert 
language = 'en'

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=mytext1, lang=language, slow=False) 

# Saving the converted audio in a mp3 file named 
# welcome 
myobj.save("capitalhungary.mp3") 

# Playing the converted file 
#os.system("mpg321 welcome.mp3") 

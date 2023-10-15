import os, openai, speech_recognition as sr, pyttsx3

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
        print("Listening...(1)")
        audio = r.listen(source)
        try:
            print("Listening... (2)")
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            if not text:
                continue

            # Send input to OpenAI API
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{text}"}]) 
            response_text = response.choices[0].message.content
            print(f"OpenAI response: {response_text}")
			
            # Speak the response
            tts = _TTS()
            tts.start(response_text)
            del(tts)			
			
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))		

# Use the default microphone as the audio source
with sr.Microphone() as source:
    listen_for(source)

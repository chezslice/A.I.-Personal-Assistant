import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audio_response):
    print(audio_response)
    tts = gTTS(text=audio_response, lang="en")
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio = r.listen(source)

        # Google Speech Recognition in use.
        data = ""
        try:
            data = r.recognize_google(audio)
            print("You said: " + data)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return data

# Colin is name of the A.I.
def Colin(data):
    # Different responses are taken from the data and fed thru Colin, and Colin will produce a response.
    # Time, Location and to see how Colin is doing today.
    if "how are you" in data:
        speak("I am Good Thanks for asking")
    if "what time is it" in data:
        speak(ctime())
    if "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Sir, I will show you where " + location + " is.")
        os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

# Initialize function.
time.sleep(4)
speak("Hi Sir, what can I help do for you?")
while 1:
    data = record()
    Colin(data)

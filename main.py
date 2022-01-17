import speech_recognition as sr
import pyaudio
from gtts import gTTS
import random
import playsound
from pydub import AudioSegment
from pydub.playback import play


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say somthing")
        audio = r.listen(source)


    try:
        speech = r.recognize_google(audio, language="ru-Ru")
        print("You said: ", speech )
        return speech
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))


def say(text):
    voice = gTTS(text, lang="ru")
    unique_name = "audio" + str(random.randint(0,100000)) + ".mp3"
    voice.save(unique_name)
    playsound.playsound(unique_name)
  
def handle_message(message):
    if "hello" in message:
        say("Hello")
    else:
        say("I dont Know a comand like that")
def finish():
    pass

if __name__ == "__main__":
    command = listen()
    handle_message(command)
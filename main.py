# from email.mime import audio
import webbrowser
import speech_recognition as sr
import time
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer() # used to recognize speech

def record_audio(ask = False):
    with sr.Microphone() as source: # microphone is the source
        if ask:
            system_speak(ask)
        audio = r.listen(source) # picks up audio from microphone
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio) # recognizes the audio
        except sr.UnknownValueError: # Unclear speech
            system_speak("Sorry, I didn't get that")
        except sr.RequestError: # Service fail
            system_speak("Sorry, I'm not available right now")
        return voice_data

def system_speak(audio_string):
    tts = gTTS(text= audio_string, lang = 'en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def respond(voice_data):
    if 'what is your name' in voice_data: 
        system_speak('My name is Helper') 
    if 'what time is it' in voice_data: 
        system_speak(ctime())
    if 'search' in voice_data:
        search = record_audio("What do you want to search for?")
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        system_speak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = record_audio("What is the location?")
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        system_speak('Here is the location of ' + location)
    if 'exit' in voice_data:
        system_speak('Have a great day!')
        exit()

time.sleep(1)
system_speak('How can I help you?') # prompt user
while 1:
    voice_data = record_audio() # calls record function
    respond(voice_data) # calls respond function

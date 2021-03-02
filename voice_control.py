import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes

def talk(text):
    engine.say(text)
    engine.runAndWait()

def get_command():
    try:
        with sr.Microphone() as source:
            print(f'listening...')
            voice = listener.listen(source, timeout=3)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f'I heard: {command}')
    except:
        command = 'Error'
    return command


def listen():
    command = get_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play ', '')
        talk('playing' + song)
        print(f'playing {song}')
        pywhatkit.playonyt(song)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'find' in command:
        what = command.replace('find ', '')
        try:
            information = wikipedia.summary(what,1)
        except:
            information = 'Didn\'t find ' + what + ' in wikipedia!'
        print(information)
        talk(information)
    elif command=='Error':
        talk('I hear only silence!')
    else:
        talk('I can\'t do it yet!')


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
talk('Hello! What you need?')

while True: 
    listen()

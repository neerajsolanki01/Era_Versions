import speech_recognition as sr  # pip install SpeechRecognition
#  From Archived: Unofficial Windows Binaries for Python Extension Packages " https://www.lfd.uci.edu/~gohlke/pythonlibs/ "
#  pip install .\PyAudio-0.2.11-cp38-cp38-win_amd64.whl

import pyttsx3                    # pip install pyttsx3
import pywhatkit                  # pip install pywhatkit
import datetime
import wikipedia                  # pip install wikipedia
import pyjokes                    # pip install pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)
engine.setProperty('rate', 200)

engine.say('Hey, I Am Your Personal Virtual Assistant.')
engine.say('How Can I Help You.')
engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def takeCommand():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'friday' in command:
                command = command.replace('friday', '')
                print(command)
    except:
        pass
    return command.lower()

def run():
    command = takeCommand()
    print(command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing...' + song)
        pywhatkit.playonyt(song)
        print('Playing...')

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current Time Is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    # Fun Part
    elif 'are you single' in command:
        talk('I am in a relationship with the, internet or a wifi.')

    elif 'what are you doing' in command:
        talk('I am talking with you Dear.')

    elif 'exit' in command:
        exit()

    elif 'stop' in command:
        exit()

    else:
        talk('Sorry, I did not understand. Can you say it again, please.')
        print('Sorry, I did not understand. Can you say it again, please.')

while True:
    # run era()
    run()
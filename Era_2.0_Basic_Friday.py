import keyboard
import speech_recognition as sr
import pyttsx3
import random
import datetime
import wikipedia
import webbrowser
import pywhatkit
import os
from playsound import playsound
import mss
import cv2
from requests import get
import numpy as np
import pyautogui
import smtplib
import pyjokes
from pywikihow import search_wikihow
import requests
from bs4 import BeautifulSoup
import pyscreenshot as ImageGrab
from googletrans import Translator
# from PyDictionary import PyDictionary as Dict

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[5].id)
Assistant.setProperty('rate', 200)

Assistant.say('Hey, I Am Friday 2.0, Your Personal Virtual Assistant.')
Assistant.say('How Can I Help You.')
Assistant.runAndWait()


# Speak
def speak(audio):
    print("   ")
    Assistant.say(audio)
    print(f" {audio}")
    print("   ")
    Assistant.runAndWait()

# Take Command.
def takecommand():
    command = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # speak('Listening...')
        command.pause_threshold = 1
        audio = command.listen(source, 0, 4)

        try:
            print('Recognizing...')
            # speak('Recognizing...')
            query = command.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except:
            return "none"
        return query.lower()

# To Wish Me.
def wishMe():
    hour = int(datetime.datetime.now().hour)

    if 0 <= hour <= 11:
        speak('Good Morning')

    elif 12 <= hour <= 15:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

# Task Perform.
def TaskExe():
    wishMe()

    # Take Hindi
    def TakeHindi():
        command = sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening...')
            command.pause_threshold = 1
            audio = command.listen(source)
            try:
                print('Recognizing...')
                query = command.recognize_google(audio, language='hi')
                print(f"user said: {query}")
            except:
                return "none"
            return query.lower()
    def Tran():
        speak('Tell me the line.')
        line = TakeHindi()
        translate = Translator()
        result = translate.translate(line)
        Text = result.text
        speak(Text)

    # Temperature
    '''def Temp():
        search = "temperature in dewas"
        url = f"https://www.bing.com/search?q={search}"
        r = requests.get(url)
        data = BeautifulSoup(r.text,"html.parser")
        temperature = data.find("div", class_ = "BNeawe").text
        speak(f"The temperature is {temperature} celcius")'''

    # Speedtest
    def SpeedTest():
        import speedtest
        speak("Cheaking speed...")
        speed = speedtest.Speedtest()
        downloading = speed.download()
        correctDown = int(downloading/800000)
        uploading = speed.upload()
        correctUpload = int(uploading / 800000)

        if 'downloading' in query:
            speak(f"The downloading speed is {correctDown} mbps")
        elif 'uploading' in query:
            speak(f"The uploading speed is {correctUpload} mbps")
        else:
            speak(f"The downloading speed is {correctDown} mbps and The uploading speed is {correctUpload} mbps")

    # YouTube Automation
    def YoutubeAuto():
        speak('What i do in youtube')
        comm = takecommand()

        if 'pause' in comm:
            keyboard.press('space bar')
        elif 'restart' in comm:
            keyboard.press('0')
        elif 'mute' in comm:
            keyboard.press('m')
        elif 'skip' in comm:
            keyboard.press('l')
        elif 'back' in comm:
            keyboard.press('j')
        elif 'full screen' in comm:
            keyboard.press('f')
        speak('Done.')

    # Chrome Automation
    def ChromeAuto():
        speak('Chrome automation started.')
        command = takecommand()

        if 'close tab' in command:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in command:
            keyboard.press_and_release('ctrl + t')
        elif 'history' in command:
            keyboard.press_and_release('ctrl + h')
        elif 'download' in command:
            keyboard.press_and_release('ctrl + j')

    # Dictionary
    '''def Dictionary():
        speak('Active Dictionary.')
        prob = takecommand()

        if 'meaning' in prob:
            prob = prob.replace('what is the meaning of', '')
            result = Dict.meaning(prob)
            speak(f"The Meaning of {prob} is {result}")
        elif 'synonym' in prob:
            prob = prob.replace('what is the synonym of', '')
            result = Dict.synonym(prob)
            speak(f"The synonym of {prob} is {result}")
        elif 'antonym' in prob:
            prob = prob.replace('what is the antonym of', '')
            result = Dict.antonym(prob)
            speak(f"The antonym of {prob} is {result}")'''

    # Open Apps
    def OpenApps():

        if 'notepad' in query:
            path = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(path)
            speak('Opening Notepad.')

        elif 'microsoft word' in query:
            path = 'C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\word'
            os.startfile(path)
            speak('Opening MS Word')

        elif 'command prompt' in query:
            os.system('start cmd')
            speak('Opening Command Prompt.')


        # elif 'camera' in query:
        #    cap = cv2.VideoCapture(0)
        #    while True:
        #        ret, img = cap.read()
        #        cv2.imshow('webcam', img)
        #        k = cv2.waitKey(50)
        #        if k == 27:
        #            break;
        #    cap.release()
        #    cv2.destroyAllWindow()

    # Close Application.
    def CloseApps():

        if 'notepad' in query:
            os.system("TASKKILL /F /im notepad.exe")

        elif 'microsoft word' in query:
            os.system("TASKKILL /F /im WINWORD.EXE")

        elif 'command prompt' in query:
            os.system("TASKKILL /F /im cmd.exe")

    # Send Email.
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('neerajsolanki271@gmail.com', 'kkji gyqo huwb iqez')
        server.sendmail('neerajsolanki271@gmail.com', to, content)
        server.close()

    # Whatsapp.
    def whatsapp():
        speak('Tell me the name of the person.')
        name = takecommand()
        #elif 'time' in query:
        #    time = datetime.datetime.now().strftime('%I:%M %p')
        #    print(time)
        #    speak('Current Time Is ' + time)


        if 'vinita' in name:
            speak('Tell me the message.')
            msg = takecommand()
            speak('Tell me the time')
            speak('Hour')
            hour = int(takecommand())
            speak('Minutes')
            min = int(takecommand())
            pywhatkit.sendwhatmsg('+916260585621', msg, hour, min, 20)
            speak('Whats app message send.')

        elif 'ritesh' in name:
            speak('Tell me the message.')
            msg = takecommand()
            speak('Tell me the time')
            speak('Hour')
            hour = int(takecommand())
            speak('Minutes')
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+918817956908", msg, hour, min, 20)
            speak('Whats app message send.')

        else:
            speak('Tell me the phone number.')
            phone = int(takecommand())
            ph = '+91' + phone
            speak('Tell me the message.')
            msg = takecommand()
            speak('Tell me the time')
            speak('Hour')
            hour = int(takecommand())
            speak('Minutes')
            min = int(takecommand())
            pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
            speak('Whats app message send.')
            pywhatkit.sendwhatmsg()




# While True Statement, Task Execution.
    while True:
        query = takecommand()

        # Open Application
        if 'open notepad' in query:
            OpenApps()

        elif 'open microsoft word' in query:
            OpenApps()

        elif 'open command prompt' in query:
            OpenApps()

        elif 'open browser' in query:
            path = 'C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe'
            os.startfile(path)
            speak('Opening Microsoft Edge Browser.')

        elif 'open chrome' in query:
            path = 'C:\\Users\\Public\\Desktop\\Google Chrome.lnk'
            os.startfile(path)
            speak('Opening Chrome Browser.')


        # Close Application.
        elif 'close notepad' in query:
            CloseApps()

        elif 'close microsoft word' in query:
            CloseApps()

        elif 'close command prompt' in query:
            CloseApps()

        elif 'close browser' in query:
            os.system("TASKKILL /F /im msedge.exe")

        elif 'close chrome' in query:
            os.system("TASKKILL /F /im chrome.exe")
            speak('Close Chrome Browser')


        # Music
        elif 'music' in query:
            music_dir = 'C:\\Music\\My Favorite Songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))
            speak('Playing Music...')

        # Play anything on YouTube.
        elif 'play' in query:
            song = query.replace('play', '')
            speak('Playing...' + song)
            pywhatkit.playonyt(song)
            speak('Playing...')
            print('Playing...')

        # Time , Date , Temperature
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            speak('Current Time Is ' + time)

        elif 'date' in query:
            date = datetime.datetime.now().strftime('%d-%m-%Y')
            print(date)
            speak('Today date is ' + date)

        # elif 'temperature' in query:
        #    Temp()

        # Internet Speed
        elif 'internet speed' in query:
            SpeedTest()
        elif 'downloading speed' in query:
            SpeedTest()
        elif 'uploading speed' in query:
            SpeedTest()

        # Screenshot.
        elif 'screenshot' in query:
            speak('Ok, What should i name that file')
            path = takecommand()
            path1name = path + ".png"
            path1 = "C:\\Image\\Screenshot\\" + path1name
            image = pyautogui.screenshot()
            image.save(path1)
            os.startfile("C:\\Image\\Screenshot")
            speak("Your Screenshot is here.")

        # IP Address.
        elif 'ip address' in query:
            ip = get('https://api.ipify.org').text
            speak(f'your IP address is {ip}')

        # Wikipedia.
        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=4)
            speak(results)
            print(results)

        # Open Web browser.

        # elif 'website' in query:
        #    query = query.replace("website", "")
        #    web1 = query.replace("website", "")
        #    web2 = 'https://www.' + web1 + '.com'
        #    webbrowser.open(web2)
        #    speak('Opening')

        elif 'website' in query:
            speak('Tell me the name of website.')
            name = takecommand()
            web = 'https://www.' + name + '.com'
            webbrowser.open(web)
            speak('Opening...')

        elif 'instagram' in query:
            webbrowser.open('www.instagram.com')
            speak('Opening Instagram.')

        # YouTube Automation
        elif 'youtube tool' in query:
            YoutubeAuto()
        elif 'pause' in query:
            keyboard.press('space bar')
        elif 'restart' in query:
            keyboard.press('0')
        elif 'mute' in query:
            keyboard.press('m')
        elif 'skip' in query:
            keyboard.press('l')
        elif 'back' in query:
            keyboard.press('j')
        elif 'full screen' in query:
            keyboard.press('f')

        # Browser Automation
        elif 'browser auto' in query:
            ChromeAuto()
        elif 'close tab' in query:
            keyboard.press_and_release('ctrl + w')
        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl + t')
        elif 'history' in query:
            keyboard.press_and_release('ctrl + h')
        elif 'download' in query:
            keyboard.press_and_release('ctrl + j')

        # Translator Not Working
        elif 'translate' in query:
            Tran()

        # Reminder
        elif 'remind me' in query:
            remembermsg = query.replace("remind me", " ")
            speak('You tell me to remind you :'+remembermsg)
            remember = open('data.text', 'w')
            remember.write(remembermsg)
            remember.close()
        elif 'remember' in query:
            remember = open('data.text', 'r')
            speak('You tell me to remind you:' + remember.read())

        # Search on google
        elif 'search' in query:
            import wikipedia as googleScrap
            query = query.replace('search', ' ')
            query = query.replace('What is ', ' ')
            pywhatkit.search(query)
            try:
                result = googleScrap.summary(query, 2)
                speak(result)
            except:
                return "none"

        # How to make
        elif 'how to' in query:
            speak("Getting data from the internet")
            op = query.replace("friday", " ")
            max_result = 1
            how_to_func = search_wikihow(op, max_result)
            assert len(how_to_func) == 1
            how_to_func[0].print()
            speak(how_to_func[0].summary)

        # Joke.
        elif 'joke' in query:
            speak(pyjokes.get_joke())

        # Dictionary
        # elif 'dictionary' in query:
        #    Dictionary()


        # YouTube Search
        elif 'youtube search' in query:
            speak('What should i search on youtube.')
            cm = takecommand().lower()
            web = 'https://www.youtube.com/results?search_query=' + cm
            webbrowser.open(f'{web}')
            speak(cm)

        # Google Search.
        elif 'google' in query:
            speak('What should i search on google.')
            cm = takecommand().lower()
            webbrowser.open(f'{cm}')

        # Alarm Not Working
        elif 'alarm' in query:
            speak('Tell Me the time')
            time = input('Enter the time : ')
            while True:
                Time_Ac = datetime.datetime.now()
                now = Time_Ac.strftime("%H:%M:%S")
                if now == time:
                    speak('Your alarm is ringing.')
                    playsound('Superman Rising.mp3')
                elif now > time:
                    break
                    speak('Alarm Closed')

        # Not Working
        elif 'whatsapp' in query:
            whatsapp()

        # Email
        elif 'email to neeraj' in query:
            try:
                speak('What should i say.')
                content = takecommand().lower()
                to = 'solankineeraj39@gmail.com'
                sendEmail(to, content)
                speak('Email Send')

            except Exception as e:
                print(e)
                speak('Email Not Send')

        elif 'email to vinita' in query:
            try:
                speak('What should i say.')
                content = takecommand().lower()
                to = 'vinitasolanki017@gmail.com'
                sendEmail(to, content)
                speak('Email Send')

            except Exception as e:
                print(e)
                speak('Email Not Send')










        # Fun Part.
        elif 'hello' in query:
            speak('hello sir')


        elif 'are you single' in query:
            speak('I am in a relationship with the, internet or a wifi.')

        elif 'what are you doing' in query:
            speak('I am talking with you Dear.')

        # Exit Part.

        elif 'break' in query:
            speak('Ok sir, you can call me anytime. Just say Wake up.')
            break

        elif 'exit' in query:
            speak('Thanks for using me , have a good day...')
            exit()

        elif 'stop' in query:
            speak('Thanks for using me , have a good day...')
            exit()

        elif 'not now' in query:
            speak('Thanks for using me , have a good day...')
            exit()



TaskExe()
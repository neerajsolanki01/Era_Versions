import openai                                       # pip install openai
import pyttsx3                                      # pip install pyttsx3
import speech_recognition as sr                     # pip install SpeechRecognition
#  From Archived: Unofficial Windows Binaries for Python Extension Packages " https://www.lfd.uci.edu/~gohlke/pythonlibs/ "
#  pip install .\PyAudio-0.2.11-cp38-cp38-win_amd64.whl
import webbrowser

openai.api_key = "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"

completion = openai.Completion()

def Reply(question):
    prompt = f'You:{question}\n Jarvis :'
    response = completion.create(prompt = prompt, engine="text-davinci-002", stop=['\You'], max_tokens=200)
    answer = response.choices[0].text.strip()
    return answer

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[5].id)
engine.setProperty('rate', 200)

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak('Hey, I Am Friday 4.0, Your personal virtual assistant.')
engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print('You Said: {} \n'.format(query))
        except Exception as e:
            print('I did not understand.')
            return "None"
        return query

if __name__== '__main__':
    while True:
        query = takecommand().lower()
        answer = Reply(query)
        print(answer)
        speak(answer)
        if 'hello' in query:
            speak('Hello Sir')
        elif 'break' in query:
            break
        elif 'exit' in query:
            exit()
        elif 'stop' in query:
            exit()
        elif 'not now' in query:
            exit()
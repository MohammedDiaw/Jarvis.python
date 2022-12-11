import speech_recognition as sr
import pyttsx3 #text to speach
import pywhatkit #search youtube
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

engine.say('I am jarvis your personal assistant')
engine.say('what can I do for you today')
engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('jarvis', '')
                print(command)
    except:
        pass
    return command

def run_jarvis():
    command = take_command()
    print(command)
    print('command')
    if 'play' in command:
        song = command.replace('play', '')
        print('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p:') #I = U.S time P = am/pm
        print(time)
        print('The current time is' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        print('info')
    elif 'joke' in command:
        print(pyjokes.get_joke())
        return pyjokes
    else:
        print('please say command again')

while True:
    run_jarvis()

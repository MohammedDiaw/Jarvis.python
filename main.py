# imput (print "what song would you like to listen too?")



import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command() -> listener:
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
        if 'jarvis' in command:
            command = command.replace('jarvis', '')
            print(command)
    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print (command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.now().strttime('%I:%M %p')
        print(time)
        talk('Current time is '+time)
    elif 'who is ' in command:
        person: command.replace('who is ', '' )
        info = wikipedia.summary(person, 3)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.getjoke())
    else:
        talk('Please say the command again.')


while True:
    run_jarvis

import speech_recognition as sr
import pyttsx3
import os
import datetime

# Text to speech engine
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Listen and recognize
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Sorry, I didn't catch that.")
        return "none"

# Main loop
while True:
    query = take_command()

    if "my name is saurabh" in query:
        speak("Hello Saurabh! How can I help you?")
    elif "hello jarvis" in query:
        speak("Hello! I am listening.")
    elif "open notepad" in query:
        speak("Opening Notepad")
        os.system("notepad")
    elif "what is the time" in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    elif "stop" in query:
        speak("Goodbye Saurabh!")
        break
    else:
        speak("I didn't understand you saurabh.")
import speech_recognition as sr

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Sorry, I didn't get that")
        return "none"

while True:
    query = take_command()

    if "my name is saurabh" in query:
        print("Hello Saurabh, nice to meet you!")
    elif "hello jarvis" in query:
        print("Hello! How can I help you?")
    elif "stop" in query:
        print("Goodbye!")
        break
    else:
        print("I didn't understand that command.")
 

import multiprocessing
import subprocess

# To run Jarvis
def startJarvis():
        # Code for process 1
        print("Process 1 is running.")
        from main import start
        start()

# To run hotword
def listenHotword():
        # Code for process 2
        print("Process 2 is running.")
        from engine.features import hotword
        hotword()


    # Start both processes
if __name__ == '__main__':
        p1 = multiprocessing.Process(target=startJarvis)
        p2 = multiprocessing.Process(target=listenHotword)
        p1.start()
        p2.start()
        p1.join()

        if p2.is_alive():
            p2.terminate()
            p2.join()

        print("system stop")
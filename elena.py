from asyncore import write
from tkinter import E
import googlesearch
from numpy import take
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import sys
from googlesearch import search as sre
import pywhatkit as pwt
import json
import keyboard

# import elena_gui
import pass_generator
import cred

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# the gui function


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("Hello Sir How are you I am Elena How can I help you")


# login detector
def login_detector():
    f = open("auth_data.json")
    auth_json_data = json.load(f)
    if isinstance(auth_json_data, dict):
        try:
            if auth_json_data["auth"] == auth_json_data["auth"]:
                pass
            else:
                with open("errors.txt", "w") as f:
                    f.write("Authentication Failed due to Missmatch of data")
            pass
        except Exception as e:
            with open("errors.txt", "w") as f:
                f.write(e)
    else:
        pass
    pass


login_detector()

# authentation
def authanticator():
    try:
        data = {
            "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "auth": pass_generator.authquator(""),
        }
        data_main = json.dumps(data, indent=4)
        with open("auth_data.json", "w") as f:
            f.write(data_main)
    except Exception as e:
        with open("errors.txt", "w") as f:
            f.write(e)


# shortcut key program
def shortcut(key):
    keyboard.add_hotkey(key)


# functions for shortcut keys
def open_websites(query):
    speak("Which website do you want to open")
    query = takeCommand()
    webbrowser.open(query)
    speak("Opening Website" + query)
    webbrowser.open(query)


# AI of elena


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hmmmmmm....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-IN")
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def ask_name(name):
    speak("Hello I am Elena , What is your Good Name")
    name = takeCommand().replace("my name is", "")
    elena_name = json.dump(name) in elena_name


def ask_cred():
    speak("Okay! Let me ask you some details real quick")
    try:
        try:
            authanticator()
            speak("Authentication Process Completed")
        except Exception as e:
            with open("errors.txt", "w") as f:
                f.write(e)
            speak(
                "Error Creating a token Currently! You might have to login again next Time"
            )

    except:
        speak("Sorry! , i was unable to do this at current moment")

    pass


def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(cred.mail_id, cred.password)
    server.sendmail(to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open website" in query:
            speak("Which website do you want to open")
            query = query.replace("open website", "")
            speak("Opening Website" + query)
            webbrowser.open(query)

            pass
        elif "open application" in query:
            speak("Which application do you want to open")
            query = query.replace("open application", "")
            speak("Opening Application" + query)
            os.system(query)
            pass

        # elif "Hello how are you" or "hi how are you doing" or "sup " in query:
        #     speak("I am doing Great Thanks for asking")
        elif "Go to sleep" in query:
            speak("taking a nap, Say hello elena to wake me up again")
            while True:
                query = takeCommand().lower()
                if "hello elena" in query:
                    speak("Hello Sir How are you I am Elena How can I help you")
                    break
        elif "open google" in query:
            webbrowser.open("google.com")
            print("program is opening google")

        elif "open youtube" in query:
            webbrowser.open("youtube.com")
            print("program is opening youtube")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "open geek" in query:
            webbrowser.open("geeksforgeeks.com")
            print("program is opening stackoverflow")
        elif "how are you" in query:
            speak("I am Doing Great thanks for asking")
        elif "search for" in query:
            query = query.replace("search for", "")
            pwt.search(query)
        elif "google search" in query:
            query = query.replace("google search", "")
            pwt.search(query)

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open code" in query:
            codePath = "C:\\Users\\Abhay\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif "open browser" in query:
            webbrowser.open("google.com")
        elif "open notepad" in query:
            notepadPath = "C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(notepadPath)
        elif "what is" in query:
            pwt.search(query)
        elif "who is" in query:
            pwt.search(query)
        elif "how is" in query:
            pwt.search(query)
        elif "where is" in query:
            pwt.search(query)
        elif "how is the weather" in query:
            pass  # add the weather
        elif "create a password" in query:
            pass_generator.password()
            speak(pass_generator.passw, "is the password")
        elif "Email To" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("To whom Should i send")
                to = takeCommand()
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend  . I am not able to send this email")
        elif "exit the program" in query:
            speak("Bye bye Have a great day")
            sys.exit()
        # else:
        #     speak("Sorry I did not understand")
        #     speak("Say that again please")
        #     continue

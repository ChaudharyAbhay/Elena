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
import csv

# import elena_gui
import pass_generator
import cred

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


# the gui function to be added here should work with rest of the code running on loop


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

#this is the wishme functions runs everytime
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak(" How are you I am Elena How can I help you")


# main data
data = {}


def data_commit():
    with open("user_data.json", "w") as f:
        json.dump(data, f)


# login detector - it is not in work currently Working shall be added when email login function would be on work
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


#Creates a token for a particular device to remember the credentials and data
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


def calculate(query):
    int first = [int(i) for i in query.split() if i.isdigit()]
    first = first
    int second = [int(i) for i in query.split() if i.isdigit()]
    second = second
    operator = [int(i) for i in query.split() if i== "add","subtract","multiply","divide"]
    if operator == "add":
        result = first+second
        pass
    elif operator == "subtract":
        result = first-second
        pass 
    elif operator == "multiply":
        result == first*second
    elif operator == "divide":
        result = first/second
    return operator


# AI of elena it shall contan all the frequent data user asks and process it in a way that user wants.

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
#set reminder function
def reminder(time):
    cur = datetime.datetime.now()
    utime = query
    while utime != cur:
        return cur


#asks for the name in stores it in data
def askname():
    with open("user_data.json", "r") as f:
        data2 = json.load(f)
    if "Name" in data2:
        pass
    else:
        speak("May i ask your good name please")
        name = query.replace("my name is", "")
        data.update({"Name": name})
        data_commit()

#asks for credentials (email login)
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

#send email function working with smptlib
def sendEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login(cred.mail_id, cred.password)
    server.sendmail(to, content)
    server.close()
#error handeling for speech commands
def report_error(e):
    with open("errors.txt", "w") as f:
        f.write(e)
#opening data of question bank
with open("question_bank.json" ,"r") as f:
    quest = json.load(f)
    pass    
#completes the query and requests by the user
if __name__ == "__main__":
    wishMe()
    while True:
        
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if "wikipedia" in query:#opens wikipedia
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open website" in query:#opens any website , asked by the user *removing open website from query
            speak("Which website do you want to open")
            query = query.replace("open website", "")
            speak("Opening Website" + query)
            webbrowser.open(query)

            pass
        elif "open application" in query:#opens application using os.system asked by the user *removing oepn appication from query
            speak("Which application do you want to open")
            query = query.replace("open application", "")
            speak("Opening Application" + query)
            try:
                os.system(query)
            except Exception as e:
                report_error(e)
                speak("Sorry! , i was unable to do this at current moment")    
            
            pass
        

        elif "Go to sleep" in query:#disables mic and goes on sleep DOES NOT WORK CURRENTLY
            speak("taking a nap, Say hello elena to wake me up again")
            while True:
                query = takeCommand().lower()
                if "hello elena" in query:
                    speak("Hello Sir How are you I am Elena How can I help you")
                    break
        #opening some common webites *Removing open from query            
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
        #search for uses google lib and searches on google for results *Removes 'search for' from query    
        elif "search for" in query:
            query = query.replace("search for", "")
            pwt.search(query)
        elif "google search" in query:
            #uses google for search Same function as above *Removes 'google search' from query
            query = query.replace("google search", "")
            pwt.search(query)

        elif "the time" in query:#tells the current time
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")
        elif "open code" in query:#useless
            codePath = "vscode.exe"
            try:
                os.startfile(codePath)
            except Exception as e:
                report_error(e) 
                speak("Sorry I was unable to do this at current moment")
        elif "open browser" in query:#opens the default browser *may open internet explorer for some users
            webbrowser.open("google.com")
        elif "open notepad" in query:#useless 2
            notepad = "notepad.exe"
            try:
                os.startfile(notepad)
            except Exception as e:
                report_error(e) 
                speak("Sorry I was unable to do this at current moment") 
        
         #some basic what is who is how is questions , uses google to answer and opens the browser as result *Does not remove anything from query
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
        elif "create a password" in query:#creates a random digit passwork using pass_generator file
            pass_generator.password()
            speak(pass_generator.passw, "is the password")
        elif "Email To" in query:#sends email using the email function made
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
        elif "set reminder" , "remind me" in query:
            #ask time also
            reminder(time)
        elif "open file" in query:
            query = query.replace("open file" , "")
            try:
                os.open(query)
                pass
            except:
                speak("Sorry! File Not Found")

        #making general talking instances 
        
            
        elif "exit the program" in query:
            speak("Bye bye Have a great day")
            sys.exit()
        # else:
        #     speak("Sorry I did not understand")
        #     speak("Say that again please")
        #     continue

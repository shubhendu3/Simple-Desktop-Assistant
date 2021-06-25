import pyttsx3
import speech_recognition as sr
import datetime
from datetime import date
import wikipedia
import webbrowser
import os
import smtplib
import sys

print("Initializing Neville")
master = "Shubhendu"
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty("voice", voices[0].id)

# Speak function will pronouce the stirng which is passsed to it.
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Wishes good morning, afternoon or evening as per the current time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    print(hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning" + master)

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon" + master)

    else:
        speak("Good Evening" + master)

    speak("I am Neville. How may I help you?")

wishMe()

# Sending emails 

def sendEmails(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com', '*******')
    server.sendmail("xyz@gmail.com", to , content)
    server.close()
while(True):

    # Main program starts here
    def nextHelp():
        speak("How May I help you next.")

    # This function will take command form the microphone
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=3)
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio)
            print("User said: " + query)

        except Exception as e:
            print("Say that again please")
            query = None
        return query


    #speak("Initializing Jarvis...")
    query = takeCommand()
    

    # Logic for executing tasks as per query
    if 'wikipedia' in query.lower():
        speak("Searching Wikipedia...")
        query = query.replace('wikipedia', '')
        results = wikipedia.summary(query, sentences=2)
        print(results)
        speak(results)

    elif 'open youtube' in query.lower():
        webbrowser.open('youtube.com')
    #url = 'youtube.com'
    #chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    #webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open("http://google.com")

    elif 'open google' in query.lower():
        webbrowser.open('google.com')

    elif 'open reddit' in query.lower():
        webbrowser.open('reddit.com')

    elif 'open facebook' in query.lower():
        webbrowser.open('facebook.com')

    elif 'open instagram' in query.lower():
        webbrowser.open('instagram.com')

    elif 'open gmail' in query.lower():
        webbrowser.open('gmail.com')


    elif 'play music' in query.lower():
        songs_dir = "D:\\song"
        songs = os.listdir(songs_dir)
        print(songs)
        os.startfile(os.path.join(songs_dir, songs[0]))
    
    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak("The time is: "+ strTime)

    elif "today's date" in query.lower():
        Date = date.today()
        Date = str(Date)
        speak("Today's date is: "+Date)

    elif 'open code' in query.lower():
        codepath = "D:\\VScode\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)

    elif 'thank you' in query.lower():
        speak("It was my pleasure to help you out. I look forward to helping you again soon.")

    elif 'send email' in query.lower():
        try :
            speak("What should I send.")
            content = takeCommand()
            to = "xyz@gmail.com"
            sendEmails(to, content)
            speak("Email has been send successfully.")
        except Exception as e:
            print(e)

    elif 'rest' or 'sleep' or 'stop' in query.lower():
        speak("Thank You. I will rest now. Do wake me up I you need any help.")
        sys.exit()
    nextHelp()
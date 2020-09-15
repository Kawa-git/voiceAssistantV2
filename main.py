import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import wolframalpha #pip install wolframalpha
import os

browser_path ='C://Program Files//Mozilla Firefox//firefox.exe %s'
visual_studio_code_path = 'F:\\VisualStudioCode\\Code.exe'
steam_path =None

ClinteWolfram = wolframalpha.Client("487PW2-38VPTQHH4R")
print("Initializing jarvis")
outputWolfram =''

#Pronounces the string which is passed to it
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) #voices[0] is italian voice
def speak(text):
    engine.say(text)
    engine.runAndWait()
with open("jarvisMaster.master", "r")as f:
    try:
        MASTER=f.read()
    except:
        speak("error reading jarvisMaster.master file")

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak("Good morning"+MASTER)
    elif hour>=12 and hour<18:
        speak("Good afternoon"+MASTER)
    else:
        speak("Good evening"+MASTER)
    
    speak("I'm jarvis, how may I help you?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-us')
        print("user said:  "+query)
    except Exception as e:
        print("Say that again please")
        query=''
    return query.lower()



#Logic for executing tasks
while True:
    query=takeCommand()
    if('jarvis' in query):
        query = query.replace("jarvis", "")
        if 'wikipedia' in query:
            speak('Searching on wikipedia..')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences = 2)
                speak(results)
            except:
                speak("Nothing found on wikipedia")

        elif 'open firefox' in query or 'duckduckgo' in query:
            url = "https://duckduckgo.com/"
            webbrowser.get(browser_path).open(url)

        elif 'open amazon' in query:
            url = "www.amazon.com"
            webbrowser.get(browser_path).open(url)

        elif 'open netflix' in query:
            url = "https://www.netflix.com/browse"
            webbrowser.get(browser_path).open(url)

        elif 'open youtube' in query:
            url = "https://youtube.com/"
            webbrowser.get(browser_path).open(url)
        
        elif 'open whatsapp' in query:
            url = "https://web.whatsapp.com/"
            webbrowser.get(browser_path).open(url)

        elif 'open code' in query or 'run code' in query or 'open visual studio code' in query or 'run visual studio code' in query:
            try:
                os.startfile(visual_studio_code_path)
            except:
                say("i can't find the executable file")

        elif 'open steam' in query or 'run steam' in query :
            try:
                os.startfile(steam_path)
            except:
                speak("i can't find the executable file")
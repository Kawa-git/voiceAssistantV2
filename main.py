import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import wolframalpha #pip install wolframalpha
import os

browser_path ='C://Program Files//Mozilla Firefox//firefox.exe %s'
visual_studio_code_path = 'F:\\VisualStudioCode\\Code.exe'
terminal_path = 'C:\\Windows\\System32\\cmd.exe'
steam_path =None

ClinteWolfram = wolframalpha.Client("487PW2-38VPTQHH4R")
print("Initializing jarvis")
outputWolfram =''

#Pronounces the string which is passed to it
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) #voices[0] is italian voice, [1] english voice
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
        speak("Buon giorno"+MASTER)
    elif hour>=12 and hour<18:
        speak("Buon pomeriggio"+MASTER)
    else:
        speak("Buona Sera"+MASTER)
    
    speak("Sono Jarvis, come posso aiutarti?")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='it')
        print("user said:  "+query)
    except Exception as e:
        print("Say that again please")
        query=''
    return query.lower()

wishMe()

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

        elif 'firefox' in query or 'duckduckgo' in query:
            url = "https://duckduckgo.com/"
            webbrowser.get(browser_path).open(url)

        elif 'amazon' in query:
            url = "www.amazon.com"
            webbrowser.get(browser_path).open(url)

        elif 'netflix' in query:
            url = "https://www.netflix.com/browse"
            webbrowser.get(browser_path).open(url)

        elif 'youtube' in query:
            url = "https://youtube.com/"
            webbrowser.get(browser_path).open(url)
        
        elif 'whatsapp' in query:
            url = "https://web.whatsapp.com/"
            webbrowser.get(browser_path).open(url)

        elif 'apri code' in query or 'lancia could' in query or 'could' in query or 'visual studio' in query or 'cod' in query:
            try:
                os.startfile(visual_studio_code_path)
            except:
                say("Non trovo il file eseguibile")

        elif 'lancia steam' in query or 'steam' in query :
            try:
                os.startfile(steam_path)
            except:
                speak("Non trovo il file eseguibile")
            
        elif 'terminale' in query or 'cmd' in query or'prompt' in query :
            try:
                os.startfile(terminal_path)
            except:
                speak("Non trovo il file eseguibile")

        elif 'shutdown' in query:
            speak('Arrivederci')
            exit()
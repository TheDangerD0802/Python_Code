import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import webbrowser as wb
import os
engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)

def wish():
    speak("Welcome Sunanda Maam")
    speak("Abhi time ho raha hai ")
    time()
    speak("aj ki date ")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6and hour<12:
        speak("Good Morning Ishika")
    elif hour >= 12 and hour <18:
        speak("Good afternoon sunanda")
    elif hour >= 18 and hour < 24:
        speak("Good evening sir ")
    else:
        speak("Good Night Sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizning..")
        query = r.recognize_google(audio, language="en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com','abc123')
    server.sendmail('abc@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    # wish()
    while True:
        query = takeCommand().lower()
        if "time" in query:
            time()
        elif 'date' in query:
            date()
        elif 'wikipedia' in query:
            speak("Searching ....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query, sentences=2)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What should I say? ")
                content = takeCommand()
                to = 'jainanshi735@gmail.com'
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Unable to send email")
        elif 'search in chrome' in query:
            speak("What should i search ?")
            chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'
            search = takeCommand().lower()
            wb.get(chromepath).open_new_tab(search+".com")
        elif 'logout' in query:
            os.system("shutdown /s /t 1")
        elif 'play songs' in query:
            songs_dir = 'E:\PERSONAL\Music\music favourite'
            os.startfile(os.path.join((songs_dir, songs[0])))
        elif 'remember that' in query:
            speak("What should i remember")
            data = takeCommand()
            speak("you said to me "+data)
            remember = open('data.txt','w')
            remember.write(data)
            remember.close()
        elif 'offline' in query:
            quit()

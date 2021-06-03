import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1],id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else:
        speak("Good evening")
    speak("I am Jarvis. Please Sir tell me how may I Help You")
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that Again please...")
        return "None"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('akash630gupta@gmail.com','62akash.Gmail')
    server.sendmail('akash630gupta@gmail.com',to,content)
    server.close()
if __name__ == '__main__':
    wishMe()
    while True:
        query=takeCommand().lower()



        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\songs'
            song=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,song[0]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, Time is {strTime}")

        elif 'open pycharm' in query:
            path ="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2020.3.3\\bin\\pycharm64.exe"
            os.startfile(path)
        elif 'email to akash' in query:
            try:
                speak("What Should I say?")
                content=takeCommand()
                to="akash630gupta@gmail.com"
                sendEmail(to,content)
                speak("Email has bee sent")
            except Exception as e:
                print(e)
                speak("Sorry Akash . I am not able to send this email")

        elif 'quit' in query:
            speak("Have a good day Sir...Bye")
            exit()
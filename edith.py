import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import subprocess
import cv2
from loc import *
import pyautogui
import pyjokes
from voice_command_game import game

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        speak("Listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1 
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n") 
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query

#funtion starts
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning!")
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        print("Good Afternoon")
        speak("Good Afternoon!")
    else:
        print("Good Evening")
        speak("Good Evening!")
    print("I am Edith. Please tell me how may I help you")
    speak("I am Edith. Please tell me how may I help you")


def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('shubhamkumar@gmail.com','password')
    server.sendmail('Receiver@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        #logic for executing tasks based on query
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'what can you do' in query:
            print("Below are the features of me that is Edith")
            speak("Below are the features of me sir")
            print('''1.Search anything in wikipedia\n2.Open browser and google\n3.Music\n4.Send email\n
                  5.Detects your face\n6.opens internal application\n7.About Collge\n8.Play game\n
                  9.opens camera for you\n10.Weather details\n11.location details\n12.It can take screenshots\n
                  13.Share jokes\n14.switches off your pc\n15.you can switch me off by commanding quit.''')   
            speak('''Search anything in wikipedia\nOpen browser and google\nPlay Music\nSend email\n
                  Detects your face\nopens internal application\nAbout Collge\nPlay game\n
                  opens camera for you\nWeather details\nlocation details\nIt can take screenshots\n
                  Share jokes\nswitches off your pc\nyou can switch me off by commanding quit.''')
         
            
        elif 'how are you' in query:
            print("I am fine How are you")
            speak("I am fine How are you")
       
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\Music'            #location of music folder
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath="C:\\vs code\\Code.exe"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say")
                content = takeCommand()
                speak("Who is the Reciever")
                reciever = takeCommand()
                to= reciever
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend . I am not able to send this email at the moment...")

        elif 'hello' in query:
            print("hello")
            speak("hello")

        elif 'about the college' in query:
            print("Name of the college is Bengal College of Engineering and Technology. It is situated in Durgapur, West Bengal.")
            speak("Name of the college is Bengal College of Engineering and Technology. It is situated in Durgapur, West Bengal.")
            speak("Do you want to know about the CSE Department of this College")
            answer=takeCommand()
            if 'no' in answer:
                speak("Ok Sir")
            elif 'yes' in answer:
                print("Name of the HOD is Sk Abdul Rahim.")
                speak("Name of the head of department is Sk Abdul Rahim.")
                print("Names of cse faculties are Prasenjit maji biswajit gope ")
                speak("Names of cse faculties are Prasenjit maji biswajit gope ")
        
        elif 'open notepad plus plus' in query:
            speak("Opening Notepad plus plus")
            codePath="C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
            os.startfile(codePath)

        elif 'open windows player' in query:
            codePath="C:\\Program Files (x86)\\Windows Media Player\\wmplayer.exe"
            os.startfile(codePath)

        elif 'open notepad' in query:
            speak("Opening notepad")
            subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

        elif 'calculator' in query:
            speak("Opening Calculator")
            subprocess.Popen('C:\\Windows\\System32\\calc.exe')

        elif 'open camera' in query:
            speak("Opening Camera")
            cap=cv2.VideoCapture(0)
            while True:
                ret,img=cap.read()
                cv2.imshow('webcam',img)
                k=cv2.waitKey(10)
                if k==27:
                    break
                
            cap.release()
            cv2.destroyAllWindows()

        elif 'game' in query:
            speak("Opening Game")
            game()

        elif 'weather condition' in query:
            speak("Showing Weather Conditions")
            weather()

        elif 'location' in query:
            speak("Showing your current location")
            location()

        elif 'detect face' in query:
            import facial_recognition1
        
        elif 'dictionary' in query:
            speak("Opening Dictionary")
            import English_teasure
            speak("Dictionary closed")

                
        elif 'switch off the pc' in query:
            #import final
            speak("Do you want to shutdown your computer sir?")
            command= takeCommand()
            if "no" in command:
                speak("Thanks sir i will not shut down the computer")
            elif "yes" in command:
                speak("shutting down the computer")
                #os.system("shutdown //s //t 0")
                os.system('shutdown -s')
                
        elif 'screenshot' in query:
            speak("Taking a screenshot")
            img = pyautogui.screenshot()
            img.save(r"C:\Users\shubh\Desktop\edith_project\screenshot.png")
            speak("Screenshot taken")

        elif 'jokes' in query:
            for i in range(5):
                speak(pyjokes.get_jokes()[i])

        elif 'shopping' in query:
            print("From which site you want to shop ?")
            speak("From which site you want to shop ")
            speak(" Flipkart or Amazon or Myntra")
            site=takeCommand()
            print("Opening your shopping site....")
            speak("Opening your shopping site")
            if 'flipkart' in site:
                webbrowser.open("flipkart.com")
            elif 'amazon' in site:
                webbrowser.open("amazon.com")
            elif 'myntra' in site:
                webbrowser.open("myntra.com")
            else:
                speak("Sorry sir your requesting website can't be open.")
                speak("Thank You")
                
        elif 'exit' in query:
            speak("Edith is now switching off")
            exit()
        

import json
from difflib import get_close_matches
import pyttsx3
import speech_recognition as sr

data = json.load(open("data.json"))

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) #to know the voice name
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def takeCommand():
    #it takes microphone input from the user and returns string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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
        return "None"
    return query

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    
    elif w.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[w.title()]

    elif w.upper() in data: #in case user enters words like USA or NATO
        return data[w.upper()]

    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did you mean %s instead?\nEnter Y if yes or N if No: " %
                   get_close_matches(w, data.keys())[0])
        yn = yn.lower()

        if yn == "y":
            return data[get_close_matches(w, data.keys())[0]]

        elif yn == "n":
            return "The word doesn't exists please double check it"

        else:
            return "We didn't undestand your query"

    else:
        return "The word doesn't exists please double check it"


#word = input("Enter the word: ")
speak("Enter the word")
word = takeCommand()
#print(translate(word))
'''for item in translate(word):  #to remove list
    print(item)'''

output = translate(word)
if type(output) == list:
    for item in output :
        print(item)
        speak(item)
    import edith
    
else:
    print(output)
    speak(output)
    import edith

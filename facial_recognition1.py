from cv2 import cv2
import numpy as np
import pyttsx3
import speech_recognition as sr


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
        speak("Listening")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=1 
        audio=r.listen(source)

    try:
        print("Recognizing...")
        speak("Recognizing")
        query= r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n") 
    except Exception as e:
        print(e)
        print("Say that again please...")
        speak("Say that again please")
        return "None"
    return query
    
face_classifier = cv2.CascadeClassifier(r'C:\python_files\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
def face_extractor(img):
    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    if faces is():
        return None
    
    for(x,y,w,h) in faces:
        cropped_faces =img[y:y+h, x:x+w]
    return cropped_faces



cap= cv2.VideoCapture(0)
count= 0

while True:
    ret,frame=cap.read()
    if face_extractor(frame) is not None:
        count+=1
        face = cv2.resize(face_extractor(frame),(400,400))
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

        file_name_path = 'C:/Jarvis/faces/face'+str(count)+'.jpg'
        cv2.imwrite(file_name_path,face)

        cv2.putText(face, str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper',face)
    else:
        speak('Face not found.')
        #print('Face not found')
        pass
    if cv2.waitKey(1)==13 or count==15:
        print("Face Detected Successfully.Now you can work further.")
        speak("Face Detected Successfully.Now you can work further.")
        break
cap.release()
cv2.destroyAllWindows()
#print('Collecting Samples Complete!!!')

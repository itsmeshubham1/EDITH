import pyttsx3
import speech_recognition as sr
import random

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takecommand():
    # It takes microphone input from user and return output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        speak("Listening")
        r.pause_threshold = 0.8
        r.energy_threshold = 300
        r.adjust_for_ambient_noise(source,duration=1)
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f'you said: {query}')

    except Exception as e:
        print("Sorry can't able to recognize")
        return  # returning none string

    return query

def game():
    lst = ["snake", "water", "gun"]
    choice = 5
    left_choice = 0
    your_score = 0
    computer_score = 0
    speak("Hello sir myself EDITH")
    speak("I am your competitor.")
    speak("welcome to snake-water-gun game")
    speak(f"you have total {choice} turns.")

    while(left_choice < choice):
        speak("Please choose only one from them")
        speak("Snake or Water or Gun")
        i = takecommand()
        j = random.choice(lst)

        if i == j:
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Oops we both asume same, no one won this turn.")
            speak( f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}")

        elif i == 'snake' and j == 'water':
            your_score = your_score+1
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Snake drink the water. Nice you won this turn")
            speak("This time you got 1 point")
            speak( f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}")

        elif i == 'snake' and j == 'gun':
            computer_score = computer_score+1
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Snake killed by gun shot. Oops you loose this turn.")
            speak("This time i got 1 point")
            speak(f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}")

        elif i == 'water' and j == 'gun':
            your_score = your_score+1
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Gun damaged due to water. Nice You won this turn")
            speak("This time You got 1 point")
            speak(f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}")

        elif i == 'water' and j == 'snake':
            computer_score = computer_score+1
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Snake drink the whole water. Oops you losse this turn.")
            speak("This time i got 1 point")
            speak(f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}\n")

        elif i == 'gun' and j == 'snake':
            your_score = your_score+1
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Snake kill by gun shot. Nice you won this turn.")
            speak("This time you got 1 point")
            speak(f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}")

        elif i == 'gun' and j == 'water':
            computer_score = computer_score+1
            speak(f"your guess was:{i} and my guess was:{j}")
            speak("Gun damage due to water. Oops you loose this turn.")
            speak("This time i got 1 point")
            speak(f"Your score is {your_score} and my score is {computer_score}")
            speak(f"available turn is: {choice-left_choice-1}")

        else:
            speak("Sorry cant recognised this time.")
            speak(f"available turn is: {choice-left_choice-1}")

        left_choice = left_choice+1

    speak("The match is over and you are really a tough competitor.")
    speak("Please wait for a moment i am calculating the final result.")

    if computer_score == your_score:
        speak(f"your total score is: {your_score} and my total score is: {computer_score}")
        speak("We both score same.")
        speak("No one won this game.")

    elif computer_score > your_score:
        speak(f"your total score is: {your_score} and my total score is: {computer_score}")
        speak("I won this time.")
        speak("Sorry you loose this game.")

    else:
        speak(f"your total score is: {your_score} and my total score is: {computer_score}")
        speak("You rock this time.")
        speak("Congrats you are the winner")

    speak("Hope you enjoy this game.")

    speak("Did you want to play again?")
    speak("say yes or no")
    query= takecommand()
    if(query=='yes'):
        game()
    else:
        speak("Thank you")
        exit()



# if __name__ == "__main__":
#     game()
    
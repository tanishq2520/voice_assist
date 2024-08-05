import pyttsx3 as p
import speech_recognition as sr
from selenium_web import infow
from YT_auto import Music
from News import news
import randfacts
from jokes import joke
from weather import *
import datetime

engine = p.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        return "Good Morning"
    elif hour >= 12 and hour < 16:
        return "Good Afternoon"
    else:
        return "Good Evening"

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        audio = r.listen(source)
        text = r.recognize_google(audio)
        return text.lower()

# Greeting and initial query
today_date = datetime.datetime.now()

speak(f"Hello sir, {wishme()}, I am your voice assistant.")
speak(f"Today is {today_date.strftime('%d')} of {today_date.strftime('%B')} and it's currently {today_date.strftime('%I:%M %p')}.")
speak("Temperature in, Panipat is " + str(temp(get_weather_data())) + " degree celsius and with " + des(get_weather_data())) 
speak(". How can I help you ,sir?")

while True:
    text2 = recognize_speech()
    print(text2)

    if "information" in text2:
        speak("You need information related to which topic?")
        infor = recognize_speech()
        print(f"Searching {infor} in Wikipedia")
        speak(f"Searching {infor} in Wikipedia")
        assist = infow()
        assist.get_info(infor)

    elif "play" in text2 or "video" in text2:
        speak("Which video do you want to play?")
        vid = recognize_speech()
        print(f"Playing {vid} on YouTube")
        speak(f"Playing {vid} on YouTube")
        assist = Music()
        assist.play(vid)

    elif "news" in text2:
        print("Sure sir, now I will read news for you.")
        speak("Sure sir, now I will read news for you.")
        arr = news()
        for i in range(len(arr)):
            print(arr[i])
            speak(arr[i])

    elif "fact" in text2 or "facts" in text2:
        print("Sure sir, here is a fact for you.")
        speak("Sure sir, here is a fact for you.")
        fact = randfacts.get_fact()
        print(fact)
        speak("Did you know that " + fact)

    elif "joke" in text2 or "jokes" in text2:
        print("Sure sir, get ready for some chuckles.")
        speak("Sure sir, get ready for some chuckles.")
        arr = joke()
        joke_data = arr[0]
        setup = joke_data["setup"]
        punchline = joke_data["punchline"]
        print(setup)
        speak(setup)
        print(punchline)
        speak(punchline)

    # Add a condition to break the loop if the user wants to stop the assistant
    elif "stop" in text2 or "exit" in text2:
        speak("Goodbye, sir!")
        break

    else:
        speak("I didn't understand that. Can you please repeat?")

import tkinter as tk
from PIL import Image, ImageTk
import pyttsx3 as p
import speech_recognition as sr
import datetime
from selenium_web import infow
from YT_auto import Music
from News import news
import randfacts
from jokes import joke
from weather import *
from search import search_google
import threading
import sys

# Initialize the Tkinter window
window = tk.Tk()
window.title("Voice Assistant")
window.geometry("720x907")

# Create a Canvas widget
canvas = tk.Canvas(window, width=720, height=907)
canvas.pack(fill="both", expand=True)

# Load the background image
try:
    bg_image_path = "Anime.jpeg"
    bg_image = Image.open(bg_image_path)
    bg_image = bg_image.resize((720, 907), Image.LANCZOS)
    bg_image_tk = ImageTk.PhotoImage(bg_image)
    
    canvas.create_image(0, 0, anchor=tk.NW, image=bg_image_tk)
except Exception as e:
    print(f"Error loading background image: {e}")

# Create a text area for dialogue on the canvas
dialog_area = tk.Label(canvas, bg='light grey', fg='black', font=('Arial', 12), padx=10, pady=10, wraplength=680, relief=tk.RAISED, bd=2)
dialog_area.place(relx=0.5, rely=0.5, anchor='center')

# Create a label for "listening..." status
status_label = tk.Label(canvas, text="Listening...", bg='light grey', font=('Arial', 12))
status_label.place(relx=0.5, rely=0.4, anchor='center')

# Initialize text-to-speech engine
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
        greeting = "Good Morning"
    elif hour >= 12 and hour < 16:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"
    
    weather_info = get_weather_data()
    temperature = temp(weather_info)
    description = des(weather_info)
    weather_details = f"Current temperature is {temperature} degrees Celsius. Weather description is {description}."
    
    return f"Hello Sir, I am your voice assistant. {greeting}. {weather_details}"

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source, 1.2)
        print("Listening...")
        status_label.config(text="Listening...")
        window.update_idletasks()
        audio = r.listen(source)
        text = r.recognize_google(audio)
        status_label.config(text="Processing...")
        window.update_idletasks()
        return text.lower()

def update_dialog(text):
    dialog_area.config(text=text)
    window.update_idletasks()

def close_window():
    window.destroy()
    sys.exit()

def handle_recognition():
    global stop_listening
    stop_listening = False
    while not stop_listening:
        text2 = recognize_speech()
        update_dialog(f"You said: {text2}")
        try:
            if "information" in text2:
                speak("You need information related to which topic?")
                update_dialog("You need information related to which topic?")
                infor = recognize_speech()
                update_dialog(f"Searching {infor} in Wikipedia")
                speak(f"Searching {infor} in Wikipedia")
                assist = infow()
                assist.get_info(infor)

            elif "search" in text2 or any(keyword in text2 for keyword in ["who is", "what is", "when", "where", "why", "meaning of"]):
                query = text2
                update_dialog(f"Searching {query} on Google")
                speak(f"Searching {query} on Google")
                search_google(query)

            elif "play" in text2 or "video" in text2:
                speak("Which video do you want to play?")
                update_dialog("Which video do you want to play?")
                vid = recognize_speech()
                update_dialog(f"Playing {vid} on YouTube")
                speak(f"Playing {vid} on YouTube")
                assist = Music()
                assist.play(vid)

            elif "news" in text2:
                speak("Sure sir, now I will read news for you.")
                update_dialog("Sure sir, now I will read news for you.")
                arr = news()
                for i in range(len(arr)):
                    update_dialog(f"News {i+1}: {arr[i]}")
                    speak(arr[i])

            elif "fact" in text2 or "facts" in text2:
                speak("Sure sir, here is a fact for you.")
                update_dialog("Sure sir, here is a fact for you.")
                fact = randfacts.get_fact()
                update_dialog(f"Did you know that {fact}")
                speak("Did you know that " + fact)

            elif "joke" in text2 or "jokes" in text2:
                speak("Sure sir, get ready for some chuckles.")
                update_dialog("Sure sir, get ready for some chuckles.")
                arr = joke()
                joke_data = arr[0]
                setup = joke_data["setup"]
                punchline = joke_data["punchline"]
                update_dialog(f"Joke setup: {setup}")
                speak(setup)
                update_dialog(f"Joke punchline: {punchline}")
                speak(punchline)

            elif "stop" in text2 or "exit" in text2:
                speak("Goodbye, sir!")
                update_dialog("Goodbye, sir!")
                close_window()  # Close the window and exit

            else:
                speak("I didn't understand that. Can you please repeat?")
                update_dialog("I didn't understand that. Can you please repeat?")

        except Exception as e:
            print(f"An error occurred: {e}")
            update_dialog(f"An error occurred: {e}")

# Initialize stop listening flag
stop_listening = False

# Run the speech recognition handling in a separate thread
thread = threading.Thread(target=handle_recognition)
thread.start()

# Initial greeting
update_dialog(wishme())
speak(wishme())

# Run the Tkinter main loop
window.mainloop()

# Ensure the thread stops when the window is closed
stop_listening = True
thread.join()

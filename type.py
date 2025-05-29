import speech_recognition as sr
import pyautogui
import time


def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 0.5
        recognizer.energy_threshold = 300
        audio = recognizer.listen(source, timeout=5)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Could not understand, please say that again.")
        return "None"
    return query


def typeText(text):
    pyautogui.typewrite(text)


def pressEnter():
    pyautogui.press("enter")


def search(query):
    # Open browser and perform search (YouTube or Google)
    pyautogui.hotkey('ctrl', 't')  # Open a new tab
    time.sleep(1)
    pyautogui.typewrite("https://www.google.com/search?q=" + query)  # Google search URL
    pyautogui.press("enter")
    time.sleep(2)  # Wait for the page to load
    pyautogui.press("enter")  # Confirm the search or open the first result if needed

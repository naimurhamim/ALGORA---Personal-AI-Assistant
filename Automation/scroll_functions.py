import pyautogui
import pyttsx3
from feature.coustom_voice import speak

engine = pyttsx3.init('sapi5')

'''def speak(text):
    engine.say(text)
    engine.runAndWait()'''

def scroll_up():
    pyautogui.scroll(500)

def scroll_down():
    pyautogui.scroll(-500)
def scroll_to_top():
    pyautogui.hotkey('home')
    speak("Scrolling to top")

def scroll_to_bottom():
    pyautogui.hotkey('end')
    speak("Scrolling to bottom")

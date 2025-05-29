import webbrowser
import requests
from Automation.Web_Data import websites
from Automation.Youtube_play_back import volume_up, volume_down, seek_forward, seek_backward, seek_forward_10s, \
    seek_backward_10s, seek_backward_frame, seek_forward_frame, seek_to_beginning, seek_to_end, \
    seek_to_previous_chapter, seek_to_next_chapter, decrease_playback_speed, increase_playback_speed, \
    move_to_next_video, move_to_previous_video
from feature.coustom_voice import speak
from Automation.tab_automation import open_new_tab, close_tab, open_browser_menu, zoom_in, zoom_out, refresh_page, \
    switch_to_next_tab, switch_to_previous_tab, open_history, open_bookmarks, go_back, go_forward, open_dev_tools, \
    toggle_full_screen, open_private_window
from type import typeText, search
import time
import pyttsx3
import keyboard
import datetime
import pyautogui
from datetime import datetime
import speech_recognition as sr
import subprocess as sp
import imdb
import wolframalpha
from decouple import config
from random import choice
from conv import random_txt
from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, send_email, get_news, weather_forecast
from Automation.scroll_functions import scroll_up, scroll_down, scroll_to_top, scroll_to_bottom
from image_generator import generate_image
import sys
import os
from sklearn.metrics import accuracy_score
import getpass
from feature.mistrail_ai_chat import generate, clean_response
from Brain.brain import Main_Brain



########################################### accuracy ############################################
successful_commands = 0
failed_commands = 0

def calculate_accuracy():
    global successful_commands, failed_commands
    total_commands = successful_commands + failed_commands
    if total_commands > 0:
        accuracy = (successful_commands / total_commands) * 100
        print(f"Accuracy: {accuracy:.2f}%")
        speak(f"Current accuracy is {accuracy:.2f} percent.")
    else:
        print("No commands executed yet.")
        speak("No commands executed yet.")

def log_command_result(success):
    global successful_commands, failed_commands
    if success:
        successful_commands += 1
    else:
        failed_commands += 1
##########################################################################################

stdout_backup = sys.stdout
sys.stdout = open(os.devnull, 'w')

sys.stdout.close()
sys.stdout = stdout_backup

random_speech_enabled = False

for i in range(3):
    speak("Enter password to open Algora")
    a = getpass.getpass("Enter Password to open ALGORA :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a == pw):
        print("WELCOME SIR ! PLZ PRESS CTRL+ALT+A TO LOAD ME UP")
        break
    elif (i == 2 and a != pw):
        exit()
    elif (a != pw):
        speak("Wrong Password, try again!")
        print("Try Again")

'''
#GUI:
from INTRO import play_gif

play_gif

'''



engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 175)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        engine.endLoop()
        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"Error in speech: {e}")


USER = config('USER')
HOSTNAME = config('BOT')




def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour > 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"Welcome, This is {HOSTNAME}. Please enter CTRL+ALT+A to load me up, {USER}")


listening = False


def start_listening():
    global listening
    listening = True
    print("started listening")
    speak("started listening")


def pause_listening():
    global listening
    listening = False
    print("stopped listening")
    speak("stopped listening")


keyboard.add_hotkey('ctrl+alt+a', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


def introduction():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour > 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak("Hello! I am ALGORA, your personal AI assistant, created by team ALGOGEN. \
          I can help with a variety of tasks, such as managing your schedule, providing the latest news,\
              answering questions, and even opening applications.Just tell me what you'd like to do, and I'll take care of the rest!")

def take_command():
    global successful_commands, failed_commands
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing......")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        successful_commands += 1  # Increment successful command count

        if not 'stop' in queri or 'exit' in queri:
            if random_speech_enabled:
                speak(choice(random_txt))
        else:
            hour = datetime.now().hour
            if (hour >= 21) and (hour < 6):
                speak(f"Good night sir, take care!")
            else:
                speak("It was a pleasure assisting you today! Have a good day, sir.")
            exit()
    except Exception:
        failed_commands += 1
        speak("Sorry I couldn't understand. Can you please repeat that sir?")
        queri = 'None'
    return queri

"""
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing......")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            if random_speech_enabled:
                speak(choice(random_txt))
        else:
            hour = datetime.now().hour
            if (hour >= 21) and (hour < 6):
                speak(f"Good night sir, take care!")
            else:
                speak("It was a pleasure assisting you today! Have a good day, sir.")
            exit()
    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that sir?")
        queri = 'None'
    return queri
    
    """


def openweb(webname):
    website_name = webname.lower().split()
    counts = {}
    for name in website_name:
        counts[name] = counts.get(name, 0) + 1
    urls_to_open = []
    for name, count in counts.items():
        if name in websites:
            urls_to_open.extend([websites[name]] * count)
    for url in urls_to_open:
        webbrowser.open(url)
    if urls_to_open:
        print("opening...")


if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            try:
                query = take_command().lower()

                if "hello" in query :
                    speak("Hello sir, how are you ?")
                elif "what are you doing now" in query:
                    speak("I am working to improve myself, sir")
                elif "i am fine and you" in query or "i am fine what about you" in query:
                    speak("Perfect, sir")
                elif "thank you" in query:
                    speak("you are welcome, sir")
                # change password:
                elif "change password" in query:
                    random_speech_enabled = True
                    speak("What's the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt", "w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"Your new password is {new_pw}")

                elif "introduce yourself" in query:
                    speak(introduction())

                elif "open command prompt" in query:
                    speak("Opening command prompt")
                    os.system('start cmd')

                elif "open camera" in query:
                    speak("Opening camera sir")
                    sp.run('start microsoft.windows.camera:', shell=True)

                elif "open notepad" in query:
                    speak("Opening Notepad for you sir")
                    notepad_path = "C:\\Windows\\notepad.exe"
                    sp.run(notepad_path)

                elif "open browser" in query:
                    speak("Sure, Opening browser for you sir")
                    browser_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
                    sp.run(browser_path)

                elif "show ip address" in query:
                    ip_address = find_my_ip()
                    speak(f"your ip address is {ip_address}")
                    print(f"Your IP address is {ip_address}")

                elif "open youtube" in query:
                    speak("What do you want to play on youtube sir?")
                    video = take_command().lower()
                    youtube(video)

                elif "open google" in query:
                    speak(f"What do you want to search on google sir, {USER}?")
                    query = take_command().lower()
                    search_on_google(query)

                elif "i want to know about" in query or "tell me about" in query or "what is" in query or "who is" in query or "which is" in query:
                    search = take_command().lower()
                    results = search_on_wikipedia(search)
                    speak(f"According to wikipedia,{results}")
                    speak("I am printing in on terminal")
                    print(results)
                    
                elif "open wikipedia" in query :
                    speak("What do you want to search on wikipedia sir?")
                    search = take_command().lower()
                    results = search_on_wikipedia(search)
                    speak(f"According to wikipedia,{results}")
                    speak("I am printing in on terminal")
                    print(results)

                elif "send an email" in query:
                    speak("On what email do you want to send sir? Please enter in the terminal")
                    receiver_add = input("Email Address: ")
                    speak("What should be the subject sir?")
                    subject = take_command().capitalize()
                    speak("What is the message?")
                    message = take_command().capitalize()
                    if send_email(receiver_add, subject, message):
                        speak("I have sent the email sir")
                        print("I have sent the email sir")
                    else:
                        speak("something went wrong. Please check the error log")

                elif "news" in query:
                    speak(f"I am reading out the latest headline of today, sir")
                    speak(get_news())
                    speak("I am printing it on screen sir")
                    print(*get_news(), sep='\n')

                elif "weather" in query:
                    ip_address = find_my_ip()
                    speak("Tell me the name of your city.")
                    city = take_command().lower()
                    speak(f"Getting weather report of your city {city}")
                    weather, temp, feels_like = weather_forecast(city)
                    speak(f"The current temperature is {temp}, but it feels like {feels_like}")
                    speak(f"Also the weather report talks about {weather}")
                    speak("I am printing weather info on screen")
                    print(f"Description: {weather}\n Temperature: {temp}\n Feels like: {feels_like}")

                elif "movie" in query:
                    movies_db = imdb.IMDb()
                    speak("Please tell me the movie or series name:")
                    text = take_command()
                    movies = movies_db.search_movie(text)
                    speak("searching for " + text)
                    speak("I found these")
                    for movie in movies:
                        title = movie["title"]
                        year = movie["year"]
                        speak(f"{title}-{year}")
                        info = movie.getID()
                        movie_info = movies_db.get_movie(info)
                        rating = movie_info["rating"]
                        cast = movie_info["cast"]
                        actor = cast[0:5]
                        plot = movie_info.get('plot outline', 'plot summary nor available')
                        speak(
                            f"{title} was released in {year} has imdb rating of {rating}. it has a cast of {actor}. The plot of summary of movie is {plot}")
                        print(
                            f"{title} was released in {year} has imdb rating of {rating}. it has a cast of {actor}. The plot of summary of movie is {plot}")

                elif "calculate" in query:
                    app_id = "GHGKAX-L7LUVXGTL6"
                    client = wolframalpha.Client(app_id)
                    ind = query.lower().split().index("calculate")
                    text = query.split()[ind + 1:]
                    result = client.query(" ".join(text))
                    try:
                        ans = next(result.results).text
                        speak("The answer is " + ans)
                        print("The answer is " + ans)
                    except StopIteration:
                        speak("I couldn't find that.Please try again")

                elif "what is" in query:
                    app_id = "GHGKAX-L7LUVXGTL6"
                    client = wolframalpha.Client(app_id)
                    try:
                        ind = query.lower().index('what is') if 'what is' in query.lower() else \
                            query.lower().index('who is') if 'who is' in query.lower() else \
                                query.lower().index('which is') if 'which is' in query.lower() else None

                        if ind is not None:
                            text = query.split()[ind + 2:]
                            result = client.query(" ".join(text))
                            ans = next(result.results).text
                            speak("The answer is " + ans)
                            print("The answer is " + ans)
                        else:
                            speak("I could not find that sir.")

                    except StopIteration:
                        speak("I couldn't find that.Please try again")


                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("algora", "")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.press("enter")

                elif "close this tab" in query:
                    pyautogui.hotkey('alt', 'f4')

                elif "the time" in query:  #problem found
                    strTime = datetime.datetime.now().strftime("%H:%M")
                    speak(f"Sir, the time is {strTime}")
                #YoutubeControl:
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                elif "volume up" in query:
                    from Automation.keyboards import volumeup

                    speak("Turning volume up,sir")
                    volumeup()
                elif "volume down" in query:
                    from Automation.keyboards import volumedown

                    speak("Turning volume down, sir")
                    volumedown()

                elif "whatsapp" in query:
                    random_speech_enabled = True
                    from Whatsapp import sendMessage

                    sendMessage()

                elif "shutdown the system" in query:
                    speak(
                        "Are you sure you want to shut down the system? Please say 'yes' or 'no'.")
                    shutdown = take_command().lower()
                    if "yes" in shutdown:
                        speak(
                            "Shutting down in 10 seconds.")
                        os.system("shutdown /s /t 10")
                    elif "no" in shutdown:
                        speak("Shutting down the system is cancelled.")
                    else:
                        speak(
                            "Sorry, I didn't understand your response. Please say 'yes' if you want to shutdown or 'no' to cancel.")

                #Screenshot
                elif "screenshot" in query:
                    random_speech_enabled = True
                    directory = r"C:\Users\Naim\Pictures\Screenshots"
                    if not os.path.exists(directory):
                        os.makedirs(directory)
                    timestamp = time.strftime("%Y%m%d-%H%M%S")
                    file_path = os.path.join(directory, f"algora_{timestamp}.jpg")
                    im = pyautogui.screenshot()
                    im.save(file_path)
                    speak("Screenshot taken and saved.")


                #Photoclick
                elif "click my photo" in query or "take my photo" in query or "take a photo" in query or "click a photo" in query:
                    random_speech_enabled = True
                    import time
                    pyautogui.press("super")
                    pyautogui.typewrite("camera")
                    pyautogui.press("enter")
                    time.sleep(2)
                    speak("SMILE")
                    pyautogui.press("enter")
                    time.sleep(1)
                    speak("Photo taken and saved to Camera Roll.")


                elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("algora", "")
                    query = query.replace("translate", "")
                    translategl(query)

                elif "type" in query:
                    text_to_type = query.replace("type", "").strip()
                    speak(f"Typing {text_to_type}")
                    typeText(text_to_type)

                elif "search" in query:
                    speak("What do you want to search for?")
                    search_query = take_command().lower()
                    if search_query and search_query != "none":
                        search(search_query)
                        speak(f"Searching for {search_query}")
                    else:
                        speak("I didn't hear what you want to search for. Please try again.")

                elif "enter" in query:
                    speak("Pressing enter")
                    pyautogui.press("enter")

                elif "scroll up" in query:
                    scroll_up()

                elif "scroll down" in query:
                    scroll_down()

                elif "scroll to top" in query:
                    scroll_to_top()
                elif "scroll to bottom" in query:
                    scroll_to_bottom()
#tab automation
                elif "new tab" in query:
                    open_new_tab()
                elif "close tab" in query:
                    close_tab()
                elif "browser menu" in query:
                    open_browser_menu()
                elif "zoom in" in query:
                    zoom_in()
                elif "zoom out" in query:
                    zoom_out()
                elif "refresh page" in query:
                    refresh_page()
                elif "next tab" in query:
                    switch_to_next_tab()
                elif "previous tab" in query:
                    switch_to_previous_tab()
                elif "show history" in query:
                    open_history()
                elif "show bookmarks" in query:
                    open_bookmarks()
                elif "go back" in query:
                    go_back()
                elif "go forward" in query:
                    go_forward()
                elif "show dev tools" in query:
                    open_dev_tools()
                elif "full screen" in query:
                    toggle_full_screen()
                elif "exit full screen" in query:
                    toggle_full_screen()
                elif "private window" in query:
                    open_private_window()

                #Youtube automation:
                elif "forward" in query:
                    seek_forward()
                elif "backward" in query:
                    seek_backward()
                elif "forward 10 seconds" in query:
                    seek_forward_10s()
                elif "backward 10 seconds" in query:
                    seek_backward_10s()
                elif "backward frame" in query:
                    seek_backward_frame()
                elif "forward frame" in query:
                    seek_forward_frame()
                elif " start beginning" in query:
                    seek_to_beginning()
                elif "go to the end" in query:
                    seek_to_end()
                elif "previous chapter" in query:
                    seek_to_previous_chapter()
                elif "next chapter" in query:
                    seek_to_next_chapter()
                elif "decrease speed" in query:
                    decrease_playback_speed()
                elif "increase speed" in query:
                    increase_playback_speed()
                elif "next video" in query:
                    move_to_next_video()
                elif "previous video" in query:
                    move_to_previous_video()


#image generator:
                elif "generate" in query:
                    text_to_generate = query.replace("generate", "").strip()
                    if text_to_generate:
                        timestamp = time.strftime("%Y%m%d-%H%M%S")
                        directory = r'C:\Users\Naim\Pictures\Generated image'
                        filename = f'generated_image_{timestamp}.png'
                        save_path = os.path.join(directory, filename)
                        generate_image(text_to_generate, save_path)
                        speak(f"Image generated for {text_to_generate}")
                        webbrowser.open(save_path)
                    else:
                        speak("Please provide some text to generate an image.")
#open website:
                elif "website" in query:
                    webname = query.replace("web open", "").strip()
                    openweb(webname)
                    speak(f"Opening {webname}")


                elif "accuracy" in query:
                    calculate_accuracy()
                    log_command_result(True)
                
                elif "Algora" in query or "remember" in query:
                    response = Main_Brain(query)
                    speak(response)
                    log_command_result(True)
                
                else:
                    def is_valid_input(query):
                        if len(query.split()) < 2:
                            return False
                        
                        noise_words = ['hmm', 'uhh', 'err', 'ah', 'oh']
                        if any(word in query.lower() for word in noise_words):
                            return False
                            
                        return True

                    try:
                        if is_valid_input(query):
                            response = generate(query)
                            print("Algora:", response)
                            max_chunk_length = 200
                            chunks = [response[i:i+max_chunk_length] for i in range(0, len(response), max_chunk_length)]
                            
                            for chunk in chunks:
                                speak(chunk)
                                time.sleep(0.1)                                
                            log_command_result(True)
                    except Exception as e:
                        print(f"Error: {e}")
                        speak("There was a problem processing your request.")
                        log_command_result(False)
                    


            except Exception as e:
                speak("There's a problem, sir.")
                print(f"Error: {e}")

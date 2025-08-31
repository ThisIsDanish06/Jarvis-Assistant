# Jarvis Personal Assistant

import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
import pygame
import os
import time
from musicLibrary import music
import subprocess
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By



# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
#     client_id="SPOTIFY_CLIENT_ID",
#     client_secret="SPOTIFY_CLIENT_SECRET",
#     redirect_uri="SPOTIFY_REDIRECT_URI",
#     scope="user-modify-playback-state user-read-playback-state"
# ))



# ========================
# Initialization
# ========================
recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "NEWSAPI_KEY"

def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    
    tts = gTTS(text)
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")

driver = webdriver.Chrome()  # Make sure chromedriver is installed and PATH is set

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Create the driver ONCE, globally
driver = webdriver.Chrome()
driver.get("https://www.youtube.com")  # open YouTube on launch

def play_youtube_song(song_name):
    # If not already on YouTube, navigate again
    if "youtube.com" not in driver.current_url:
        driver.get("https://www.youtube.com")
        time.sleep(2)

    # Find and clear the search box
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.clear()
    search_box.send_keys(song_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    # Click first video as before
    videos = driver.find_elements(By.ID, "video-title")
    for video in videos:
        video_title = video.get_attribute("title")
        if video.is_displayed() and video_title:
            video.click()
            break
    else:
        print(f"No playable videos found for {song_name}")

# Use play_youtube_song() for each song request WITHOUT creating new driver!



def open_app(app_name):
    subprocess.run(["open", "-a", app_name])



# ========================
# Command Processing
# ========================
def processCommands(c):
        c_lower = c.lower()
        if "open google" in c.lower():
            webbrowser.open("https://www.google.com")
        elif "open youtube" in c.lower():
            webbrowser.open("https://www.youtube.com")
        elif "open instagram" in c.lower():
            webbrowser.open("https://www.instagram.com")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://www.linkedin.com")
        elif "open facebook" in c.lower():
            webbrowser.open("https://www.facebook.com")
        elif "open amazon" in c.lower():
            webbrowser.open("https://www.amazon.com")
        elif "open flipkart" in c.lower():
            webbrowser.open("https://www.flipkart.com")
        elif "open nykaa" in c.lower():
            webbrowser.open("https://www.nykaa.com")
        elif "open bonkers corner" in c.lower():
            webbrowser.open("https://www.bonkerscorner.com")
        elif "open myntra" in c.lower():
            webbrowser.open("https://www.myntra.com")
        elif "open meesho" in c.lower():
            webbrowser.open("https://www.meesho.com")
        elif "open net mirror" in c.lower():
            webbrowser.open("https://net2025.cc/home")
        elif "open map" in c.lower():
            webbrowser.open("https://www.google.com/maps/@19.0939136,72.8858624,6458m/data=!3m1!1e3?entry=ttu&g_ep=EgoyMDI1MDgyNS4wIKXMDSoASAFQAw%3D%3D")
        elif "open indiamart" in c.lower():
            webbrowser.open("https://www.indiamart.com")
        elif "open roblox" in c_lower:
            speak("Opening Roblox")
            open_app("Roblox")
        elif "open camera" in c_lower:
            speak("Opening Camera")
            open_app("Photo Booth")
        elif "open spotify" in c_lower:
            speak("Opening Spotify")
            open_app("Spotify")
        elif "open whatsapp" in c_lower:
            speak("Opening Whatsapp")
            open_app("WhatsApp")

            # Personal Info
        elif "what is my name" in c_lower:
            speak("Your name is Daanish")
        elif "who am i" in c_lower:
            speak("ou are Daanish. You are 17 years old, currently studying in Mithibai college pursuing Bachelor of Science in statistics and computer science minor. You live in Jarimari, Sakinaka, Mumbai")



        # elif c_lower.startswith("play"):
        #     song_name = c_lower.replace("play", "").strip()
        #     results = sp.search(q=song_name, type="track")
        #     if results ['tracks']['items']:
        #         track_uri = results['tracks']['items'][0]['uri']

        #         sp.start_playback(uris=[track_uri])
        #         speak(f"Playing {song_name} on Spotify")
        #     else:
        #         speak("Song not found on Spotify")



        elif c_lower.startswith("play"):
            song_name = c_lower.replace("play", "").strip()
            play_youtube_song(song_name)
            speak(f"Playing {song_name} on YouTube")








        # elif c_lower.startswith("play"):
        #     song_name = c_lower[5:].replace(" ", "").strip()
        #     for k in music:
        #         if song_name in k.lower().replace(" ", ""):
        #             webbrowser.open(music[k])



        # News
        elif "news" in c.lower():
            r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=NEWSAPI_KEY")
            if r.status_code==200:
                data = r.json()     # parse the json response
                articles = data.get('articles', [])      # extract the articles
            for article in articles:               # Print the headlines
                    speak(article['title'])
        
        else:
            pass

if __name__ == "__main__":



# ========================
# Wake Word Detection
# ========================
    def wake_word_callback(recognizer, audio):
        try:
            text = recognizer.recognize_google(audio)
            print(f"Wake word listening got: {text}")

            if "jarvis" in text.lower():
                speak("Yes sir!")
                # Listen explicitly for command after wake word detection
                with sr.Microphone() as source:
                    print("Listening for command...")
                    command_audio = recognizer.listen(source, timeout=5)
                    command = recognizer.recognize_google(command_audio)
                    print(f"Command: {command}")
                    processCommands(command)
        except Exception as e:
            print(f"Error in wake_word_callback: {e}")



    # ========================
    # Main
    # ========================
    if __name__ == "__main__":
        speak("Initializing Jarvis....")
        r = sr.Recognizer()
        mic = sr.Microphone()

        # Listen in background
        stop_listening = r.listen_in_background(mic, wake_word_callback)

        print("Jarvis is listening for wake word in background...")

        # Keep the program running.
        while True:
            time.sleep(0.1)

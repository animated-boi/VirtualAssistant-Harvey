import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import favMusic
import requests
import openai_client
from openai import OpenAI
import creds


recozniser = sr.Recognizer()
engine = pyttsx3.init(driverName='nsss')
engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')

def speak(text):
    engine.say(text)
    engine.runAndWait()



def processCommand(command):
    command = command.lower()
    if "hello" in command:
        speak("Hello Animesh, how can I assist you today?")
    elif "how are you" in command:
        speak("I am just a program, but thank you for asking!")
    elif "what is your name" in command:
        speak("I am Animo, your personal AI Assistant.")
    elif "goodbye" in command or "exit" in command:
        speak("Goodbye Animesh! Have a great day!")
        exit()
    
    elif "open google" in command:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in command:
        webbrowser.open("https://www.linkedin.com/in/animesh-chaudhary-a98b58125/")

    elif "open github" in command:
        webbrowser.open("https://github.com/animated-boi")
    
    elif command.startswith("play"):
        song = command.split(" ")[1]
        favMusic.playMusic(song)

    elif "news" in command:
        response = requests.get(f"https://newsdata.io/api/1/latest?apikey={creds.key_newsapi}&country=us&prioritydomain=top")
        data = response.json()
        if data.get("status") == "success":
            results = data.get("results", [])
            print("\n📰 Top Headlines:\n")
            for idx, article in enumerate(results, 1):
                speak(f"{idx}. {article.get('title')}")
        else:
            print("Failed to fetch news.")


    else:
        print("Processing command with OpenAI...")
        response = openai_client.aiProcessing(command)
        speak(response)


if __name__ == "__main__":
    speak("Initializing your personal AI Assistant Harvey!")
    # Listening for the wake word "Harvey"
    while True: 
        r = sr.Recognizer()
        
        try:
            with sr.Microphone() as source:
                print("Listening for the wake word 'Harvey'...")
                audio = r.listen(source, timeout=2, phrase_time_limit=3)
            
            # Recognizing the audio
            word = r.recognize_google(audio)
            print(f"Recognized: {word}")
            if("harvey" in word.lower()):
                print("Harvey activated!")
                speak("Yes, how can I assist you?")
                
                with sr.Microphone() as source:
                    print("Harvey listing...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
            
        
        except Exception as e:
            print(f"Error; {e}")




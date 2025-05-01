import webbrowser
import main
# This module contains a dictionary of favorite songs and their corresponding YouTube links.

music = {
    "snowman" : "https://youtu.be/gset79KMmt0?si=VOEhtCtHFxbm_e-3",
    "qismat" : "https://youtu.be/9xVp8m0fJSg?si=w8aM1jO6lZ4cvCBj",
    "fortnight" : "https://youtu.be/q3zqJs7JUCQ?si=TM2o0_MbsgTTX1SE"
}

def playMusic(song):
    if song in music:
        url = music[song]
        webbrowser.open(url)
        main.speak(f"Playing {song} for you.")
    else:
        main.speak("Sorry, I couldn't find that song in my playlist.")


 # song = command.replace("play", "").strip()
        # if song in favMusic.music:
        #     url = favMusic.music[song]
        #     webbrowser.open(url)
        #     speak(f"Playing {song} for you.")
        # else:
        #     speak("Sorry, I couldn't find that song in my playlist.")
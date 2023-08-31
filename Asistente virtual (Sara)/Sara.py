# Asistente virtual de YouTube

import speech_recognition as sr
import pyttsx3, pywhatkit

# Declaracion de variables...

name = "Sara"
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# ...Declaracion de variables

# Funciones...

def talk(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language="es")
        rec = rec.lower()
    except sr.UnknownValueError:
        print("No enendi, intenta de nuevo...")
        if name in rec:
            rec = rec.replace(name, '')
    return rec

def run_Sara():
    while True:
        try:
            rec = listen()
        except UnboundLocalError:
            print("No entendi, intenta de nuevo...")
            continue
        if 'reproduce' in rec:
            music = rec.replace('reproduce', '')
            print("Reproduciendo" + music)
            talk("Reproduciendo" + music)
            # Reproducir musica en youtube con PyWhatKit...
            pywhatkit.playonyt(music)
            # ... Reproducir musica en youtube con PyWhatKit

if __name__ == '__main__':
    run_Sara()
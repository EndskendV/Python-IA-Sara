# Asistente virtual Wiki y Alarma

import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, Sara_RColors, os
from pygame import mixer

# Declaracion de variables...

name = "Sara"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 145)

sites={
                'google' : 'google.com',
                'youtube': 'youtube.com',
                'facebook' : 'facebook.com',
                'whatsapp' : 'web.whatsapp.com',
            }

files = {
    'carta' : 'constancia.pdf',
    'cedula' : 'portada.docx',
    'foto' : 'imagen.jpg'
}

programs = {
    'pluto' : r"C:\Users\jdiaz\Documents\Juegos\plutonium.exe",
    'google' : r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    'opera' : r"C:\Users\jdiaz\AppData\Local\Programs\Opera GX\launcher.exe",
    'spotify' : r"C:\Users\jdiaz\AppData\Roaming\Spotify\Spotify.exe",
    'discord' : r"C:\Users\jdiaz\AppData\Local\Discord\Update.exe --processStart Discord.exe"
}

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
        print("No entendi, intenta de nuevo...")
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
        
        elif 'busca' in rec:
            search = rec.replace('busca', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search + ": " + wiki)
            talk(wiki)
        
        elif 'alarma' in rec:
            clock = rec.replace('alarma', '')
            clock = clock.strip()
            talk("Alarma activada a las " + clock + "horas")
            while True:
                if datetime.datetime.now().strftime('%H:%M') == clock:
                    print("DESPIERTA!!!")
                    mixer.init()
                    mixer.music.load("supermariobros.mp3")
                    mixer.music.play()
                    if keyboard.read_key() == "q":
                        mixer.music.stop()
                        break
        
        elif 'colores' in rec: 
            talk("Enseguida...")
            Sara_RColors.capture()
        
        elif 'abre' in rec: 
            for site in sites:
                if site in rec:
                    sub.call(f'start chrome.exe {sites[site]}', shell = True)
                    talk(f'Abriendo {site}')
            for app in programs:
                if app in rec:
                    talk(f'Abriendo {app}')
                    os.startfile(programs[app])
        
        elif 'archivo' in rec:
            for file in files:
                if file in rec:
                    sub.Popen([files[file]], shell = True)
                    talk(f'Abriendo {file}')
        
        elif 'escribe' in rec:
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            
            except FileNotFoundError as e:
                file = open("Nota.txt", 'w')
                write(file)
        
        elif 'termina' in rec:
            talk('Adios!')
            break

def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell = True)

if __name__ == '__main__':
    run_Sara()
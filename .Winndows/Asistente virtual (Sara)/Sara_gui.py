                                        # Asistente virtual completo

 #Importación de librerías...

import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, Sara_RColors, os
from pygame import mixer
from tkinter import *
from PIL import Image, ImageTk
import threading as tr

# ... Importación de librerías

# Creación visual para ventana...q

main_window = Tk()
main_window.title("Sara AI")

main_window.geometry("1400x800")
main_window.resizable(0, 0)
main_window.configure(bg = '#203A43')

comandos = """ 
           Comandos para usar:

           - Reproduce...(canción)
           - Busca...(algo)
           - Abre...(página web o app)
           - Alarma...(hora en 24 horas)
           - Archivo...(nombre)
           - Colores (rojo, azul, amarillo)
           - Termina 
"""

label_title = Label(main_window, text =  "Sara AI", bg = "#2C5364", fg = "#91eae4",
                    font = ('Arial', 30, 'bold'))
label_title.pack(pady = 10)

canvas_comandos = Canvas(bg = "#799F0C", height = 250, width = 300)
canvas_comandos.place(x = 0, y = 0)

canvas_comandos.create_text(120, 110, text = comandos, fill = "White", font = 'Arial 10')

text_info = Text(main_window, bg  = "#1f4037", fg = "White")
text_info.place(x = 0, y = 250, width = 304, height = 550)

Sara_photo = ImageTk.PhotoImage(Image.open("robot.png"))
windows_photo = Label(main_window, image = Sara_photo)
windows_photo.pack(pady = 5)

def mexican_voice():
    change_voice(3)
def spanish_voice():
    change_voice(0)
def english_voice():
    change_voice(1)
def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("Hola soy Sara, ¿qué puedo hacer por ti el día de hoy?")

# Declaracion de variables...

name = "Sara"
listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 145)

def charge_data(name_dict, name_file):
    try:
        with open(name_file) as f:
            for line in f:
                (key, val) = line.split(",")
                val = val.rstrip("\n")
                name_dict[key] = val
    except FileNotFoundError as e:
        pass

sites = dict()
charge_data(sites, "pages.txt")

files = dict()
charge_data(files, "archivos.txt")

programs = dict()
charge_data(programs, "apps.txt")
print(programs)

# ...Declaracion de variables

# Funciones...

def mexican_voice():
    change_voice(3)
def spanish_voice():
    change_voice(0)
def english_voice():
    change_voice(1)
def change_voice(id):
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("Hola soy Sara, ¿qué puedo hacer por ti el día de hoy?")

def talk(text):
    engine.say(text)
    engine.runAndWait()

def hablar():
    text = text_info.get("1.0", "end")
    talk(text)

def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        talk("¡Hola soy Sara!, esperando instrucciones.")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language = "es")
        rec = rec.lower()
    except sr.UnknownValueError:
        talk("No entendi, intenta de nuevo...")
        if name in rec:
            rec = rec.replace(name, '')
    return rec

def talk_pages():
    if bool(sites) == True:
        talk("Has agregado las siguientes páginas web: ")
        for site in sites:
            talk(site)
    else:
        talk("Aún no has agregado páginas web.")

def talk_apps():
    if bool(programs) == True:
        talk("Has agregado las siguientes aplicaciones: ")
        for program in programs:
            talk(program)
    else:
        talk("Aún no has agregado aplicaciones.")

def talk_files():
    if bool(files) == True:
        talk("Has agregado los siguientes archivos: ")
        for file in files:
            talk(file)
    else:
        talk("Aún no has agregado archivos.")

def clock(rec):
    num = rec.replace('alarma', '')
    num = num.strip()
    talk("Alarma activida a las " + num + "horas.")
    if num[0] != '0' and len(num) < 5:
        num = '0' + num
    print(num)
    while True:
        if datetime.datetime.now().strftime('%H:%M') == clock:
            print("DESPIERTA!!!")
            mixer.init()
            mixer.music.load("supermariobros.mp3")
            mixer.music.play()
        else:
            continue
        if keyboard.read_key() == "q":
            mixer.music.stop()
            break

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
            talk(wiki)
            write_text(search + ": " + wiki)
            break
        
        elif 'alarma' in rec:
            t = tr.Thread(target = clock, args = (rec,))
            t.start()
        
        elif 'colores' in rec: 
            talk("Enseguida...")
            Sara_RColors.capture()
        
        elif 'abre' in rec:
            task = rec.replace('abre', '').strip() 

            if task in sites:
                for task in sites:
                    if task in rec:
                        sub.call(f'start brave.exe {sites[task]}', shell = True)
                        talk(f'Abriendo {task}')
            elif task in programs:
                for task in programs:
                    if task in rec:
                        talk(f'Abriendo {task}')
                        sub.Popen(programs[task])
            else:
                talk("Lo siento, parece que aun no has agregado esa app o página web")
        
        elif 'archivo' in rec:
            file = rec.replace('archivo', '').strip()
            if file in files:
                for file in files:
                    if file in rec:
                        sub.Popen([files[file]], shell = True)
                        talk(f'Abriendo {file}')
            else:
                talk("Lo siento, parece que aun no has agregado el archivo")
        
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

def open_w_files():
    global namefile_entry, pathf_entry
    windows_files = Toplevel()
    windows_files.title("Agregar archivos")
    windows_files.configure(bg = "#C9D6FF")
    windows_files.geometry("600x400")
    windows_files.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(windows_files)} center')

    title_label = Label(windows_files, text = "Agregar archivo", fg = "Black", bg = "#6dd5ed", font = ('Arial', 15, 'bold'))
    title_label.pack(pady = 3)
    
    name_label = Label(windows_files, text = "Nombre del archivo", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    name_label.pack(pady = 2)

    namefile_entry = Entry(windows_files)
    namefile_entry.pack(pady = 1)

    path_label = Label(windows_files, text = "Ruta del archivo", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    path_label.pack(pady = 2)

    pathf_entry = Entry(windows_files, width = 40)
    pathf_entry.pack(pady = 1)

    save_button = Button(windows_files, text = "Guardar", bg = "#7303c0", fg = "White", width = 8, height = 1, command = add_files)
    save_button.pack(pady = 4)

def open_w_apps():
    global nameapps_entry, patha_entry
    windows_apps = Toplevel()
    windows_apps.title("Agregar app")
    windows_apps.configure(bg = "#C9D6FF")
    windows_apps.geometry("600x400")
    windows_apps.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(windows_apps)} center')

    title_label = Label(windows_apps, text = "Agregar una app", fg = "Black", bg = "#6dd5ed", font = ('Arial', 15, 'bold'))
    title_label.pack(pady = 3)
    
    name_label = Label(windows_apps, text = "Nombre de la app", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    name_label.pack(pady = 2)

    nameapps_entry = Entry(windows_apps)
    nameapps_entry.pack(pady = 1)

    path_label = Label(windows_apps, text = "Ruta de la app", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    path_label.pack(pady = 2)

    patha_entry = Entry(windows_apps, width = 40)
    patha_entry.pack(pady = 1)

    save_button = Button(windows_apps, text = "Guardar", bg = "#7303c0", fg = "White", width = 8, height = 1, command = add_apps)
    save_button.pack(pady = 4)

def open_w_pages():
    global namepages_entry, pathp_entry
    windows_pages = Toplevel()
    windows_pages.title("Agregar página web")
    windows_pages.configure(bg = "#C9D6FF")
    windows_pages.geometry("600x400")
    windows_pages.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(windows_pages)} center')

    title_label = Label(windows_pages, text = "Agregar página web", fg = "Black", bg = "#6dd5ed", font = ('Arial', 15, 'bold'))
    title_label.pack(pady = 3)
    
    name_label = Label(windows_pages, text = "Nombre de la página web", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    name_label.pack(pady = 2)

    namepages_entry = Entry(windows_pages)
    namepages_entry.pack(pady = 1)

    path_label = Label(windows_pages, text = "Ruta de la página web", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    path_label.pack(pady = 2)

    pathp_entry = Entry(windows_pages, width = 40)
    pathp_entry.pack(pady = 1)

    save_button = Button(windows_pages, text = "Guardar", bg = "#7303c0", fg = "White", width = 8, height = 1, command = add_pages)
    save_button.pack(pady = 4)

def add_files():
    name_file = namefile_entry.get().strip()
    path_file = pathf_entry.get().strip()
    
    files[name_file] = path_file

    save_data(name_file, path_file, "archivos.txt")
    namefile_entry.delete(0, "end")
    pathf_entry.delete(0, "end")

def add_apps():
    name_file = nameapps_entry.get().strip()
    path_file = patha_entry.get().strip()
    
    save_data(name_file, path_file, "apps.txt")
    programs[name_file] = path_file
    nameapps_entry.delete(0, "end")
    patha_entry.delete(0, "end")

def add_pages():
    name_page = namepages_entry.get().strip()
    url_pages = pathp_entry.get().strip()
    
    sites[name_page] = url_pages
    save_data(name_page, url_pages, "pages.txt")
    namepages_entry.delete(0, "end")
    pathp_entry.delete(0, "end")

def save_data(key, value, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write(key + "," + value + "\n")
    except FileNotFoundError as f:
        file = open(file_name, 'a')
        file.write(key + "," + value + "\n")

def give_me_name():
    talk("Hola, ¿Cómo te llamas?")
    name = listen()
    name = name.strip()
    talk(f"Bienvenido {name}")

    try:
        with open("name.txt", 'w') as f:
            f.write(name)
    except FileNotFoundError:
        file = open("name.txt", 'w')
        file = write(name)

def say_hello():
    try:
        with open("name.txt", 'w') as f:
            for name in f:
                talk(f"Hola bienvenido {name}")
    except FileNotFoundError:
        give_me_name()

# ...Funciones

# Botones...

button_voice_mx = Button(main_window, text = "Voz México", fg = "white", bg = "#c471ed",
                        font = ("Arial", 10, "bold"), command = mexican_voice)
button_voice_mx.place(x=1030, y = 100, width = 120, height = 40)

button_voice_es = Button(main_window, text = "Voz España", fg = "white", bg = "#f64f59",
                        font = ("Arial", 10, "bold"), command = spanish_voice)
button_voice_es.place(x=1030, y = 170, width = 120, height = 40)

button_voice_us = Button(main_window, text = "Voz USA", fg = "white", bg = "#FBD786",
                        font = ("Arial", 10, "bold"), command = english_voice)
button_voice_us.place(x=1030, y = 240, width = 120, height = 40)

button_listen = Button(main_window, text = "Escuchar", fg = "white", bg = "#eaafc8",
                        font = ("Arial", 15, "bold"), command = run_Sara)
button_listen.pack(pady = 10)

button_speak = Button(main_window, text = "Hablar", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = hablar)
button_speak.place(x=1030, y = 310, width = 120, height = 40)

button_add_files = Button(main_window, text = "Agregar archivos", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = open_w_files)
button_add_files.place(x=1005, y = 380, width = 168, height = 40)

button_add_apps = Button(main_window, text = "Agregar apps", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = open_w_apps)
button_add_apps.place(x=1005, y = 450, width = 168, height = 40)

button_add_pages = Button(main_window, text = "Agregar páginas", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = open_w_pages)
button_add_pages.place(x=1005, y = 520, width = 168, height = 40)

button_tell_pages = Button(main_window, text = "Páginas agregadas", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_pages)
button_tell_pages.place(x=1195, y = 100, width = 195, height = 45)

button_tell_apps = Button(main_window, text = "Apps agregadas", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_apps)
button_tell_apps.place(x=1195, y = 170, width = 195, height = 45)

button_tell_files = Button(main_window, text = "Archivos agregadas", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_files)
button_tell_files.place(x=1195, y = 240, width = 195, height = 45)

# ... Botones

main_window.mainloop()
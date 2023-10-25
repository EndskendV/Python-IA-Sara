# --- Asistente virtual completo ---

# Importación de librerías...

import speech_recognition as sr
import subprocess as sub
import pyttsx3, pywhatkit, wikipedia, datetime, keyboard, Sara_RColors, os
from pygame import mixer
from tkinter import *
from PIL import Image, ImageTk
import threading as tr
import os
import whatsapp as whapp
import browser
import tabla # Database
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot import preprocessors
import face_recognizer as fr

# ... Importación de librerías

# Creación visual para ventana...

main_window = Tk()
main_window.title("Sara IA")

main_window.geometry("1400x800")
main_window.resizable(0, 0)
main_window.configure(bg = '#203A43')

comandos = """
           Comandos para usar:

           - Reproduce...(canción)
           - Busca...(algo)
           - Buscamé...(algo)
           - Abre...(página web o app)
           - Alarma...(hora en 24 horas)
           - Archivo...(nombre)
           - Colores (rojo, azul, amarillo)
           - Escribe
           - Mensaje de Whatsapp
           - Conversar
           - Termina 
"""

label_title = Label(main_window, text =  "Sara IA", bg = "#2C5364", fg = "#91eae4",
                    font = ('Arial', 30, 'bold'))
label_title.pack(pady = 10)

canvas_comandos = Canvas(bg = "#799F0C", height = 250, width = 300)
canvas_comandos.place(x = 0, y = 0)

canvas_comandos.create_text(120, 110, text = comandos, fill = "White", font = 'Arial 10')

text_info = Text(main_window, bg  = "#1f4037", fg = "White")
text_info.place(x = 0, y = 250, width = 304, height = 550)

# Imagen de Sara IA...

Sara_photo = ImageTk.PhotoImage(Image.open("robot.png"))
windows_photo = Label(main_window, image = Sara_photo)
windows_photo.pack(pady = 5)

# ...Imagen de Sara IA

# Declaracion de variables...

name = "Sara"
listener = sr.Recognizer()
engine = pyttsx3.init()

# Escoger voz representante para Sara IA...

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[3].id)
engine.setProperty('rate', 145)

# ...Escoger voz representante para Sara IA

def charge_data(name_dict, name_file):
    try:
        with open(name_file) as f:
            for line in f:
                (key, val) = line.split(",")
                val = val.rstrip("\n")
                name_dict[key] = val
    except FileNotFoundError as e:
        pass

# Funciones...

sites = dict()
charge_data(sites, "pages.txt")

files = dict()
charge_data(files, "archivos.txt")

programs = dict()
charge_data(programs, "apps.txt")

contacts = dict()
charge_data(contacts, "contacts.txt")

# ... Funciones

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

# Función que permite que te escuche Sara...

def listen(phrase = None):
    listener = sr.Recognizer()
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source)
        talk(phrase)
        pc = listener.listen(source)
    try:
        rec = listener.recognize_google(pc, language = "es")
        rec = rec.lower()
    except sr.UnknownValueError:
        talk("No entendi, intenta de nuevo...")
    except sr.RequestError as e:
        print("Could not request results from google Speech Recognition service: {0}".format(e))
    return rec

# ...Función que permite que te escuche Sara

# Función para agregar diferentes actividades...

# Páginas web...
def talk_pages():
    if bool(sites) == True:
        talk("Has agregado las siguientes páginas web: ")
        for site in sites:
            talk(site)
    else:
        talk("Aún no has agregado páginas web.")
# ...Páginas web

# Aplicaciones...
def talk_apps():
    if bool(programs) == True:
        talk("Has agregado las siguientes aplicaciones: ")
        for program in programs:
            talk(program)
    else:
        talk("Aún no has agregado aplicaciones.")
# ...Aplicaciones

# Archivos...
def talk_files():
    if bool(files) == True:
        talk("Has agregado los siguientes archivos: ")
        for file in files:
            talk(file)
    else:
        talk("Aún no has agregado archivos.")
# ...Archivos

# Contactos...

def talk_contacts():
    if bool(contacts) == True:
        talk("Has agregado los siguientes contactos")
        for cont in contacts:
            talk(cont)
    else:
        talk("No hay ningun nuevo contacto para mostrar")

# ... Contactos

# Acciones...

# Funciones asociadas a las palabras claves...

# Reproducir musica en youtube con PyWhatKit...
def reproduce(rec):
    music = rec.replace('reproduce', '')
    print("Reproduciendo" + music)
    talk("Reproduciendo" + music)
    pywhatkit.playonyt(music)
# ...Reproducir musica en youtube con PyWhatKit

# Busca información a través de explorador web...
def busca(rec):
    search = rec.replace('busca', '')
    wikipedia.set_lang("es")
    wiki = wikipedia.summary(search, 1)
    talk(wiki)
    write_text(search + ": " + wiki)
# ...Busca información a través de explorador web

# Creación de alarma...
def thread_alarma(rec):
    t = tr.Thread(target = clock, args = (rec,))
    t.start()
# ...Creación de alarma

# Busca colores a través de cámara(Color Amarrillo y Rojo)...
def colores(rec):
    talk("Enseguida...")
    t = tr.Thread(target = Sara_RColors.capture)
    t.start()
# ...Busca colores a través de cámara(Color Amarrillo y Rojo)

# Abrir aplicación o información web...
def abre(rec):
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
# ...Abrir aplicación o información web

# Archivo...
def archivo(rec):
    file = rec.replace('archivo', '').strip()
    if file in files:
        for file in files:
            if file in rec:
                os.startfile([files[file]], shell = True)
                talk(f'Abriendo {file}')
    else:
        talk("Lo siento, parece que aun no has agregado el archivo")
# ...Archivo

# Escribir nota...
def escribe(rec):
    try:
        with open("nota.txt", 'a') as f:
            write(f)
            
    except FileNotFoundError as e:
        file = open("Nota.txt", 'w')
        write(file)
# ...Escribir nota

# Enviar mensaje...

def enviar_mensaje(rec):
    talk("¿A quién quieres enviar el mensaje?")
    contact = listen("Te escucho")
    contact = contact.strip()

    if contact in contacts:
        for cont in contacts:
            if cont == contact:
                contact = contacts[cont]
                talk("Escriba su mensaje: ")
                message = listen("Te escucho")
                talk("Enviando mensaje...")
                whapp.send_message(contact, message)
    else:
        talk("Parece que aún no has agregado a ese contacto")

# ... Enviar mensaje

# ...Funciones asociadas a las palabras claves.


# Creación de alarma...
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
# ...Creación de alarma

def cierra(rec):
    for task in programs:
        kill_task = programs[task].split('\\')
        kill_task = kill_task[-1]
        if task in rec:
            sub.call(f'TASKKILL /M {kill_task} /F', Shell = True)
            talk(f'Cerrando {task}')
        
        if 'todo' in rec:
            sub.call(f'TASKKILL /M {kill_task} /F', Shell = True)
            talk(f'Cerrando {task}')
    
    if 'ciérrate' in rec:
        sub.call(f'TASKKILL /M SARA_IA.exe /F', Shell = True)
        talk('Adiós!')

def buscame(rec):
    something = rec.replace('búscame', '').strip()
    talk("Buscando " + something)
    browser.search(something)

'''def conversar(rec):
    chat = ChatBot("Sara", database_uri = None)
    trainer = ListTrainer(chat)
    trainer.train(tabla.get_questions_answers())
    talk("Vamos a conversar...")
    while True:
        try: 
            request = listen("")
        except UnboundLocalError:
            talk("Hubo un error, intenta de nuevo.")
            continue
        print("Tú: ", request)
        answer = chat.get_response(request)
        print("Sara: ", answer)
        talk(answer)
        if 'bai' in request:
            break
'''

def reconocimiento(rec):
    rec = rec.replace('reconocimiento', '').strip()
    if rec == 'activado':
        t = tr.Thread(target = fr.face_rec, args = (0,))
        t.start()
        talk("Activando reconocimiento...")
    elif 'lechuga':
        fr.face_rec(1)

# Acción principal para Sara...

# Diccionario con palabras clave...

key_words = {
    'reproduce' : reproduce,
    'busca' : busca,
    'alarma' : thread_alarma,
    'colores' : colores,
    'abre' : abre,
    'archivo' : archivo,
    'escribe' : escribe,
    'mensaje' : enviar_mensaje,
    'cierra' : cierra,
    'ciérrate' : cierra,
    'búsca': buscame,
    #'conversar' : conversar,
    'reconocimiento': reconocimiento
}

# ...Dicionario con palabras clave

def run_Sara():
    # Reproducir musica en youtube con PyWhatKit...
    chat = ChatBot("Sara", database_uri = None)
    trainer = ListTrainer(chat)
    trainer.train(tabla.get_questions_answers())
    talk("Te escucho...")
    while True:
        try: 
            rec = listen("")
        except UnboundLocalError:
            talk("Hubo un error, intenta de nuevo.")
            continue
        if 'busca' in rec:
            key_words['busca'](rec)
            break

        elif rec.split()[0] in key_words:
            key_words[rec.split()[0]](rec)
        
        else:
            print("Tú: ", rec)
            answer = chat.get_response(rec)
            print("Sara: ", answer)
            talk(answer)
            if 'bai' in rec:
                break

    main_window.update()
       
# ...Acción principal para Sara

# Escribir una nota a través de voz...
def write(f):
    talk("¿Que quieres que escriba?")
    rec_write = listen("Te escucho")
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listo, puedes revisarlo")
    sub.Popen("nota.txt", shell = True)
# ...Escribir una nota a través de voz

# ...Acciones

# Agregar funciones archivos, aplicaciones y páginas web...
# Función Archivos...
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
# ...Función Archivos

# Función aplicaciones...
def open_w_apps():
    global nameapps_entry, patha_entry
    windows_apps = Toplevel()
    windows_apps.title("Agregar una app")
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
# ...Función aplicaciones

# Función página web...
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
# ...Función página web

# Función contactos...

def open_w_contacts():
    global namecontact_entry, phone_entry
    windows_contacts = Toplevel()
    windows_contacts.title("Agregar contactos")
    windows_contacts.configure(bg = "#C9D6FF")
    windows_contacts.geometry("600x400")
    windows_contacts.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(windows_contacts)} center')

    title_label = Label(windows_contacts, text = "agregar contacto", fg = "Black", bg = "#6dd5ed", font = ('Arial', 15, 'bold'))
    title_label.pack(pady = 3)
    
    name_label = Label(windows_contacts, text = "Nombre del contacto", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    name_label.pack(pady = 2)

    namecontact_entry = Entry(windows_contacts)
    namecontact_entry.pack(pady = 1)

    phone_label = Label(windows_contacts, text = "Número del contacto (con código del país)", fg = "Black", bg = "#6dd5ed", font = ('Arial', 10, 'bold'))
    phone_label.pack(pady = 2)

    phone_entry = Entry(windows_contacts, width = 40)
    phone_entry.pack(pady = 1)

    save_button = Button(windows_contacts, text = "Guardar", bg = "#7303c0", fg = "White", width = 8, height = 1, command = add_contacts)
    save_button.pack(pady = 4)

#... Función contactos

# ...Agregar funciones archivos, aplicaciones y páginas web

# Formato para guardar...

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

def add_contacts():
    name_contact = namecontact_entry.get().strip()
    phone = phone_entry.get().strip()

    contacts[name_contact] = phone
    save_data(name_contact, phone, "contacts.txt")
    namecontact_entry.delete(0, "end")
    phone_entry.delete(0, "end")

def save_data(key, value, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write(key + "," + value + "\n")
    except FileNotFoundError as f:
        file = open(file_name, 'a')
        file.write(key + "," + value + "\n")

# ...Formato para guardar

# Método de saludo...

def give_me_name():
    talk("Hola, ¿Cómo te llamas?")
    name = listen("Te escucho")
    name = name.strip()
    talk(f"Bienvenido {name}")

    try:
        with open("name.txt", 'w') as f:
            f.write(name)
    except FileNotFoundError:
        file = open("name.txt", 'w')
        file = write(name)

def say_hello():
    
    if os.path.exists("name.txt"):
        with open("name.txt") as f:
            for name in f:
                talk(f"Hola, bienvenido {name}")
    else: 
        give_me_name()

def thread_hello():
    t = tr.Thread(target = say_hello)
    t.start()

thread_hello()

# ...Método de saludo

# ...Función para agregar diferentes actividades

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
button_add_files.place(x=1005, y = 380, width = 180, height = 40)

button_add_apps = Button(main_window, text = "Agregar apps", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = open_w_apps)
button_add_apps.place(x=1005, y = 450, width = 180, height = 40)

button_add_pages = Button(main_window, text = "Agregar páginas", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = open_w_pages)
button_add_pages.place(x=1005, y = 520, width = 180, height = 40)

button_add_contacts = Button(main_window, text = "Agregar contactos", fg = "white", bg = "#1f4037",
                        font = ("Arial", 10, "bold"), command = open_w_contacts)
button_add_contacts.place(x=1005, y = 590, width = 180, height = 40)

button_tell_pages = Button(main_window, text = "Páginas agregadas", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_pages)
button_tell_pages.place(x=1180, y = 100, width = 210, height = 45)

button_tell_apps = Button(main_window, text = "Apps agregadas", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_apps)
button_tell_apps.place(x=1180, y = 170, width = 210, height = 45)

button_tell_files = Button(main_window, text = "Archivos agregadas", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_files)
button_tell_files.place(x=1180, y = 240, width = 210, height = 45)

button_tell_contacts = Button(main_window, text = "Contactos Agregados", fg = "white", bg = "#1e130c",
                        font = ("Arial", 10, "bold"), command = talk_contacts)
button_tell_contacts.place(x=1180, y = 310, width = 210, height = 45)

# ... Botones

# Ventana principal de la aplicación...

main_window.mainloop()

# ... Ventana principal de la aplicación
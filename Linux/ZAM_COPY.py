# Importacion de librerias necesarias para la utilizacion del asistente virtual...

import speech_recognition as sr # Toma todo lo que decimos por microfono y lo transforma en texto.
import pyttsx3, pywhatkit # pyttsxx3 - Nos ayuda a que python permita hablar con el usuario. //////// # pywhatkit - Lo que hara es que nos permitira abrir una aplicacion, un ejemplo YouTube.
import wikipedia, colors # Wikipedia - conecta nuestra aplicacion a la pagina wikipedia. ///////// # colors - Integramos el programa de deteccion de colores.
import keyboard, datetime # keyboard - Nos ayuda a que cuando nosotros cuando utilizamos el teclado, la aplicacion lo podra manipular, por asi decirlo.
from pygame import mixer # Maneja el sonido. ///////// # pfacebook.comTraceback (most recent call last): File "/home/jesusdiaz/Escritorio/clon3/Python-IA-Sara/Linux/conectar.py", line 78, in <module> insert_data('question_answers', ['default','¿Cuál es tu nombre?', 'Juan']) File "/home/jesusdiaz/Escritorio/clon3/Python-IA-Sara/Linux/conectar.py", line 63, in insert_data cursor.execute(query, data) psycopg2.errors.InvalidTextRepresentation: invalid input syntax for type integer: "default" LINE 1: INSERT INTO question_answers VALUES ('default', '¿Cuál es tu...ygame - Generalmente se utiliza para crear videojuegos.
import time, os # os - nos ayuda en manejar archivos en dentro de python.
import subprocess as sub # SubProcess - Este nos ayuda pueda llamar otros procesos o a otros programas de nuestra computadora y que los pueda ejecutar.
import threading as tr # threading - Nos ayuda en crear aplicaciones que puedan realizar múltiples tareas en paralelo. Los hilos son una forma de lograr concurrencia en Python.
from tkinter import * # tkinter - Nos servira para crear interfaces gráficas de usuario de manera sencilla.
from PIL import Image # PIL - Nos ayuda a utilizar imagenes dentro de python, manipulación.
import whatsapp as what # Importacion del archivo whatsapp, lo nombraremos como what.
import conectar
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import database
import face_recognizer as fr

# ...Importacion de librerias necesarias para la utilizacion del asistente virtual.

# Creación de ventana principal...

main_window = Tk()
main_window.title("ZAM - Asistente virtual") # Titulo de la ventana.
 
main_window.geometry("550x950") # Tamaño de la ventana.
main_window.resizable(0, 0) # No se pueda agrandar
main_window.configure(bg = '#0d090f') # Fondo de la ventana.

# ,,,Creación de ventana principal.

# Muestra esto en pantalla de la aplicacion...

comandos = """


            Comandos que puedes utilizar:
            
            > Reproduce... (Canción o video).
            > Busca... (Algun tipo de informacion).
            > Abre... (Página web o aplicación de escritorio).
            > Alarma... (Definelo en 24H).
            > Archivo... (Escoger nombre).
            > Colores... (Rojo, Azul y Amarillo).
            > mensaje... (Whatsapp).
            > Termina.
            > Conversar...
"""

# ...Muestra esto en pantalla de la aplicacion.

Label_title = Label(main_window, text = "ZAM - Asistente Virtual", bg = '#0d090f', fg = '#E3C6CE',
                    font = ('URW Bookman', 15, 'bold')) # Titulo de la aplicación. Este tendra: texto, color del fondo, color de letra y tipo de letra.
Label_title.pack(pady = 30)

text_info = Text(main_window, bg = "#2E202A", fg = "white", bd = 0, highlightbackground = "#0d090f")
text_info.place(x = 48, y = 750, height = 100, width = 450)

# GIF...

Zam_gif_path = "/home/jesusdiaz/Escritorio/clon3/Python-IA-Sara/Resourses/Loading.gif" # Ubicacion de la imagen GIF.
info_gif = Image.open(Zam_gif_path)
gif_nframes = info_gif.n_frames # 73 = numero de frames del GIF

Zam_gif_list = [PhotoImage(file = Zam_gif_path, format = f'gif -index {i}') for i in range(gif_nframes)] # Contiene informacion de las 73 imagenes que conforma el GIF.
label_gif = Label(main_window, bd = 0, highlightbackground='#0d090f') # Configuracion de fondo y contorno del GIF.
label_gif.pack() # Posicionar nuestro GIF debajo de la interfaz.

# Animar GIF...

def animate_gif(index):
    frame = Zam_gif_list[index] # Acceder cada uno de los elementos a traves del indice, cada uno son informacion de los cuadros o imagenes que compone el GIF.
    index += 1 # Aumentar en 1 el indice.
    if index == gif_nframes:
        index = 0 # Reiniciar el ciclo de las imagenes
    label_gif.configure(image = frame)
    main_window.after(25, animate_gif, index)
 

# ...Animar GIF.

# Nueva ventana para instrucciones...

def ventana_instrucciones():
    ventana_Instrucciones = Toplevel(main_window)
    ventana_Instrucciones.title("Comandos_ZAM")

    ventana_Instrucciones.geometry("350x550") # Tamaño de la ventana.
    ventana_Instrucciones.resizable(0, 0) # No se pueda agrandar
    ventana_Instrucciones.configure(bg = '#0d090f') # Fondo de la ventana.canvas

    if ventana_Instrucciones.title() == "Instrucciones":
        pass
    else:
        canvas_comandos = Canvas(ventana_Instrucciones, bg="black", height=450, width=450)
        canvas_comandos.pack()
        canvas_comandos.create_text(150, 90, text=comandos, fill="white", font='Arial 11') # Muestra los comandos a la cual podemos utilizar.

# ...Nueva ventana para instrucciones.

# Nueva Agregar para instrucciones...

def ventana_agregar(): # Aun no hablar de esto es para despues...
    ventana_Agregar = Toplevel(main_window)
    ventana_Agregar.title("Apps/Files/Pages_ZAM")

    ventana_Agregar.geometry("750x300") # Tamaño de la ventana.
    ventana_Agregar.resizable(0, 0) # No se pueda agrandar
    ventana_Agregar.configure(bg = '#0d090f') # Fondo de la ventana.canvas

    if ventana_Agregar.title() == "Agregar":
        pass
    else:

        # Creacion de botones y etiquetas en la ventana de instrucciones...

        Label_title = Label(ventana_Agregar, text = "Agregar", bg = '#0d090f', fg = '#E3C6CE', # Etiqueta "Agregar"...
                    font = ('URW Bookman', 15, 'bold')) 
        Label_title.place(x = 120, y = 20)

        Label_title = Label(ventana_Agregar, text = "Agregados", bg = '#0d090f', fg = '#E3C6CE', # Etiqueta "Agregados"...
                    font = ('URW Bookman', 15, 'bold'))
        Label_title.place(x = 520, y = 20)
        
        button_add_files = Button(ventana_Agregar, text = "Archivos", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_files) # Funcion para el boton "Archivos"...
        button_add_files.place(x = 105, y = 75)

        button_add_apps = Button(ventana_Agregar, text = "Programas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_apps) # Funcion para el boton "Programas"...
        button_add_apps.place(x = 105, y = 130) 

        button_add_pages = Button(ventana_Agregar, text = "Páginas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_pages) # Funcion para el boton "Paginas"... 
        button_add_pages.place(x = 105, y = 190)

        button_add_contacts = Button(ventana_Agregar, text = "Contactos", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_contacts) # Funcion para el boton "Contactos"...
        button_add_contacts.place(x = 105, y = 245)

        button_tell_files = Button(ventana_Agregar, text = "Ver Archivos", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                                command = talk_files) # Funcion para ver que "Ver Archivos" agregamos...
        button_tell_files.place(x = 500, y = 75)

        button_tell_apps = Button(ventana_Agregar, text = "Ver Programas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                                command = talk_apps) # Funcion para ver que "Ver Programas" agregamos...
        button_tell_apps.place(x = 500, y = 130)

        button_tell_pages = Button(ventana_Agregar, text = "Ver Páginas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = talk_pages) # Funcion para ver que "Ver Páginas" agregamos...
        button_tell_pages.place(x = 500, y = 190)

        button_tell_contacts = Button(ventana_Agregar, text = "Ver Contactos", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = talk_contacts) # Funcion para ver que "Ver Contactos" agregamos...
        button_tell_contacts.place(x = 500, y = 245)

        # ...Creacion de botones y etiquetas en la ventana de instrucciones.

# ...Nueva Agregar para instrucciones.

# Declaracion de variables...
name = "ZAM" # Nombre del asistente virtual.
listener = sr.Recognizer() # iniciala una variable para que escuche la maquina.
engine = pyttsx3.init()

# Esto nos permite escoger la voz la que utilizara el  asistente virtual...
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[22].id) # Escogimos como voz Spanish Latin, (escoger el idioma).
#engine.setProperty('lang', 'es')
engine.setProperty('rate', 145)
# ... Esto nos permitira escoger la voz que utilizara el asistente virtual.

# Diccionario, estructura de datos una clave y un valor...



# region TXT LECTURA
##LECTURA
def charge_data(name_file):
    try:
        valorx = conectar.get_table(f'"{name_file}"')
        print('Cargando '+name_file)
        print(dict(valorx))
        return dict(valorx)
    except FileNotFoundError as e:
        print('Paso '+ name_file)
        pass

programs = charge_data("apps.txt") # Guarda las Apps en la base de datos

sites = charge_data("pages.txt") # Guarda las paginas web como ".txt"

files = charge_data("archivos.txt") # Guarda las archivos como ".txt"

contacts = charge_data("contacts.txt") # Guarda las Contactos como ".txt"

# endregion



# ...Diccionario, estructura de datos una clave y un valor.

# ...Declaracion de variables.

# Crear funciones...
def talk(text):
    engine.say(text) # Todo lo que pongamos dentro de este parentesis con el metodo say, lo convertira en voz.
    engine.runAndWait() # Esto hara que funcione la instruccion anterior.

def read_and_talk():
    text = text_info.get("1.0", "end")
    talk(text)

def write_text(text_wiki):
    text_info.insert(INSERT, text_wiki)

# Creacion de la funcion para crear una ventana para ingresar nombre, enlace y boton para agregar archivo...

def open_files():
    
    # Creacion de la ventana...

    global namefiles, pathf
    window_files = Toplevel()
    window_files.title("Agrega archivos.")
    window_files.geometry("750x250")
    window_files.configure(bg = "#0d090f")
    window_files.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_files)} center')

    # ...Creacion de la ventana.

    title_label = Label(window_files, text = "Agregar un archivo:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_files, text = "Nombre del archivo:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    namefiles = Entry(window_files) # Ventana para ingresar texto.
    namefiles.place(x = 55, y = 80)

    path_label = Label(window_files, text = "Ruta del archivo:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    path_label.place(x = 450, y = 50)

    pathf = Entry(window_files) # Ventana para ingresar texto.
    pathf.place(x = 400, y = 80, width = 300)

    save_button = Button(window_files, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_files) # En donde se almacenerá.
    save_button.place(x = 300, y = 150) # Creacion de boton "Guardar".

# ...Creacion de la funcion para crear una ventana para ingresar nombre, enlace y boton para agregar archivo.

# Creacion de la funcion para crear una ventana para ingresar nombre, enlace y boton para agregar Apps...

def open_apps():

    # Creacion de la ventana...

    global nameapps, patha
    window_apps = Toplevel()
    window_apps.title("Agrega aplicación.")
    window_apps.geometry("750x250")
    window_apps.configure(bg = "#0d090f")
    window_apps.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_apps)} center')

    # ...Creacion de la ventana.

    title_label = Label(window_apps, text = "Agregar una aplicación:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_apps, text = "Nombre de la aplicación:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    nameapps = Entry(window_apps)
    nameapps.place(x = 55, y = 80)

    path_label = Label(window_apps, text = "Ruta de la aplicación:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    path_label.place(x = 450, y = 50)

    patha = Entry(window_apps)
    patha.place(x = 400, y = 80, width = 300)

    save_button = Button(window_apps, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_apps)
    save_button.place(x = 300, y = 150)

# ...Creacion de la funcion para crear una ventana para ingresar nombre, enlace y boton para agregar Apps.

def open_pages():
    global namepages, pathpages
    window_pages = Toplevel()
    window_pages.title("Agrega páginas web.")
    window_pages.geometry("750x250")
    window_pages.configure(bg = "#0d090f")
    window_pages.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_pages)} center')

    title_label = Label(window_pages, text = "Agregar un página web:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_pages, text = "Nombre de la página web:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    namepages = Entry(window_pages)
    namepages.place(x = 55, y = 80)

    path_label = Label(window_pages, text = "URL de la página web:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    path_label.place(x = 450, y = 50)

    pathpages = Entry(window_pages)
    pathpages.place(x = 400, y = 80, width = 300)

    save_button = Button(window_pages, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_pages)
    save_button.place(x = 300, y = 150)

def open_contacts():
    global namecontact_entry, phone_entry
    window_contacts = Toplevel()
    window_contacts.title("Agrega contactos.")
    window_contacts.geometry("750x250")
    window_contacts.configure(bg = "#0d090f")
    window_contacts.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_contacts)} center')

    title_label = Label(window_contacts, text = "Agrega contacto:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_contacts, text = "Nombre del contacto:", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    namecontact_entry = Entry(window_contacts)
    namecontact_entry.place(x = 55, y = 80)

    phone_label = Label(window_contacts, text = "Número celular (con código del país):", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    phone_label.place(x = 400, y = 50)

    phone_entry = Entry(window_contacts, width=35)
    phone_entry.place(x = 400, y = 80, width = 300)

    save_button = Button(window_contacts, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_contacts)
    save_button.place(x = 300, y = 150)
# region ESCRITURA

def add_files():
    name_file = namefiles.get().strip() # Nombre del archivo.
    path_file = pathf.get().strip() # Ruta del archivo.
    print(path_file)
    files[name_file] = path_file

    save_data(name_file, path_file, "archivos.txt") # Donde se almacenará
    namefiles.delete(0, "end")
    pathf.delete(0, "end")

def add_apps():
    name_file = nameapps.get().strip()
    path_file = patha.get().strip()
    
    save_data(name_file, path_file, "apps.txt")
    programs[name_file] = path_file
    nameapps.delete(0, "end")
    patha.delete(0, "end")

def add_pages():
    name_page = namepages.get().strip()
    url_pages = pathpages.get().strip()
    
    sites[name_page] = url_pages
    save_data(name_page, url_pages, "pages.txt")
    namepages.delete(0, "end")
    pathpages.delete(0, "end")

def add_contacts():
    name_contact = namecontact_entry.get().strip()
    phone = phone_entry.get().strip()
    
    contacts[name_contact] = phone
    save_data(name_contact, phone, "contacts.txt")
    namecontact_entry.delete(0, "end")
    phone_entry.delete(0, "end")

def save_data(key, value, file_name):
    try:
        conectar.insert_data(f'"{file_name}"',f"'{key}','{value}'")
        print('Subido')

    except FileNotFoundError as f:
        
## Escritura
# save_data('Misael','+664801225222',"contacts.txt")

# endregion
# Muestra que Aplicaciones, Contatos, Paginas web y Archivos agregados...

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

def talk_contacts():
    if bool(contacts) == True:
        talk("Has agregado los siguientes contactos.")
        for cont in contacts:
            talk(cont)
    else:
        talk("Aún no has agregado contactos.")

# ...Muestra que Aplicaciones, Contatos, Paginas web y Archivos agregados.

def listen(phrase=None):
    listener = sr.Recognizer()
    with sr.Microphone() as source: # Toma como fuente el microfono para escuchar.
        listener.adjust_for_ambient_noise(source)
        talk(phrase)
        pc = listener.listen(source)
    # Comprueba que si va bien el programa...
    try:
        rec = listener.recognize_google(pc, language = "es") # Aseguramos que fue capturado la voz y lo transforma en texto.
        rec = rec.lower() # Metodo que transforma las palabras en minusculas, para minimizar problemas.
    except sr.UnknownValueError:
        print("No entendí, intenta de nuevo.")
    # Comprueba que si va bien el programa...
    except sr.RequestError as e:
        print("could not request from Google Speech Recognition service; {0}".format(e))

    return rec # Retorna todo lo que dijimos en microfono.

# Esto sirve para escribir blocs de notas...

# Definicion de funciones, esto representa acciones que puede realizar el asistente virtual...

def reproduce(rec):
    music = rec.replace('reproduce', '')
    print("Reproduciendo: " + music)
    talk("Reproduciendo: " + music)
    pywhatkit.playonyt(music) # Reproduce musica y/o video desde YouTube, gracias a pywhatkit.

def busca(rec):
    search = rec.replace('busca: ', '')
    wikipedia.set_lang("es") # Lo que busque Wikipedia, nos mostrara la informacion en espanol.
    wiki = wikipedia.summary(search, 1) # Resumir la informacion, el "1" es la cantidad de oraciones que utilizara
    talk(wiki) # Nos dira la informacion obtenida.
    write_text(search + ": " + wiki)

def alarma(rec):
    num = rec.replace('alarma', '').strip()
    alarm_time = datetime.datetime.now().strftime(num, '%H:%M')
    
    current_time = datetime.now()
    time_difference = alarm_time - current_time
    # Convierte la diferencia de tiempo en segundos
    seconds_until_alarm = time_difference.total_seconds()
            
    if seconds_until_alarm <= 0:
        talk("La hora de la alarma ha pasado.")
    else:
        talk(f"Alarma activada a las {num} horas.")
        time.sleep(seconds_until_alarm)  # Espera hasta que sea hora de la alarma

        print("¡Es hora de despertar!")
        mixer.init()
        mixer.music.load("SuperMarioBros.mp3")
        mixer.music.play()

        if keyboard.read_key() == "s":
            mixer.music.stop()

def colores(rec):
    talk("Enseguida...")
    t = tr.Thread(target=colors.capture)
    t.start()

def abre(rec):
    task = rec.replace('abre', '').strip()

    if task in sites: 
        for task in sites:
            if task in rec:
                sub.call(f'google-chrome {sites[task]}', shell=True) # Aqui seleccionamos el programa de busqueda de Google Chrome
                talk(f'Abriendo {task}')
    elif task in programs:
        for task in programs:
            if task in rec:
                talk(f'Abriendo {task}')
                sub.Popen(programs[task])
    else:
        talk("Lo siento, parece que aun no has agregado esa app o página web.")

def archivo(rec):
    file = rec.replace('archivo', '').strip()
    if file in files:
        for file in files:
            if file in rec:
                file_path = files[file]
                sub.run(["xdg-open", file_path]) # Esto nos ayudara a ejecutar una instruccion para poder abrir un archivo.
                talk(f'Abriendo {file}')
            else:
                talk("Lo siento, parece que aun no has agregado ese archivo.")

def escribe(rec):
    try:
        with open("nota.txt", 'a') as f:
            write(f)
            
    except FileNotFoundError as e:
        file = open("nota.txt", 'w')
        write(file)

def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listó, puede revisarlo")
    sub.run(["xdg-open", "nota.txt"])

def enviar_mensaje(rec):
    talk("¿A quién enviamos mensaje?")
    contact = listen("...")
    print(contact)
    contact = contact.strip()

    if contact in contacts:
        for cont in contacts:
            if cont == contact:
                contact = contacts[cont]
                talk("¿Qué mensaje quieres enviar?")
                message = listen("...")
                talk("Enviando mensaje:")
                what.send_message(contact, message)
    
    else:
        talk("Parece que aún no has agregado a ese contacto, usa el botón de agregar.")

# Nos ayudara al momento de iniciar ZAM, te solicitara un nombre de usuario...

def give_me_name():
    talk("Hola, ¿Cómo te llamas?")
    name = listen() # Guarda el nombre del usuario.
    name = name.strip()
    talk(f"Bienvenido {name}") # Si ya tiene un nombre de usuario ZAM saludara al usuario.

    try:
        with open("name.txt", 'w') as f:
            f.write(name)
    except FileNotFoundError:
        file = open("name.txt", 'w')
        file.write(name)

# ...Nos ayudara al momento de iniciar ZAM, te solicitara un nombre de usuario.

def say_hello():
    
        if os.path.exists("name.txt"):
            with open("name.txt") as f:
                for name in f:
                    talk(f"Hola, bienvenido {name}")
        else:
            give_me_name()

def thread_hello():
    t = tr.Thread(target=say_hello)
    t.start()


#def conversar(rec):
 #   chat = ChatBot("ZAM", conectar_uri=None)
  #  trainer = ListTrainer(chat)
   # trainer.train(conectar.get_questions_answers())
    #talk("Vamos a conversar...")
    #while True:
     #   try:
      #      request=listen("")
       # except UnboundLocalError:
        #    talk("No entendi, acercate al microfono...")
         #   continue
        #print("Tú: ", request)
       # answer = chat.get_response(request)
        #print("ZAM: ", answer)
        #talk(answer)
        #if 'terminar ZAM' in request:
         #   break

def conversar(rec):
    chat = ChatBot("ZAM", database_url=None)
    trainer = ListTrainer(chat) 
    trainer.train(database.get_questions_answer())
    talk("Vamos a conversar...")
    while True:
        try:
            request = listen()
        except UnboundLocalError:
            talk("No te entendi, acercate al microfono...")
            continue
        print("Tú: ", request)
        answer = chat.get_response(request)
        print("ZAM: ", answer)
        talk(answer)
        if 'finalizar' in request:
            break

def reconocimiento(rec):
    rec = rec.replace('reconocimiento', '').strip()
    if rec == 'activado':
        t = tr.Thread(target=fr.face_rec, args=(0,))
        t.start()
        talk("Activando alarma de reconocimiento...")
    elif 'apagar':
        fr.face_rec(1)

# ...Esto sirve para escribir blocs de notas.

# ...Definicion de funciones, esto representa acciones que puede realizar el asistente virtual.

# Diccionario a la cual llama las acciones determinadas...

key_words = {
    'reproduce' : reproduce,
    'reproducir' : reproduce,
    'busca' : busca,
    'alarma' : alarma,
    'colores' : colores,
    'abre' : abre,
    'archivo' : archivo,
    'escribe' : escribe,
    'mensaje' : enviar_mensaje,
    'conversar' : conversar,
    'reconocimiento' : reconocimiento,

}

# ...Diccionario a la cual llama las acciones determinadas.

# Esta es la funcion principal para iniciar el detector de voz a la cual ejecutara ciertas acciones...
# a la cual se encuentra en el diccionario "Key_words".

def run_ZAM():
    talk("Te escucho...")
    while True:
        try:
            rec = listen()

        except UnboundLocalError:
            talk("No te entendí, intenta de nuevo.")
            continue # En dado de que no entienda nuestras instrucciones volvera al while para empezar de nuevo.

        if 'busca' in rec:
            key_words['busca'](rec)
            break
        else:
            for word in key_words:
                if word in rec:
                    key_words[word](rec)
        if 'termina' in rec:
            talk('adios!')
            break
    main_window.update() # Sirve para refrescar la pantalla, no interrumpe con el ciclo de while True.

# Esta es la funcion principal para iniciar el detector de voz a la cual ejecutara ciertas acciones...
# a la cual se encuentra en el diccionario "Key_words".

# ...Crear funciones.

button_start = Button(main_window, text = "INICIAR", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce", width = 20,
                          command = run_ZAM) #Funcion principal que sirve para iniciar ZAM.
button_start.pack(pady = 20)

boton_instrucciones = Button(main_window, text="Ver instrucciones de uso", command = ventana_instrucciones, fg = "#e3c6ce",bd = 0, bg = "#0d090f", highlightbackground = "#e3c6ce")
boton_instrucciones.pack(pady = 1) # Funcion que crea una ventana para ver instrucciones de uso del asistente virtual.

button_speak = Button(main_window, text = "HABLA", fg = "#e3c6ce", bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = read_and_talk) # Funcion que sirve para leer y hablar lo que puso el usuario en el cuadro de texto.
button_speak.place(x = 385, y = 870)

button_add_files = Button(main_window, text = "EXTRA", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = ventana_agregar) # Funcion que sirve para agregar programas, apps y paginas webs.
button_add_files.place(x = 225, y = 690)


# ...Entrada principal del programa.
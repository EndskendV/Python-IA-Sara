# Importacion de librerias necesarias para la utilizacion del asistente virtual...

import speech_recognition as sr # Toma todo lo que decimos por microfono y lo transforma en texto.
import pyttsx3, pywhatkit # pyttsxx3 - Nos ayuda a que python permita hablar con el usuario. //////// # pywhatkit - Lo que hara es que nos permitira abrir una aplicacion, un ejemplo YouTube.
import wikipedia, colors # Wikipedia - conecta nuestra aplicacion a la pagina wikipedia. ///////// # colors - Integramos el programa de deteccion de colores.
import keyboard, datetime # keyboard - Nos ayuda a que cuando nosotros cuando utilizamos el teclado, la aplicacion lo podra manipular, por asi decirlo.
from pygame import mixer # Maneja el sonido. ///////// # pygame - Generalmente se utiliza para crear videojuegos.
import time, os # os - nos ayuda en manejar archivos en dentro de python.
import subprocess as sub # SubProcess - Este nos ayuda pueda llamar otros procesos o a otros programas de nuestra computadora y que los pueda ejecutar.
import threading as tr # threading - Nos ayuda en crear aplicaciones que puedan realizar múltiples tareas en paralelo. Los hilos son una forma de lograr concurrencia en Python.
from tkinter import * # tkinter - Nos servira para crear interfaces gráficas de usuario de manera sencilla.
from PIL import Image # PIL - Nos ayuda a utilizar imagenes dentro de python, manipulación.

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
            > Termina.
"""

# ...Muestra esto en pantalla de la aplicacion.

Label_title = Label(main_window, text = "ZAM - Asistente Virtual", bg = '#0d090f', fg = '#E3C6CE',
                    font = ('URW Bookman', 15, 'bold')) # Titulo de la aplicación. Este tendra: texto, color del fondo, color de letra y tipo de letra.
Label_title.pack(pady = 30)

text_info = Text(main_window, bg = "#2E202A", fg = "white", bd = 0, highlightbackground = "#0d090f")
text_info.place(x = 50, y = 700, height = 50, width = 450)

# GIF...

Zam_gif_path = "../Resourses/Loading.gif" # Ubicacion de la imagen GIF.
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
 
animate_gif(0) 

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
        canvas_comandos.create_text(150, 90, text=comandos, fill="white", font='Arial 11')

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

        Label_title = Label(ventana_Agregar, text = "Agregar", bg = '#0d090f', fg = '#E3C6CE',
                    font = ('URW Bookman', 15, 'bold'))
        Label_title.place(x = 120, y = 20)

        Label_title = Label(ventana_Agregar, text = "Agregados", bg = '#0d090f', fg = '#E3C6CE',
                    font = ('URW Bookman', 15, 'bold'))
        Label_title.place(x = 520, y = 20)
        
        button_add_files = Button(ventana_Agregar, text = "Archivos", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_files) # Funcion
        button_add_files.place(x = 105, y = 75)

        button_add_apps = Button(ventana_Agregar, text = "Programas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_apps) # Funcion
        button_add_apps.place(x = 105, y = 130) # 750x300

        button_add_pages = Button(ventana_Agregar, text = "Paginas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = open_pages) # Funcion 
        button_add_pages.place(x = 105, y = 190)

        button_tell_files = Button(ventana_Agregar, text = "Ver Archivos", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                                command = talk_files) # Funcion
        button_tell_files.place(x = 500, y = 75)

        button_tell_apps = Button(ventana_Agregar, text = "Ver Programas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                                command = talk_apps) # Funcion
        button_tell_apps.place(x = 500, y = 130)

        button_tell_pages = Button(ventana_Agregar, text = "Ver Páginas", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = talk_pages) # Funcion
        button_tell_pages.place(x = 500, y = 190)

# ...Nueva Agregar para instrucciones.
# Aun no mostrar, falta implemnentar configuracion...
def charge_data(name_dict, name_file):
    try:
        with open(name_file) as f:
            for line in f:
                (key, val) = line.split(",")
                val = val.rstrip("\n")
                name_dict[key] = val
    except FileNotFoundError as e:
        pass

# ... GIF.

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

sites = dict()
charge_data(sites, "pages.txt")

files = dict()
charge_data(files, "archivos.txt")

programs = dict()
charge_data(programs, "apps.txt")

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

def open_files():
    global namefiles, pathf
    window_files = Toplevel()
    window_files.title("Agrega archivos")
    window_files.geometry("750x250")
    window_files.configure(bg = "#0d090f")
    window_files.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_files)} center')

    title_label = Label(window_files, text = "Agregar un archivo", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_files, text = "Nombre del archivo", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    namefiles = Entry(window_files)
    namefiles.place(x = 55, y = 80)

    path_label = Label(window_files, text = "Ruta del archivo", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    path_label.place(x = 450, y = 50)

    pathf = Entry(window_files)
    pathf.place(x = 400, y = 80, width = 300)

    save_button = Button(window_files, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_files)
    save_button.place(x = 300, y = 150)

def open_apps():
    global nameapps, patha
    window_apps = Toplevel()
    window_apps.title("Agrega aplicación")
    window_apps.geometry("750x250")
    window_apps.configure(bg = "#0d090f")
    window_apps.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_apps)} center')

    title_label = Label(window_apps, text = "Agregar una aplicación", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_apps, text = "Nombre de la aplicación", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    nameapps = Entry(window_apps)
    nameapps.place(x = 55, y = 80)

    path_label = Label(window_apps, text = "Ruta de la aplicación", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    path_label.place(x = 450, y = 50)

    patha = Entry(window_apps)
    patha.place(x = 400, y = 80, width = 300)

    save_button = Button(window_apps, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_apps)
    save_button.place(x = 300, y = 150)

def open_pages():
    global namepages, pathpages
    window_pages = Toplevel()
    window_pages.title("Agrega páginas web")
    window_pages.geometry("750x250")
    window_pages.configure(bg = "#0d090f")
    window_pages.resizable(0, 0)
    main_window.eval(f'tk::PlaceWindow {str(window_pages)} center')

    title_label = Label(window_pages, text = "Agregar un página web", fg = "white", bg = "#0d090f", font = ('URW Bookman', 15, 'bold'))
    title_label.pack(pady = 3)
    name_label = Label(window_pages, text = "Nombre de la página web", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    name_label.place(x = 50, y = 50)

    namepages = Entry(window_pages)
    namepages.place(x = 55, y = 80)

    path_label = Label(window_pages, text = "URL de la página web", fg = "white", bg = "#0d090f", font = ('URW Bookman', 13, 'bold'))
    path_label.place(x = 450, y = 50)

    pathpages = Entry(window_pages)
    pathpages.place(x = 400, y = 80, width = 300)

    save_button = Button(window_pages, text = "Guardar", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = add_pages)
    save_button.place(x = 300, y = 150)

def add_files():
    name_file = namefiles.get().strip()
    path_file = pathf.get().strip()
    
    files[name_file] = path_file

    save_data(name_file, path_file, "archivos.txt")
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

def save_data(key, value, file_name):
    try:
        with open(file_name, 'a') as f:
            f.write(key + "," + value + "\n")
    except FileNotFoundError as f:
        file = open(file_name, 'a')
        file.write(key + "," + value + "\n")

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

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source: # Toma como fuente el microfono para escuchar.
        talk("Bienvenido, te escuchó...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    # Comprueba que si va bien el programa...
    try:
        rec = listener.recognize_google(pc, language = "es") # Aseguramos que fue capturado la voz y lo transforma en texto.
        rec = rec.lower() # Metodo que transforma las palabras en minusculas, para minimizar problemas.
    except sr.UnknownValueError:
        pass
    # Comprueba que si va bien el programa...

    return rec # Retorna todo lo que dijimos en microfono.

# Esto sirve para escribir blocs de notas...

def write(f):
    talk("¿Qué quieres que escriba?")
    rec_write = listen()
    f.write(rec_write + os.linesep)
    f.close()
    talk("Listó, puede revisarlo")
    sub.run(["xdg-open", "nota.txt"])

# ...Esto sirve para escribir blocs de notas.

# Todo un proceso para reproducir en YouTube... 

def run_ZAM():
    while True:
        rec = listen()
        if 'reproduce' in rec: # Vamos a decir que reprodusca "Tal musica o tal video". 
            music = rec.replace('reproduce', '')
            print("Reproduciendo: " + music)
            talk("Reproduciendo: " + music)
            pywhatkit.playonyt(music) # Reproduce musica y/o video desde YouTube, gracias a pywhatkit.

# ...Todo un proceso para reproducir en YouTube.

        elif 'busca' in rec: # Vamos a decir que busque "tal cosa" a base del motor de busqueda de Wikipedia. 
            search = rec.replace('busca: ', '')
            wikipedia.set_lang("es") # Lo que busque Wikipedia, nos mostrara la informacion en espanol.
            wiki = wikipedia.summary(search, 1) # Resumir la informacion, el "1" es la cantidad de oraciones que utilizara
            talk(wiki) # Nos dira la informacion obtenida.
            write_text(search + ": " + wiki)
            break
        
        elif 'alarma' in rec: # Vamos a definir un despertador, la palabra alarma es la clave para que funcione un accion del asistente virtual.
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
        
        elif 'colores' in rec: # Vamos a definir Colors para llamar a la aplicacion de lector de colores.
            talk("Enseguida...")
            colors.capture()

        elif 'abre' in rec: # Definimos la palabra abre para poder abrir una pestaña de busqueda.
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
        
        elif 'archivo' in rec: # Definimos la palabra archivo, esto nos permite abrir una archivo dentro de nuestro computador. 
            file = rec.replace('archivo', '').strip()
            if file in files:
                for file in files:
                    if file in rec:
                        file_path = files[file]
                        sub.run(["xdg-open", file_path]) # Esto nos ayudara a ejecutar una instruccion para poder abrir un archivo.
                        talk(f'Abriendo {file}')
                    else:
                        talk("Lo siento, parece que aun no has agregado ese archivo.")
        
        elif 'escribe' in rec: # Decimos: escribe para poder hacer una nota a la cual guarda en nuestro computador.
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            
            except FileNotFoundError as e:
                file = open("nota.txt", 'w')
                write(file)

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
    
        if os.path.exists("name.txt"):
            with open("name.txt") as f:
                for name in f:
                    talk(f"Hola bienvenido {name}")
        else:
            give_me_name()

def thread_hello():
    t = tr.Thread(target=say_hello)
    t.start()

thread_hello()

# Instruccion que sirve para escoger que idioma va mostrar como ejemplo...

def mexican_voice():
    change_voice(22)

def spanish_voice():
    change_voice(21)

def usa_voice():
    change_voice(18)

def change_voice(id): # Va a mostrar que voz fue elegido como muestra.
    engine.setProperty('voice', voices[id].id)
    engine.setProperty('rate', 145)
    talk("Bienvenido, soy ZAM. Listo para trabajar.")

# ...Instruccion que sirve para escoger que idioma va mostrar como ejemplo.

# ...Crear funciones.

button_voice_mx = Button(main_window, text = "México", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                         command = mexican_voice) # Funcion que sirve para crear un boton para mostrar voz en idioma Español(Mexico).
button_voice_mx.place(x = 45, y = 900)

button_voice_es = Button(main_window, text = "España", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = spanish_voice) # Funcion que sirve para crear un boton para mostrar voz en idioma Español(España).
button_voice_es.place(x = 215, y = 900) 

button_voice_usa = Button(main_window, text = "English", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = usa_voice) # Funcion que sirve para crear un boton para mostrar voz en idioma Ingles(USA).
button_voice_usa.place(x = 385, y = 900)

button_start = Button(main_window, text = "INICIAR", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce", width = 20,
                          command = run_ZAM) #Funcion principal que sirve para iniciar ZAM.
button_start.pack(pady = 20)

boton_instrucciones = Button(main_window, text="Ver instrucciones de uso", command = ventana_instrucciones, fg = "#e3c6ce",bd = 0, bg = "#0d090f", highlightbackground = "#e3c6ce")
boton_instrucciones.pack(pady = 1)

button_speak = Button(main_window, text = "HABLA", fg = "#e3c6ce", bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = read_and_talk) # Funcion que sirve para leer y hablar lo que puso el usuario en el cuadro de texto.
button_speak.place(x = 45, y = 800)

button_add_files = Button(main_window, text = "AGREGAR", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = ventana_agregar) # Funcion que sirve para agregar programas, apps y paginas webs.
button_add_files.place(x = 385, y = 800)

# Entrada principal del programa...

main_window,mainloop()

# ...Entrada principal del programa.
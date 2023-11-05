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
from tkinter import ttk

# ...Importacion de librerias necesarias para la utilizacion del asistente virtual.

# Creación de ventana principal...

main_window = Tk()
main_window.title("ZAM - Asistente virtual") # Titulo de la ventana.

#///////////////////////////////////////////////////////////////

panel = ttk.Notebook(main_window)
panel.pack(fill = "both", expand="yes")

tab1 = ttk.Frame(panel)
panel.add(tab1, text = "Etiquetas")


#///////////////////////////////////////////////////////////////


main_window.geometry("550x950") # Tamaño de la ventana.
main_window.resizable(0, 0) # No se pueda agrandar
main_window.configure(bg = '#0d090f') # Fondo de la ventana.

# ,,,Creación de ventana principal.

# Muestra esto en pantalla de la aplicacion...

comandos = """
            Comandos que puedes utilizar:
            > Reproduce... (Cancion o video).
            > Busca... (Algun tipo de informacion).
            > Abre... (Pagina web o aplicacion de escritorio).
            > Alarma... (Definelo en 24H).
            > Archivo... (Escoger nombre).
            > Colores... (Rojo, Azul y Amarillo).
            > Termina.
"""

# ...Muestra esto en pantalla de la aplicacion.

Label_title = Label(main_window, text = "ZAM - Asistente Virtual", bg = '#0d090f', fg = '#E3C6CE',
                    font = ('URW Bookman', 15, 'bold')) # Titulo de la aplicación. Este tendra: texto, color del fondo, color de letra y tipo de letra.
Label_title.pack(pady = 30)

canvas_comandos = Canvas(bg = "black", height = 50, width = 450)
canvas_comandos.place(x = 45, y = 700)

# GIF...

Zam_gif_path = "/home/jesusdiaz/Escritorio/Clon/Python-IA-Sara/Resourses/Loading.gif" # Ubicacion de la imagen GIF.
info_gif = Image.open(Zam_gif_path)
gif_nframes = info_gif.n_frames # 73 = numero de frames del GIF

Zam_gif_list = [PhotoImage(file = Zam_gif_path, format = f'gif -index {i}') for i in range(gif_nframes)] # Contiene informacion de las 73 imagenes que conforma el GIF.
label_gif = Label(main_window, bd=0, highlightbackground='white') # Configuracion de fondo y contorno del GIF.
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

sites = {
                'google' : 'https://www.google.com', # Visitar google.
                'youtube' : 'https://www.youtube.com/',
                'wikipedia' : 'https://es.wikipedia.org/wiki/Wikipedia:Portada',
                'mortales' : 'https://www.youtube.com/@kdevs1488',
                'classroom' : 'https://classroom.google.com/'
}

files = {
                'constancia': 'constancia.pdf', # Abrir cualquier tipo de archivo.
                'imagen': 'kakashi.jpg',
                'leer': 'logicaProgramacion.pdf'
}

programs = {
    'navegador': '/usr/bin/google-chrome', # Abrir programa.
    'firefox': '/usr/bin/firefox',
    'calculadora': '/usr/bin/gnome-calculator'
}

# ...Diccionario, estructura de datos una clave y un valor.

# ...Declaracion de variables.

# Crear funciones...
def talk(text):
    engine.say(text) # Todo lo que pongamos dentro de este parentesis con el metodo say, lo convertira en voz.
    engine.runAndWait() # Esto hara que funcione la instruccion anterior.

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
    talk("Listo, puede revisarlo")
    sub.run(["xdg-open", "nota.txt"])

# ...Esto sirve para escribir blocs de notas.

def clock(rec):
    num = rec.replace('alarma', '')
    num = num.strip()
    talk("Alarma activada a las " + num + " horas.")

    if num[0] != '0' and len(num) < 5: 
        num = '0' + num
    print(num)
    while True:
        if datetime.datetime.now().strftime('%H:%M') == num:
            print("DESPIERTA, HUEVON!!!")
            mixer.init()
            mixer.music.load("SuperMarioBros.mp3")
            mixer.music.play()

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
            wiki = wikipedia.summary(search, 1) # Resumir la informacion, el "1" es la cantidad de oraciones que utilizara.
            print(search + ": " + wiki)
            talk(wiki) # Nos dira la informacion obtenida.
        
        elif 'alarma' in rec: # Vamos a definir un despertador, la palabra alarma es la clave para que funcione un accion del asistente virtual.
            t = tr.Thread(target = clock, args=(rec, ))
            t.start()
        
        elif 'colores' in rec: # Vamos a definir Colors para llamar a la aplicacion de lector de colores.
            talk("Enseguida...")
            colors.capture()

        elif 'abre' in rec: # Definimos la palabra abre para poder abrir una pestaña de busqueda.
            for site in sites:
                if site in rec:
                    sub.call(f'google-chrome {sites[site]}', shell=True) # Aqui seleccionamos el programa de busqueda de Google Chrome
                    talk(f'Abriendo {site}')
            for app in programs:
                if app in rec:
                    talk(f'Abriendo {app}')
                    sub.Popen(programs[app])
        
        elif 'archivo' in rec: # Definimos la palabra archivo, esto nos permite abrir una archivo dentro de nuestro computador. 
            for file in files:
                if file in rec:
                    file_path = files[file]
                    sub.run(["xdg-open", file_path]) # Esto nos ayudara a ejecutar una instruccion para poder abrir un archivo.
                    talk(f'Abriendo {file}')
        
        elif 'escribe' in rec: # Decimos: escribe para poder hacer una nota a la cual guarda en nuestro computador.
            try:
                with open("nota.txt", 'a') as f:
                    write(f)
            
            except FileNotFoundError as e:
                file = open("nota.txt", 'w')
                write(file)

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
button_voice_mx.place(x = 45, y = 850)

button_voice_es = Button(main_window, text = "España", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = spanish_voice) # Funcion que sirve para crear un boton para mostrar voz en idioma Español(España).
button_voice_es.place(x = 215, y = 850) 

button_voice_usa = Button(main_window, text = "English", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce",
                          command = usa_voice) # Funcion que sirve para crear un boton para mostrar voz en idioma Ingles(USA).
button_voice_usa.place(x = 385, y = 850)

button_start = Button(main_window, text = "INICIAR", fg = "#e3c6ce",bd = 0, bg = "#0d090f", font = ('URW Bookman', 15, 'bold'), highlightbackground = "#e3c6ce", width = 20,
                          command = run_ZAM) #Funcion principal que sirve para iniciar ZAM.
button_start.pack(pady = 20)

# Entrada principal del programa...

main_window,mainloop()

# ...Entrada principal del programa.


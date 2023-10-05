# Importacion de librerias necesarias para la utilizacion del asistente virtual...

import speech_recognition as sr # Toma todo lo que decimos por microfono y lo transforma en texto.
import pyttsx3, pywhatkit # pyttsxx3 - Nos ayuda a que python permita hablar con el usuario. //////// # pywhatkit - Lo que hara es que nos permitira abrir una aplicacion, un ejemplo YouTube.
import wikipedia, pygame # Wikipedia - conecta nuestra aplicacion a la pagina wikipedia. ///////// # pygame - Generalmente se utiliza para crear videojuegos.
import keyboard, datetime # keyboard - Nos ayuda a que cuando nosotros cuando utilizamos el teclado, la aplicacion lo podra manipular, por asi decirlo.
from pygame import mixer # Maneja el sonido.

# ...Importacion de librerias necesarias para la utilizacion del asistente virtual.

# Declaracion de variables...
name = "ZAM" # Nombre del asistente virtual.
listener = sr.Recognizer() # iniciala una variable para que escuche la maquina.
engine = pyttsx3.init()

# Esto nos permite escoger la voz la que utilizara el  asistente virtual...
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[21].id) # Escogimos como voz Spanish Latin, (escoger el idioma).
engine.setProperty('lang', 'es')
# ... Esto nos permitira escoger la voz que utilizara el asistente virtual.

# ...Declaracion de variables.

# Crear funciones...
def talk(text):
    engine.say(text) # Todo lo que pongamos dentro de este parentesis con el metodo say, lo convertira en voz.
    engine.runAndWait() # Esto hara que funcione la instruccion anterior.

def listen():
    listener = sr.Recognizer()
    with sr.Microphone() as source: # Toma como fuente el microfono para escuchar.
        print("Escuchando...")
        listener.adjust_for_ambient_noise(source)
        pc = listener.listen(source)

    # Comprueba que si va bien el programa...
    try:
        rec = listener.recognize_google(pc, language = "es") # Aseguramos que fue capturado la voz y lo transforma en texto.
        rec = rec.lower() # Metodo que transforma las palabras en minusculas, para minimizar problemas.
    except sr.UnknownValueError:
        print("No entendi, intenta de nuevo...")
        if name in rec:
            rec = rec.replace(name, '')
    # Comprueba que si va bien el programa...

    return rec # Retorna todo lo que dijimos en microfono.

# Todo un proceso para reproducir en YouTube...
def run_ZAM():
    while True:
        rec = listen()
        if 'reproduce' in rec: # Vamos a decir que reprodusca "Tal musica o tal video". 
            music = rec.replace('reproduce', '')
            print("Reproduciendo: " + music)
            talk("Reproduciendo: " + music)
            pywhatkit.playonyt(music) # Reproduce musica y/o video desde YouTube, gracias a pywhatkit.
        elif 'busca' in rec: # Vamos a decir que busque "tal cosa" a base del motor de busqueda de Wikipedia. 
            search = rec.replace('busca: ', '')
            wikipedia.set_lang("es") # Lo que busque Wikipedia, nos mostrara la informacion en espanol.
            wiki = wikipedia.summary(search, 1) # Resumir la informacion, el "1" es la cantidad de oraciones que utilizara.
            print(search + ": " + wiki)
            talk(wiki) # Nos dira la informacion obtenida.
        elif 'alarma' in rec: # Vamos a definir un despertador, la palabra alarma es la clave para que funcione un accion del asistente virtual.
            num = rec.replace('alarma', '')
            num = num.strip() # Este metodo corta el string vacio de la instruccion de arriba, sin esto la hora va a tener un espacio de mas, esto genera un error.
            talk("Alarma activada a las " + num + " horas.")
            while True: #Se repita la alarma hasta que lo cerremos.
                if datetime.datetime.now().strftime('%H:%M') == num: # El "H" es para hora y "M" es para minutos.
                    print("DESPIERTA!!!")
                    mixer.init()
                    mixer.music.load("SuperMarioBros.mp3") # Sonido de alarma.
                    mixer.music.play()
                    if keyboard.is_pressed() == "s": # Tecla parar la alarma.
                        mixer.music.stop()
                        break

# ...Todo un proceso para reproducir en YouTube.

# ...Crear funciones.

# Entrada principal del programa...
if __name__ == '__main__':
    run_ZAM()
# ...Entrada principal del programa.
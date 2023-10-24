# Importacion de librerias necesarias para la utilizacion del asistente virtual
import speech_recognition as sr # Toma todo lo que decimos por microfono y lo transforma en texto.
import pyttsx3, pywhatkit # pyttsxx3 - Nos ayuda a que python permita hablar con el usuario. //////// # pywhatkit - Lo que hara es que nos permitira abrir una aplicacion, un ejemplo YouTube.
import wikipedia, pygame # Wikipedia - conecta nuestra aplicacion a la pagina wikipedia. ///////// # pygame - Generalmente se utiliza para crear videojuegos.
import keyboard, datetime # keyboard - Nos ayuda a que cuando nosotros cuando utilizamos el teclado, la aplicacion lo podra manipular, por asi decirlo.
from pygame import mixer
import time

# Declaracion de variables...
name = "ZAM" # Nombre del asistente virtual.
listener = sr.Recognizer() # iniciala una variable para que escuche la maquina.
engine = pyttsx3.init()

####Que tal si separamos el codigo POR PARTES!!!!
####Por ejemplo pyttsx3 Y las configuraciones del mismo colocarlo aparte, y posteriormente hacer un
#### .Configure para el usuario customize, si hay error use un Default.

# Esto nos permite escoger la voz la que utilizara el  asistente virtual...
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[21].id) # Escogimos como voz Spanish Latin, escoger el idioma.
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

        ##Codigo para Colocar lo que esta entendiendo el LISTEN
        ##
        ##
        print(rec)
        time.sleep(1000)

        if 'reproduce' in rec: 
            music = rec.replace('reproduce', '')
            print("Reproduciendo: " + music)
            talk("Reproduciendo: " + music)
            pywhatkit.playonyt(music)
        elif 'busca' in rec:
            search = rec.replace('busca: ', '')
            wikipedia.set_lang("es")
            wiki = wikipedia.summary(search, 1)
            print(search +": " + wiki)
            talk(wiki)
        elif 'alarma' in rec:
            num = rec.replace('alarma', '')
            num = num.strip()
            talk("Alarma activada a las " + num + " horas.")   
            print(num)         
            while True:
                if datetime.datetime.now().strftime('%H:%M') == num:
                    print("DESPIERTA!!!")
                    pygame.mixer.init()
                    pygame.mixer.music.load("SuperMarioBros.mp3")
                    pygame.mixer.music.play()
                    detener = input("s")
                    if detener == "s":
                        pygame.mixer.music.stop()
                        break


# ...Todo un proceso para reproducir en YouTube.

# ...Crear funciones.

if __name__ == '__main__':
    run_ZAM()
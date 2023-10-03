# Importacion de librerias necesarias para la utilizacion del asistente virtual
import speech_recognition as sr # Toma todo lo que decimos por microfono y lo transforma en texto.
import pyttsx3, pywhatkit # pyttsxx3 - Nos ayuda a que python permita hablar con el usuario. //////// # pywhatkit - Lo que hara es que nos permitira abrir una aplicacion, un ejemplo YouTube.
import wikipedia, pygame # Wikipedia - conecta nuestra aplicacion a la pagina wikipedia. ///////// # pygame - Generalmente se utiliza para crear videojuegos.
import keyboard, datetime # keyboard - Nos ayuda a que cuando nosotros cuando utilizamos el teclado, la aplicacion lo podra manipular, por asi decirlo.
from pygame import mixer # 

# Declaracion de variables...
name = "ZAM" # Nombre del asistente virtual.
listener = sr.Recognizer() # iniciala una variable para que escuche la maquina.
engine = pyttsx3.init()

# Esto nos permite escoger la voz la que utilizara el  asistente virtual...
voices = engine.getProperty('voices') 
engine.setProperty('voice', voices[21].id) # Escogimos como voz Spanish Latin, escoger el idioma.
engine.setProperty('lang', 'es')

for i in voices:
    print (i)
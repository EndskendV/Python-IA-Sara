import speech_recognition as sr
import pyttsx3
import time
import os

# Función set_alarm
def set_alarm(hour, minute):
    while True:
        current_time = time.localtime()
        if current_time.tm_hour == hour and current_time.tm_min == minute:
            print("¡Es hora de despertar!")
            play_alarm_sound()
            break
        time.sleep(60)  # Esperar 1 minuto antes de verificar de nuevo

# Función play_alarm_sound
def play_alarm_sound():
    # Cambia la ruta al archivo de sonido que desees reproducir
    sound_file = "SuperMarioBros.mp3"
    if os.path.exists(sound_file):
        os.system(f"aplay {sound_file}")
    else:
        print("Archivo de sonido no encontrado.")

# Función talk para que el asistente hable
def talk(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    print("Programa de despertador")

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Háblame para configurar la alarma...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        alarm_time = recognizer.recognize_google(audio, language="es")
        print("Hora de la alarma configurada a:", alarm_time)
        talk("Hora de la alarma configurada a:" + alarm_time)

        alarm_time_parts = alarm_time.split(":")
        alarm_hour = int(alarm_time_parts[0])
        alarm_minute = int(alarm_time_parts[1])

        set_alarm(alarm_hour, alarm_minute)

    except sr.UnknownValueError:
        print("No se escuchó una hora válida.")

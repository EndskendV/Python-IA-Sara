import webbrowser
import pyautogui as at # Automatizar procesos con python, se puede utilizar con paginas webs.
import time 

def send_message(contact, message): # Necesitara dos parametros, el numero de contacto y el mensaje.
    webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
    time.sleep(8)
    at.press('enter')
import webbrowser
import pyautogui as at # "as" Alias
import time

def send_message(contact, message):
    webbrowser.open(f"https://web.whatsapp.com/send?phone={contact}&text={message}")
    time.sleep(8)
    at.press('enter')
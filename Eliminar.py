from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

def check_chromium():
    # Configura las opciones del navegador
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = '/usr/bin/chromium'  # Ruta al binario de Chromium

    # Crea una instancia del navegador
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Abre una página de ejemplo
        driver.get('https://www.google.com')

        # Imprime el título de la página para verificar que está funcionando
        print('Título de la página:', driver.title)
    finally:
        # Cierra el navegador al finalizar
        driver.quit()

check_chromium()

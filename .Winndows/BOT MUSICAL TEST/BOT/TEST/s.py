import openpyxl
import pyautogui
import time

def leer_datos_desde_excel(archivo_excel):
    # Cargar el archivo Excel
    wb = openpyxl.load_workbook(archivo_excel)
    # Seleccionar la hoja de trabajo deseada
    hoja = wb['Hoja1']
    
    # Leer los datos de cada fila
    datos = []
    for fila in hoja.iter_rows(values_only=True):
        # Ignorar la primera fila si contiene encabezados
        if fila[0] != "Consecutivo":
            datos.append(fila)
    
    return datos

def desglosar_nombre(nombre_completo):
    partes = nombre_completo.split(' ', 2)
    if len(partes) < 3:
        partes.extend(['', ''])
    nombre, apellido1, apellido2 = partes
    return nombre, apellido1, apellido2

def ingresar_datos_al_sistema(datos):
    # Esperar unos segundos antes de iniciar para asegurarse de que el sistema esté listo
    time.sleep(5)
    for dato in datos:
        consecutivo, nombre_completo, edad, sexo = dato
        nombre, apellido1, apellido2 = desglosar_nombre(nombre_completo)
        
        # Lógica para ingresar los datos al sistema
        # Utiliza las variables nombre, apellido1 y apellido2 según sea necesario
         
        # Simular comandos de "KeyPress" para ingresar los datos uno por uno

        pyautogui.typewrite('300')  # Codigo USR
        pyautogui.press('enter', presses=3);  # Tabulador para pasar al siguiente campo
        time.sleep(0.1)

        pyautogui.typewrite(nombre)  # Ingresa el nombre
        pyautogui.press('tab')  # Tabulador para pasar al siguiente campo
        pyautogui.typewrite(apellido1)  # Ingresa el nombre
        pyautogui.press('tab')  # Tabulador para pasar al siguiente campo
        pyautogui.typewrite(apellido2)  # Ingresa el nombre
        pyautogui.press('enter')  # Tabulador para pasar al siguiente campo

        if edad is None:
            pyautogui.typewrite('20')
        else:
            pyautogui.typewrite(str(edad))  # Ingresa la edad
        pyautogui.press('enter',presses=2)

        if sexo == 'M' or sexo is None:
            time.sleep(0.1)  # Espera 1 segundo
            pyautogui.press('right')  # Presiona la tecla "Right" si el sexo es "M" o nulo
            
        else:
            pyautogui.press('enter') 

        pyautogui.press('enter') 
        pyautogui.typewrite('22')  # Codigo DOPING
        pyautogui.press('enter', presses=4);  # Tabulador para pasar al siguiente campo
            
        # Esperar un segundo antes de pasar al siguiente dato
        time.sleep(0.1)
        #////
        #pyautogui.click(x=100, y=200) #Ajustar a medicos
        #////
        pyautogui.press(['a','down'],interval=0.1)
        pyautogui.press('enter',presses=5, interval=0.05) #Pasar a cobro
        #////
        #pyautogui.click(x=100, y=200) #Ajustar a pago
        #////
        pyautogui.press('enter',presses=4, interval=0.05) #Pasar a recibo
        pyautogui.press(['right','enter'],presses=2, interval=0.1) #Omitir etiqueta y fact
        time.sleep(0.1)

        # Ejemplo:
        print(f"Ingresando datos: Consecutivo={consecutivo}, Nombre={nombre}, Apellido1={apellido1}, Apellido2={apellido2}, Edad={edad}, Sexo={sexo}")



# Ejemplo de uso
archivo_excel = "C:/Users/CALIPSO/Desktop/BOT/TEST/datos.xlsx"
datos = leer_datos_desde_excel(archivo_excel)
ingresar_datos_al_sistema(datos)

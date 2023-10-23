##pip uninstall opencv-python
##sudo apt-get install build-essential libgtk2.0-dev pkg-config
##pip install opencv-python

##hacer esto en terminal principal.

import cv2 # Se utilizara para abrir la camara y reconocimiento de colores e imagenes y de rostros.
import numpy as np # Se utiliza para arreglos y funciones matematicas, se utilizara np para definir la libreria como alias NP.

# Funcion para dibujar contornos de las figuras y esos contornos se pinten de esa figura...

def draw(mask, color, frame_arg): # Se utilizara BGR para detectar los colores. Trabaja lo contrario que RGB
    countours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) # Encontrar contorno.
    for c in countours:
        area = cv2.contourArea(c)
        if area > 1000:
            new_countour = cv2.convexHull(c)
            cv2.drawContours(frame_arg, [new_countour], 0, color, 3) # Nuevo contornos. Esto ayuda a definir bien el color.

# ... Funcion para dibujar contornos de las figuras y esos contornos se pinten de esa figura.

def capture():
    # Metodo usar la camara en vivo.
    cap = cv2.VideoCapture(0)

    # Deteccion de colores
    low_yellow = np.array([25, 190, 20], np.uint8)
    high_yellow = np.array([30, 255, 255], np.uint8)
    low_red1 = np.array([0, 100, 20], np.uint8)
    high_red1 = np.array([5, 255, 255], np.uint8)
    low_red2 = np.array([175, 100, 20], np.uint8)
    high_red2 = np.array([180, 255, 255], np.uint8)
    low_blue = np.array([100, 100, 20], np.uint8)
    high_blue = np.array([130, 255, 255], np.uint8)

    while True: 
        comp, frame = cap.read()
        if comp == True: 
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            yellow_mask = cv2.inRange(frame_HSV, low_yellow, high_yellow)
            red_mask1 = cv2.inRange(frame_HSV, low_red1, high_red1)
            red_mask2 = cv2.inRange(frame_HSV, low_red2, high_red2)
            blue_mask = cv2.inRange(frame_HSV, low_blue, high_blue)

            
            red_mask = cv2.add(red_mask1, red_mask2)

            draw(yellow_mask, [0, 255, 255], frame)
            draw(red_mask, [0, 0, 255], frame)
            draw(blue_mask, [255, 0, 0], frame)


            cv2.imshow('Chesse_ZAM', frame)

            if cv2.waitKey(1) & 0xFF == ord('s'):
                break
    cap.release()
    cv2.destroyAllWindows()
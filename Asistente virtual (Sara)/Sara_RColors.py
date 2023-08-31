# Asistente reconoce colores a partir del uso de la camara
import cv2
import numpy as np

def draw(mask, color, frame_arg):
    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, 
        cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        area = cv2.contourArea(c) # Calcular el área del contorno
        if area > 1000:
            new_countour = cv2.convexHull(c)
            cv2.drawContours(frame_arg, [new_countour], 0, color, 3)
            M = cv2.moments(c)
            if (M["m00"]==0): M["m00"]=1
            x = int(M["m10"]/M["m00"])
            y = int(M['m01']/M['m00'])
            font = cv2.FONT_HERSHEY_COMPLEX
            if color == [0, 255, 255]:
                cv2.putText(frame_arg, 'Amarillo', (x+10, y), font, 0.75, (0, 255, 255), 1, cv2.LINE_AA)
            elif color == [0, 0, 255]:
                cv2.putText(frame_arg, 'Rojo', (x+10, y), font, 0.75, (0, 0, 255), 1, cv2.LINE_AA)
            elif color == [255, 0, 0]:
                cv2.putText(frame_arg, 'Azul', (x+10, y), font, 0.75, (255, 0, 0), 1, cv2.LINE_AA)

def capture():
    cap = cv2.VideoCapture(0)

    low_yellow = np.array([20, 190, 20], np.uint8)
    high_yellow = np.array([30, 255, 255], np.uint8)

    low_red1 = np.array([0, 100, 20], np.uint8)
    high_red1 = np.array([5, 255, 255], np.uint8)
    
    low_red2 = np.array([175, 100, 20], np.uint8)
    high_red2 = np.array([179, 255, 255], np.uint8)

    low_green = np.array([45, 100, 20], np.uint8)
    high_green = np.array([75, 255, 255], np.uint8)

    low_blue = np.array([85, 200, 20], np.uint8)
    high_blue = np.array([125, 255, 255], np.uint8)

    while True:
        comp, frame = cap.read()
        if comp == True:
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask_yellow = cv2.inRange(frame_HSV, low_yellow, high_yellow)
            mask_red1 = cv2.inRange(frame_HSV, low_red1, high_red1)
            mask_red2 = cv2.inRange(frame_HSV, low_red2, high_red2)
            mask_red = cv2.add(mask_red1, mask_red2)
            green_mask = cv2.inRange(frame_HSV, low_green, high_green)
            blue_mask = cv2.inRange(frame_HSV, low_blue, high_blue)
            green_mask = cv2.inRange(frame_HSV, low_green, high_green)

            draw(mask_yellow, (35, 220, 240), frame)
            draw(mask_red, (0, 0, 255), frame)
            draw(blue_mask, (255, 0, 0), frame)
            draw(green_mask, (0, 143, 57), frame)
            cv2.imshow('Webcam', frame)

            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
                cap.release()
                cv2.destroyAllWindows()
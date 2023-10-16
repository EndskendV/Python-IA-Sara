from tkinter import *

root = Tk()
 
framesNum = 73 # Numero de frames que tiene el gif, si no lo conoces ir haciendo tentativos.
archivo = "Resourses/Loading.gif"

# Lista de todas las imagenes del gif
frames = [PhotoImage(file=archivo, format='gif -index %i' %(i)) for i in range(framesNum)]

def update(ind):
    """ Actualiza la imagen gif """
    frame = frames[ind]
    ind += 1
    if ind == framesNum:
        ind = 0
    label.configure(image=frame)
    root.after(20, update, ind) # Numero que regula la velocidad del gif

label = Label(root)
label.pack()
root.after(0, update, 0)
root.overrideredirect(True)  # Elimina bordes y barra de título

        # Obtiene las dimensiones de la pantalla
screen_width = root.winfo_screenwidth()/3
screen_height = root.winfo_screenheight()/2
root.geometry(f"+{int(screen_width)}+{int(screen_height)}")  # Mueve la ventana al centro inferior
   
root.mainloop()


import sqlite3

def abrir_y_mostrar_contenido():
    # Conectar a la base de datos
    conn = sqlite3.connect('brain.db')
    cursor = conn.cursor()

    # Realizar una consulta SELECT para recuperar los archivos
    cursor.execute('SELECT nombre, rutaArchivo FROM archivos')
    archivos = cursor.fetchall()

    # Mostrar el contenido de los archivos
    if archivos:
        for nombre, rutaArchivo in archivos:
            try:
                # Abrir y leer el contenido del archivo
                with open(rutaArchivo, 'r') as archivo:
                    contenido = archivo.read()
                    print(f"Contenido del archivo {nombre}:\n{contenido}\n")
            except FileNotFoundError:
                print(f"Archivo {nombre} no encontrado en la ruta {rutaArchivo}")
            except Exception as e:
                print(f"Error al leer el archivo {nombre}: {str(e)}")
    else:
        print("No hay archivos en la base de datos.")

    # Cerrar la conexión
    conn.close()

# Llamar a la función para abrir y mostrar el contenido de los archivos
abrir_y_mostrar_contenido()

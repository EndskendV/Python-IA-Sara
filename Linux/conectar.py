# import mysql.connector

# def create_connection():
#     conexion = mysql.connector.connect(user = 'root', password='Galgos-2020', host='localhost', database='brain', port = '3306')
#     print('hacks')
#     return conexion

# def get_table():
#     connection = create_connection()
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM question_answers")
#     return cursor.fetchall()

# bot_list = list()

# def get_questions_answers():
#     rows = get_table()
#     for row in rows:
#         print(row)
#         bot_list.extend(list(row))
#         print(bot_list)
#     return bot_list

import psycopg2 as db
##Conexion a BD
conexion=db
try:
    conexion1 = db.connect(user='zam', password='1234', host='post4parra.ddns.net', database='zamdata', port=5432)
    conexion=conexion1
    print("Conexión a la primera base de datos exitosa")

# Manejar la excepción en caso de error
except db.Error as e:
    print(f"Error durante la conexión a la primera base de datos: {e}")

# Intentar conectarse a la segunda base de datos
try:
    conexion2 = db.connect(user='zam', password='1234', host='rolling-corp.net', database='zamdata', port=5432)
    conexion=conexion2
    print("Conexión a la segunda base de datos exitosa")

# Manejar la excepción en caso de error
except db.Error as e:
    print(f"Error durante la conexión a la segunda base de datos: {e}")
    




def get_table(table, condition=None):
    cursor = conexion.cursor()
    if condition:
        cursor.execute(f"SELECT * FROM {table} WHERE {condition}")
    else:
        cursor.execute(f"SELECT * FROM {table}")
    return cursor.fetchall()

def get_table_columns(table):
    cursor = conexion.cursor()
    cursor.execute(f"SELECT * FROM {table}")
    return [desc[0] for desc in cursor.description]



def update_data(table, data, condition):
    cursor = conexion.cursor()
    query = f"UPDATE {table} SET {data} WHERE {condition}"
    cursor.execute(query)
    conexion.commit()
    return cursor.rowcount


def insert_data(table, data):
    cursor = conexion.cursor()

    if isinstance(data, dict):
        # Para un diccionario, obtener las columnas y valores
        columns = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        cursor.execute(query, tuple(data.values()))
    else:
        # Para una lista o tupla de valores
        query = f"INSERT INTO {table} VALUES ({data})"
        cursor.execute(query)
        # Si no es ninguno de los anteriores, lanzar un error

    # Realiza la confirmación para aplicar los cambios
    conexion.commit()

    # Devuelve la cantidad de filas afectadas (debería ser 1 si la inserción fue exitosa)
    return cursor.rowcount

# # Ejemplos de uso
# insert_data('question_answers', {'question': '¿Cuál es tu nombre?', 'answer': 'Juan0'})
# # # O con un String
# insert_data('"pages.txt"', "'Google', 'google.com'")
# # insert_data('"pages.txt"', "'facebook', 'facebook.com'")
# insert_data('"pages.txt"', "'Gmail', 'gmail.com'")
# insert_data('"contacts.txt"', "'Jesús', '+526644714104'")
# # insert_data('"contacts.txt"', "'Yael', '+52663445465'")
# insert_data('"archivos.txt"', "'Conexion postgres', '~/Escritorio/clon3/Python-IA-Sara/Linux/conectar.py'")
# insert_data('"archivos.txt"', "'Super Mario 3 Cancion', '~/Escritorio/clon3/Python-IA-Sara/Linux/SuperMarioBros.mp3'")


def get_questions_answers():
    bot_list = []
    rows = get_table('question_answers')
    for row in rows:
        print(row)
        bot_list.extend(row)

    print(bot_list)
    return bot_list

# get_questions_answers()
# print(get_table('question_answers','id=1'))
# print(get_table_columns('question_answers'))
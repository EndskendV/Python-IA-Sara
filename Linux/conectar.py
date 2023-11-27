import mysql.connector

def create_connection():
    conexion = mysql.connector.connect(user = 'root', password='Galgos-2020', host='localhost', database='brain', port = '3307')
    return conexion

def get_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM question_answers")
    return cursor.fetchall()

bot_list = list()

def get_questions_answers():
    rows = get_table()
    for row in rows:
        print(row)
        bot_list.extend(list(row))
    return bot_list


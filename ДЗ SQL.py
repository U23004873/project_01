

# import sqlite3
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """CREATE TABLE Students (
# Students_Id INTEGER NOT NULL PRIMARY KEY,
# Students_Name TEXT NOT NULL,
# Place_Count INTEGER NOT NULL
# );
# """
# cursor.execute(query)
# connection.commit()
# connection.close() 

# import sqlite3
# connection = sqlite3.connect('teatchers.db')
# cursor = connection.cursor()
# query = """INSERT INTO Students (Students_Id , Students_Name , Place_Count)
# VALUES
# ('201', 'Иван', '1'),
# ('202', 'Петр', '2'),
# ('203', 'Анастасия', '3'),
# ('204', 'Игорь', '4');
# """
# cursor.execute(query)
# connection.commit()
# connection.close()

import sqlite3

def get_connection():
  connection = sqlite3.connect('teatchers.db')
  return connection

def close_connection(connection):
  if connection:
    connection.close()

def get_stydent_name(Students_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    select_query = """SELECT * FROM Students WHERE Students_Id = ?"""    
    cursor.execute(select_query,(Students_Id,))
    record = cursor.fetchone()
    close_connection(connection)
    return record[1]
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)


def get_school(Students_Id):
  try:
    school_name = get_stydent_name(Students_Id)
    connection = get_connection()
    cursor = connection.cursor()
    sql_select_query = """SELECT * FROM Students WHERE Students_Id = ?"""
    cursor.execute(sql_select_query, (Students_Id,))
    records = cursor.fetchall()
    print ("Студенты", school_name)
    for row in records:
      print ("ID студента: ", row[0])
      print ("Имя студента: ", row[1])
      print ("ID школы: ", row[2])
      print ("Название школы: ", school_name)
      
  except (Exception, sqlite3.Erorr) as erorr:
    print ("Ошибка в получении данных", erorr)

print ('Иинформацию о школе и студенте:')
get_school(201)
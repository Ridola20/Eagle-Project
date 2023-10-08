# from kivy.storage.jsonstore import JsonStore

# store = JsonStore("DataBase/User_Info.json")


import sqlite3 as sql 
from contextlib import closing

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(name, admission_number, classe, age, visuals, passed_out, security_pin):
    try:
        with closing(sql.connect ('DataBase/AccountLogin.db')) as sqliteConnection:
            with closing(sqliteConnection.cursor()) as cursor:
                print("Connected to SQLite\n")

                cursor.execute("""CREATE TABLE if not exists AccountLogin(student_id integer primary key AUTOINCREMENT, name text NOT NULL, admission_number int not null, class varchar(255) not null, age int not null, visuals BLOB, passed_out boolean not null, security_pin int not null)""")


                sqlite_insert_blob_query = """ INSERT INTO AccountLogin(name, admission_number, class, age, visuals, passed_out, security_pin) VALUES (?, ?, ?, ?, ?, ?, ?)"""

                empPhoto = convertToBinaryData(visuals)
                # Convert data into tuple format
                data_tuple = (name, admission_number, classe, age, empPhoto, passed_out, security_pin)
                cursor.execute(sqlite_insert_blob_query, data_tuple)
                sqliteConnection.commit()
                print("Image and file inserted successfully as a BLOB into a table")
    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")




with closing(sql.connect ('DataBase/AccountLogin.db')) as con:
    with closing(con.cursor()) as cur:
        c = cur.execute("""Select * from AccountLogin""")
        for i in c:
            print(i[0])
            print(i[1])
            print(i[2])
            print(i[3])
            print(i[4])
            print(i[6])
            print(i[7])

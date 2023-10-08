# from kivy.storage.jsonstore import JsonStore

# store = JsonStore("DataBase/User_Info.json")


import sqlite3 as sql 

# print("....................")

idsses = []
names = []
admission_numbers = []
classes = []
ages = []
visualses = []
passed_outs = []



def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def insertBLOB(ids, name, admission_number, classe, age, visuals, passed_out):
    try:
        sqliteConnection = sql.connect('DataBase/StdentsLogin.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite\n")

        cursor.execute("""CREATE TABLE if not exists StudentsLogin(id int primary key, name text NOT NULL, admission_number varchar(255) not null, class varchar(255) not null, age int not null, visuals BLOB, passed_out boolean)""")


        sqlite_insert_blob_query = """ INSERT INTO StudentsLogin(id, name, admission_number, class, age, visuals, passed_out) VALUES (?, ?, ?, ?, ?, ?, ?)"""

        empPhoto = convertToBinaryData(visuals)
        # Convert data into tuple format
        data_tuple = (ids, name, admission_number, classe, age, empPhoto, passed_out)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")

    except sql.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

# insertBLOB(1, "Smith", "E:\pynative\Python\photos\smith.jpg", "E:\pynative\Python\photos\smith_resume.txt")




int_id = 0

f = open("DataBase/students_txt_data/general.txt", "r")
fr = f.read()

frs = fr.split("|")
for i in frs:
    frss = i.split(",")
    # print(frss)
    idsses.append(frss[0])
    names.append(frss[1])
    admission_numbers.append(frss[2])
    classes.append(frss[3])
    ages.append(frss[4])
    visualses.append(frss[5])
    passed_outs.append(frss[6])

while int_id < len(idsses):
    ids = idsses[int_id]
    ids = ids.strip()
    ids = int(ids)

    name = names[int_id]
    name = name.strip()

    age = ages[int_id]
    age = age.strip()
    age = int(age)

    classe = classes[int_id]
    classe = classe.strip()

    admission_number = admission_numbers[int_id]
    admission_number = admission_number.strip()

    visual = visualses[int_id]
    visual = visual.strip()

    passed_out = passed_outs[int_id]
    passed_out = passed_out.strip()
    if passed_out == "True":
        passed_out = True
    elif passed_out == "False":
        passed_out = False


    data_organize = [int(ids), name, admission_number, classe, age, visual, passed_out]
    print(data_organize)
    print("\n")
    int_id+=1

    insertBLOB(int(ids), name, admission_number, classe, age, visual, passed_out)

# print(int(ids), name, admission_number, classe, age, visual, passed_out)

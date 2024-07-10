import mysql.connector
from mysql.connector import errorcode

count_user = 0

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "chinhdo09",
    database = "myproject"
)
mycursor = db.cursor()

def check_username_not_exited(username):
    sql = "SELECT * FROM information WHERE username = %s"
    val = username
    mycursor.execute(sql,(val,))
    results = mycursor.fetchall()
    if len(results) == 0:
        return True
    else:
        return False

def add_user(username, email, password):
    global count_user
    sql = "INSERT INTO information (id, username, email, password) VALUES (%s, %s, %s, %s)"
    val = (str(count_user), username, email, password)
    mycursor.execute(sql, val)
    db.commit()
    count_user += 1

def check_password(username, password):
    if check_username_not_exited(username) == False:
        sql = "SELECT password, id FROM information WHERE username = %s"
        val = username
        mycursor.execute(sql,(val,))
        results = list(mycursor.fetchall()[0])
        if password == results[0]:
            return int(results[1])
        else:
            return -1
    else:
        return -1

def take_password(username, email):
    if check_username_not_exited(username) == False and username != "admin":
        sql = "SELECT email, password FROM information WHERE username = %s"
        val = username
        mycursor.execute(sql,(val,))
        results = list(mycursor.fetchall()[0])
        if email == results[0]:
            return results[1]
        else:
            return 0
    return -1

def get_data():
    data = []
    sql = "SELECT id, username, email FROM information"
    mycursor.execute(sql)
    results = mycursor.fetchall()
    for x in results:
        a = {}
        a.update({"id": list(x)[0]})
        a.update({"username": list(x)[1]})
        a.update({"email": list(x)[2]})
        data.append(a)
    return data
get_data()   


        




    
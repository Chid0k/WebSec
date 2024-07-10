import mysql.connector
from mysql.connector import errorcode


def reset_db(database_name):
    try: 
        # check database exited
        db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "chinhdo09"
        )
        mycursor = db.cursor() # pointer to database
        mycursor.execute(f"SHOW DATABASES LIKE '{database_name}'")
        result = mycursor.fetchone() # tuple reulst of query
        if result: # database exited
            mycursor.execute(f"DROP DATABASE {database_name}") # reset
            mycursor.execute(f"CREATE DATABASE {database_name}")
            print("Create sucessfully")   
        else:
            mycursor.execute(f"CREATE DATABASE {database_name}")
    except:
        pass


reset_db("myproject")
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "chinhdo09",
    database = "myproject"
)
mycursor = db.cursor() # pointer to database
mycursor.execute("CREATE TABLE information (id int, username varchar(255), email varchar(255), password varchar(255))")

mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)
    

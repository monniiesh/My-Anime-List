import mysql.connector
from mysql.connector import Error
 

# Connect to MySQL database


try:

    cnx = mysql.connector.connect(host='localhost',
                                       user='root',
                                       password='imtheboss22')
    if cnx.is_connected():
        print('Connected to MySQL database\a')
 
except Error:
    print(Error)


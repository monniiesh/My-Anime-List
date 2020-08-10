#Creating the recquired data for Mysql code

dbname='Anime'
table={}
table['watched']= (
    "CREATE TABLE `watched` ("
    "  `No` int(11) AUTO_INCREMENT,"
    "  `Name` char(225),"
    "  `Date` char(225),"
    "  `No_Of_Episodes` int(3),"
    "  `Ratings` int(2),"
    "   PRIMARY KEY (`No`)"
    ")")
table['to_watch']=(
        " CREATE TABLE `to_watch`("
        " `No` int(11) AUTO_INCREMENT ,"
        " `Name` char(225),"
        " `No_Of_Episodes` int(3),"
        "  PRIMARY KEY (`No`) "
        ")")
        
# Creating Connection


import connection
from connection import cnx
loc=cnx.cursor()




# Checking If Database Exist
basic='''select schema_name from information_schema.schemata where schema_name = 'anime' '''
loc.execute(basic)
ans=loc.fetchall()

        
#Checking Database
        
if len(ans)==0:

        #Creating Database
        
        print('Creating Database')
        loc.execute("create database {}".format(dbname))
        loc.execute("use {}".format(dbname)) 


        for tab in table:

                print("Creating table {} ".format(tab))
                loc.execute(table[tab])

else:
        print('Opening Database')
        
	







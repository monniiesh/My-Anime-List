import os
import sys

PATH = os.path.dirname(os.path.realpath(__file__))
PATH = PATH + '\Save Files'
sys.path.append(PATH)

import Table
import mysql.connector
from time import sleep


print('\nHi! I am Your Assistant\n'
      'I hope you are doing well!\n'
      'I keep track of all the animes you have watched and the animes you wish to watch\n'
      'I can perform the following tasks\n'
      'Select 10 if you wish to know about me\n')


add_watched=(
    " INSERT INTO watched"
    "(Name, Date, No_Of_Episodes, Ratings)"
    "VALUES (%(name)s, %(date)s, %(eps)s, %(rate)s)"
    )

add_ToWatch=(
    "INSERT INTO to_watch"
    "(Name, No_Of_Episodes)"
    "VALUES (%(name)s, %(eps)s)"
    )


c=1
while c:
    sleep(0.7)
    print('\n1.Add Data To Watched Anime \n2.Add Data To Wish To Watch Anime \n3. View Watched Animes \n4. View To Watch Animes'
          '\n5. Count Number of Watched Animes \n6. Count Number of To Watch animes\n'
          '7. Search For A Anime In Watched Animes \n8. Search For A Anime That You Wish To Watch \n'
          '9. Close The Program \n')

    print('Please Select what you want me to do')      

    c=int(input('Enter option:'))
    print('\n')
    sleep(0.7)

    if c>0 and c<11:

        if c==1:
            cnx = mysql.connector.connect(host='localhost',
                                               user='root',
                                               password='imtheboss22',database='anime')
                                            
            loc=cnx.cursor() 


            infowatched={
                'name':input('Enter Anime Name:'),
                'date':input('Enter Date (dd/mm/yy):'),
                'eps':int(input('Enter No. Of Episodes:')),
                'rate':int(input('Enter Ratings(1-10):'))
                }
            
            loc.execute(add_watched, infowatched)

            print('I saved it in my memory')
            sleep(0.4)
      

            cnx.commit()
            loc.close()
            cnx.close()
            

            
        if c==2:
            cnx = mysql.connector.connect(host='localhost',
                                               user='root',
                                               password='imtheboss22',database='anime')
                                            
            loc=cnx.cursor() 
                        
            

            infotowatch={
                'name':input('Enter Anime Name:'),
                'eps':int(input('Enter No. Of Episodes:'))
                }

            loc.execute(add_ToWatch, infotowatch)

            print('I saved it in my memory')
            sleep(0.4)

            cnx.commit()
            loc.close()
            cnx.close()
        if c==3:
            cnx = mysql.connector.connect(host='localhost',
                                               user='root',
                                               password='imtheboss22',database='anime')
            loc=cnx.cursor() 
                        

            q='SELECT * FROM WATCHED'

            loc.execute(q)
            table=loc.fetchall()

            

            data=[('No.','Name','Date','No Of Episodes','Ratings')]
            for row in table:
                y=row
                data.append(y)

            dash='-'*83
            print('\nHere is the animes you have watched\n')
            
            for i in range(len(data)):
                if i==0:
                    print(dash)
                    print('{:<4s}{:<40s}{:<10s}{:>16s}{:>9s}'.format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
                    print(dash)
                else:
                    print('{:<4d}{:<40s}{:<10s}{:^16d}{:^9d}'.format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
            sleep(5)    
            cnx.commit()
            loc.close()
            cnx.close()

        if c==4:

            cnx = mysql.connector.connect(host='localhost',
                                                   user='root',
                                                   password='imtheboss22',database='anime')
            loc=cnx.cursor() 
                        

            q='SELECT * FROM TO_WATCH'

            loc.execute(q)
            table=loc.fetchall()

            

            data=[('No.','Name','No Of Episodes')]
            for row in table:
                y=row
                data.append(y)

            dash='-'*51
            
            print('\nHere is the animes you have planned to watch\n')
            for i in range(len(data)):
                if i==0:
                    print(dash)
                    print('{:<4s}{:<30s}{:>16s}'.format(data[i][0],data[i][1],data[i][2]))
                    print(dash)
                else:
                    print('{:<4d}{:<30s}{:^16d}'.format(data[i][0],data[i][1],data[i][2]))
            sleep(5)    
            cnx.commit()
            loc.close()
            cnx.close()

        if c==5:

           cnx = mysql.connector.connect(host='localhost',
                                                   user='root',
                                                   password='imtheboss22',database='anime')
           loc=cnx.cursor()

           q='SELECT COUNT(NAME) FROM WATCHED'

           loc.execute(q)
           data=loc.fetchall()
           print('\n')

           for row in data:
               print('No. of Watched Animes you have watched is', row[0])

           cnx.commit()
           loc.close()
           cnx.close()

        if c==6:

           cnx = mysql.connector.connect(host='localhost',
                                                   user='root',
                                                   password='imtheboss22',database='anime')
           loc=cnx.cursor()

           q='SELECT COUNT(NAME) FROM TO_WATCH'

           loc.execute(q)
           data=loc.fetchall()
           print('\n')

           for row in data:
               print('No. of animes you wish to watch', row[0])

           cnx.commit()
           loc.close()
           cnx.close()

        if c==7:

            cnx = mysql.connector.connect(host='localhost',
                                                   user='root',
                                                   password='imtheboss22',database='anime')
            loc=cnx.cursor()

            q='SELECT * FROM WATCHED'

            loc.execute(q)
            table=loc.fetchall()

            n=input('Enter the name of the anime:')

            data=[('No.','Name','Date','No Of Episodes','Ratings')]
            for row in table:
                y=row
                data.append(y)

            dash='-'*83
            
            
            for i in range(len(data)):
                if n==data[i][1]:
                    print(dash)
                    print('{:<4s}{:<40s}{:<10s}{:>16s}{:>9s}'.format(data[0][0],data[0][1],data[0][2],data[0][3],data[0][4]))
                    print(dash)
                    print('{:<4d}{:<40s}{:<10s}{:^16d}{:^9d}'.format(data[i][0],data[i][1],data[i][2],data[i][3],data[i][4]))
                    sleep(5)
                    break
                else:
                    print('Sorry!.....',"'",n,"'",'is Not Saved In My Memory!')
                    sleep(1)
            

            cnx.commit()
            loc.close()
            cnx.close()

        if c==8:

            cnx = mysql.connector.connect(host='localhost',
                                                   user='root',
                                                   password='imtheboss22',database='anime')
            loc=cnx.cursor()

            q='SELECT * FROM TO_WATCH'

            loc.execute(q)
            table=loc.fetchall()

            n=input('Enter the name of the anime:')

            data=[('No.','Name','No Of Episodes')]
            for row in table:
                y=row
                data.append(y)

            dash='-'*51
            
            
            for i in range(len(data)):
                if n==data[i][1]:
                    print(dash)
                    print('{:<4s}{:<30s}{:>16s}'.format(data[0][0],data[0][1],data[0][2]))
                    print(dash)
                    print('{:<4d}{:<30s}{:^16d}'.format(data[i][0],data[i][1],data[i][2]))
                    sleep(5)
                    break
            else:
                print('Sorry!.....',"'",n,"'",'is Not Saved In My Memory!')
                sleep(1)
                    
            cnx.commit()
            loc.close()
            cnx.close()

        if c==9:
            break


        if c==10:
            print('I am Your Assistant\n'
                  'I am created by Monniiesh Velmurugan\n'
                  'My creation was completed on 9th March 2019\n')
           
    else:
        print('\nSorry......I cant perform this operation\n')

print('I hope I was of great use to you!\nGood Bye!\n\a')
input()
            
        
        
        
        

        

















          
    
                            

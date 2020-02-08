import sqlite3

from Menu import Menu
"""
Build a Python application which stores the following example data in a SQLite database
Finally a program to celebrate the feats of Chainsaw Jugglers!!!
This program will . . .
    - Let users add a new row for a record holder.
    - Let user search for a record holder by name.
    - Let users update the number of catches for a record holder. 
Using SQLite for this. Just have to Create, Update and Read. 

"""
conn = sqlite3.connect('my_first_db.db') # Creates or opens database file

#Create a table if not exists. . 
conn.execute('create table if not exists heros (juggler text, country text, catches int)')
# Added some data

conn.execute('insert into heros values("Ben Dover" , "Thudland" , 42)')


conn.commit()

def main():

    while True:
        Menu.showMenu()



main()
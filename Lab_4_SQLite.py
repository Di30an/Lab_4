import sqlite3

"""
Build a Python application which stores the following example data in a SQLite database
Finally a program to celebrate the feats of Chainsaw Jugglers!!! 
Using SQLite for this. Just have to Create, Update and Read. 
Was originaly going to use a menu and allow for input. However you said not to spend over an hour
on this. 
"""
conn = sqlite3.connect('my_first_db.db') # Creates or opens database file

#Create a table if not exists. . 
conn.execute('create table if not exists heros (juggler text, country text, catches int)')
# Added some data
conn.execute('INSERT INTO heros values("Ben Dover" , "Thudland" , 42)')
conn.execute('INSERT INTO heros values("Mike Hunt" , "Barrtinia" , 77)')
conn.execute('INSERT INTO heros values("Landon Cider" , "Tzicaca" , 65)')

conn.execute(' UPDATE heros SET catches = 12 WHERE juggler ="Ben Dover"')

cur = conn.cursor()
cur.execute('SELECT * FROM heros WHERE juggler = "Landon Cider"')

rows = cur.fetchone()

print (rows)

conn.commit()

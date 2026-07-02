import sqlite3

import pandas as pd

conn=sqlite3.connect('sports.db')

conn.execute("DROP TABLE IF EXISTS Player;")

conn.execute("""CREATE TABLE Player (Player_Id INTEGER PRIMARY KEY, Player_Name TEXT NOT NULL UNIQUE, Team_Name TEXT NOT NULL, Jersey_Number INTEGER, Is_Captain TEXT DEFAULT 'No');""")
conn.commit()

print("Table created successfully!")
 
 
conn.execute("""INSERT INTO Player VALUES 
 (1, 'Aarav', 'Tigers', 7, 'Yes')")
 (2, 'Diya', 'Tigers', 10, 'No')
 (3, 'Kabir', 'Lions', 9, 'Yes')
 (4, 'Meera', 'Lions', 4, 'No')
 (5, 'Riya', 'Eagles', 11, 'No')
 (6, 'Arjun', 'Eagles');""")
conn.commit()

print("Rows inserted successfully!")
 

  
try:
    conn.execute("INSERT INTO Player VALUES (3, 'Aarav', 19;")
    conn.commit()
except Exception as e:
    conn.rollback()


arjun = pd.read_sql("""SELECT Player_Name, Team_Name, Is_Captain FROM Player WHERE Player_Name == 'Arjun';""", conn)
print(arjun)


nulls=pd.read_sql("""SELECT * FROM Player WHERE Jersey_Number IS NULL;""", conn)
print(nulls)


not_nulls=pd.read_sql("""SELECT * FROM Players WHERE Jersey_Number IS NOT NULL;""", conn)
print(not_nulls)

 

conn.close()
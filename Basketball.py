import sqlite3

database='basketball.sqlite'

conn=sqlite3.connect(database)
print("Opened database successfully")

import pandas as pd
table=pd.read_sql("""SELECT * FROM sqlite_master WHERE type='table';""", conn)

print(table)
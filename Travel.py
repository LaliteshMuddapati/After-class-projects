import sqlite3

import pandas as pd


conn=sqlite3.connect(':memory:')

conn.execute("""CREATE TABLE destination (destination_id INTGER PRIMARY KEY, destination_name TEXT NOT NULL UNIQUE, country TEXT NOT NULL);""")

conn.execute("""CREATE TABLE attraction (attraction_id INTEGER PRIMARY KEY, attraction_name TEXT NOT NULL UNIQUE, destination_id INTEGER);""")

conn.executemany("INSERT INTO destination VALUES (?, ?, ?)", [(1, 'Paris', 'France'), (2, 'Tokyo', 'Japan'), (3, 'Sydney', 'Australia'), (4, 'Rome', 'Italy'), (5, 'Cairo', 'Egypt'), (6, 'Dubai', 'UAE'),])

conn.executemany("INSERT INTO attraction VALUES (?, ?, ?)", [(1, 'Eiffel Tower', 1), (2, 'Louvre Museum', 1), (3, 'Tokyo Tower', 2), (4, 'Senso-ji Temple', 2), (5, 'Sydney Opera House', 3), (6, 'Colosseum', 4), (7, 'Trevi Fountain', 4),])

conn.commit()




destinations = pd.read_sql("SELECT * FROM destination", conn)
print(destinations)


attractions = pd.read_sql("SELECT * FROM attraction", conn)
print(attractions)


inner_join = pd.read_sql("SELECT destination.destination_name, attraction.destination_id FROM destination INNER JOIN attraction ON destination.destination_id = attraction.destination_id", conn)
print(inner_join)


left_join = pd.read_sql("SELECT destination.destination_name, destination.country, attraction.attraction_name FROM destination LEFT JOIN attraction ON destination.destination_id = attraction.destination_id", conn)
print(left_join)


cross_join = pd.read_sql("SELECT destination.destination_name, attraction.attraction_name FROM destination CROSS JOIN attraction WHERE destination.destination_id <= 2", conn)
print(cross_join)


union = pd.read_sql("SELECT destination_name AS d_name, 'destination' AS type FROM destination UNION SELECT attraction_name AS a_name,'attraction' AS type FROM attraction", conn)
print(union)



conn.close()
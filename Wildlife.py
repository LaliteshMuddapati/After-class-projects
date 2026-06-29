import sqlite3

import pandas as pd

conn = sqlite3.connect('wildlife.db')


conn.execute("""DROP TABLE IF EXISTS Animal;""")
conn.commit()

conn.execute("""DROP TABLE IF EXISTS Keeper;""")
conn.commit()

conn.execute("""DROP TABLE IF EXISTS Animal_Keeper;""")
conn.commit()

conn.execute("""CREATE TABLE Animal (Animal_Id INTEGER PRIMARY KEY, Animal_Name TEXT, Animal_Type TEXT, Habitat TEXT, Age INTEGER, Food_Kg REAL);""")
conn.commit()

conn.execute("""CREATE TABLE Keeper (Keeper_Id INTEGER PRIMARY KEY, Keeper_Name TEXT, Country TEXT);""")
conn.commit()

conn.execute("""CREATE TABLE Animal_Keeper (Animal_Id INTEGER, Keeper_Id INTEGER);""")
conn.commit()

conn.execute("""INSERT INTO Animal VALUES
  (1,'Leo','Mammal','Savannah',8,7.5),
  (2,'Maya','Mammal','Savannah',5,6.0),
  (3,'Ella','Bird','Rainforest',4,1.5),
  (4,'Rio','Bird','Rainforest',3,1.2),
  (5,'Tara','Reptile','Wetland',10,2.0),
  (6,'Max','Mammal','Forest',6,4.5),
  (7,'Nina','Mammal','Forest',2,3.0),
  (8,'Ollie','Bird','Wetland',7,1.8),
  (9,'Zara','Reptile','Desert',9,2.5),
  (10,'Ben','Mammal','Savannah',11,8.0),
  (11,'Kiwi','Bird','Forest',5,1.4),
  (12,'Rex','Reptile','Desert',6,2.2);""")
conn.commit()

conn.execute("""INSERT INTO Keeper VALUES
  (1,'Aarav', 'India'),
  (2,'Diya', 'India'),
  (3,'Meera', 'Kenya'),
  (4,'Kabir', 'Australia'),
  (5,'Riya', 'India');""")
conn.commit()

conn.execute("""INSERT INTO Animal_Keeper VALUES
  (1,1),(2,1),(3,2),(4,2),(5,3),
  (6,4),(7,4),(8,3),(9,5),(10,1);
""")
conn.commit()

print('Wildlife park database ready!')


types = pd.read_sql("""SELECT DISTINCT(Animal_Type) FROM Animal;""", conn)
print(types)


habitats = pd.read_sql("""SELECT DISTINCT(Habitat) FROM Animal;""", conn)
print(habitats)


age = pd.read_sql("""SELECT * FROM Animal ORDER BY Age DESC;""", conn)
print(age)


food = pd.read_sql("""SELECT * FROM Animal ORDER BY Food_Kg;""", conn)
print(food)


keepers = pd.read_sql("""SELECT * FROM Keeper ORDER BY Keeper_Name;""", conn)
print(keepers)


mammals = pd.read_sql("""SELECT COUNT(Animal_Id) FROM Animal WHERE Animal_Type == 'Mammal';""", conn)
print(mammals)


birds = pd.read_sql("""SELECT SUM(Food_Kg) FROM Animal WHERE Animal_Type == 'Bird';""", conn)
print(birds)


average_age = pd.read_sql("""SELECT AVG(Age) FROM Animal;""", conn)
print(average_age)


average_mammal_food = pd.read_sql("""SELECT AVG(Food_Kg) FROM Animal WHERE Animal_Type == 'Mammal';""", conn)
print(average_mammal_food)


animals_habitat = pd.read_sql("""SELECT Habitat, COUNT(Animal_Id) FROM Animal GROUP BY Habitat;""", conn)
print(animals_habitat)


average_age_per_habitat = pd.read_sql("""SELECT Habitat, AVG(Age) FROM Animal GROUP BY Habitat;""", conn)
print(average_age_per_habitat)


conn.close()
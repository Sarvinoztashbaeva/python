#here combination of 1 and 2 questions
import sqlite3

create_table = """CREATE TABLE IF NOT EXISTS Roster (
    Name TEXT,
    Species TEXT,
    Age INTEGER
    );"""

insert1 = """INSERT INTO Roster VALUES (
    'Benjamin Sisko',
    'Human',
    40
);"""
insert2 = """INSERT INTO Roster VALUES (
    'Jadzia Dax',
    'Trill',
    30
);"""
insert3 = """INSERT INTO Roster VALUES (
    'Kira Nerys',
    'Bajoran',
    29
);"""

connection = sqlite3.connect('info.db')
my_cursor = connection.cursor()
my_cursor.execute(create_table)
my_cursor.execute(insert1)
my_cursor.execute(insert2)
my_cursor.execute(insert3)
connection.commit()
connection.close()

connection = sqlite3.connect('info.db')
my_cursor = connection.cursor()
update_query = """UPDATE Roster
SET Name = 'Ezri Dax'
WHERE Name = 'Jadzia Dax';"""
my_cursor.execute(update_query)
connection.commit()
connection.close()

connection = sqlite3.connect('info.db')
my_cursor = connection.cursor()
select_query = """
SELECT Name, Age
FROM Roster
WHERE Species = 'Bajoran';
"""
my_cursor.execute(select_query)
results = cursor.fetchall()
for name, age in results:
    print(f'Name: {name}, Age: {age}')
connection.close()

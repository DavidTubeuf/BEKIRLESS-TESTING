import sqlite3
from Query import Query
from pathlib import Path
import os

my_file = Path("test2.db")
if my_file.is_file():
    os.remove("test2.db")

conn = sqlite3.connect('test2.db')
# Teste si la BDD est bien crée
assert my_file.is_file()

query = Query(conn)
c = conn.cursor()

query.create_tables()
# Teste si les tables PERSON, ITEM, et QUANTITY sont bien créées
c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND (name='PERSON' OR name='ITEM' OR name='QUANTITY') ''')
assert c.fetchone()[0]==3

# Teste que la personne Emma n'existe pas avant la création
assert query.person_exists("Emma") == False
query.insert_person("Emma")
# Teste que la personne Emma existe après la création
assert query.person_exists("Emma")

# Teste que la liste d'Emma est vide
assert query.get_list("Emma") == "Votre liste est vide."

# Teste que l'objet pomme n'existe pas avant la création
assert query.item_exists("Pomme") == False
query.insert_item("Pomme")
# Teste que l'objet pomme existe après la création
assert query.item_exists("Pomme")

# Teste que la personne Emma ne possède pas de pommes
assert query.quantity_exists("Emma", "Pomme") == False
query.insert_quantity("Emma", "Pomme", 2)
# Teste que la personne Emma possède bien 2 pommes
c.execute(''' SELECT qty FROM QUANTITY WHERE ITEMNAME='Pomme' AND PERSONNAME='Emma' ''')
assert c.fetchone()[0]==2

# Teste que la liste d'Emma contient 2 pommes
assert query.get_list("Emma") == "- 2 Pomme"

# Teste que la personne Emma possède bien 5 pommes
query.add_quantity("Emma", "Pomme", 3)
c.execute(''' SELECT qty FROM QUANTITY WHERE ITEMNAME='Pomme' AND PERSONNAME='Emma' ''')
assert c.fetchone()[0]==5

# Teste que la personne Emma possède bien 7 oranges
query.insert_quantity("Emma", "Orange", 7)
c.execute(''' SELECT qty FROM QUANTITY WHERE ITEMNAME='Orange' AND PERSONNAME='Emma' ''')
assert c.fetchone()[0]==7

# Teste que la liste d'Emma contient 5 pommes et 7 oranges
list = query.get_list("Emma")
assert "7 Orange" in list and "5 Pomme" in list

conn.close()
os.remove("test2.db")
print("Tests fonctionnels : OK")
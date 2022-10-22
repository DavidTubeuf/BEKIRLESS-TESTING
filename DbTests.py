import sqlite3
from Query import Query
from pathlib import Path
import os
import unittest

class DbTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_file = Path("test.db")
        if cls.my_file.is_file():
            os.remove("test.db")
        cls.conn = sqlite3.connect('test.db')
        cls.query = Query(cls.conn)
        cls.c = cls.conn.cursor()

    # Teste si la BDD est bien créée
    def test_01_db_creation(self):
        self.assertTrue(self.my_file.is_file(), "Database creation error")

    # Teste si les tables PERSON, ITEM, et QUANTITY sont bien créées
    def test_02_tables_creation(self):
        self.query.create_tables()
        self.c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND (name='PERSON' OR name='ITEM' OR name='QUANTITY') ''')
        self.assertTrue(self.c.fetchone()[0]==3, "Table creation error ")

    # Teste que la personne Emma n'existe pas avant la création 
    def test_03_person_dont_exists(self):
        self.assertFalse(self.query.person_exists("Emma"), "Person exists before insertion")

    # Teste que la personne Emma est bien insérée
    def test_04_insert_person(self):
        self.query.insert_person("Emma")
        self.c.execute("SELECT count(*) FROM PERSON WHERE name=\"Emma\"")
        self.assertTrue(self.c.fetchone()[0]==1, "The person is not correctly inserted")

    # Teste que la personne Emma existe après l'insertion
    def test_05_person_exists(self):
        self.assertTrue(self.query.person_exists("Emma"), "Person does not exist after insertion")

    # Teste que la liste d'Emma est vide
    def test_06_init_list_empty(self):
        self.assertTrue(self.query.get_list("Emma") == "Votre liste est vide.", "The list should be empty after creating a person")

    # Teste que l'objet pomme n'existe pas avant la création
    def test_07_item_dont_exists(self):
        self.assertFalse(self.query.item_exists("Pomme"), "Item exists before insertion")

    # Teste que l'objet pomme est bien inséré
    def test_08_insert_item(self):
        self.query.insert_item("Pomme")
        self.c.execute("SELECT count(*) FROM Item WHERE name=\"Pomme\"")
        self.assertTrue(self.c.fetchone()[0]==1, "The item is not correctly inserted")

    # Teste que l'objet pomme existe après l'insertion
    def test_09_item_exists(self):
        self.assertTrue(self.query.item_exists("Pomme"), "Item does not exist after insertion")

    # Teste que la personne Emma ne possède pas de pommes
    def test_10_quantity_dont_exists(self):
        self.assertFalse(self.query.quantity_exists("Emma", "Pomme"), "Quantity exists before insertion")

    # Teste que 2 pommes sont bien insérées pour Emma
    def test_11_insert_quantity(self):
        self.query.insert_quantity("Emma", "Pomme", 2)
        self.c.execute(''' SELECT qty FROM QUANTITY WHERE ITEMNAME='Pomme' AND PERSONNAME='Emma' ''')
        self.assertTrue(self.c.fetchone()[0]==2, "The quantity is not correctly inserted")    
    
    # Teste que la personne Emma possède des pommes après insertion
    def test_12_quantity_exists(self):
        self.assertTrue(self.query.quantity_exists("Emma", "Pomme"), "Quantity does not exist after insertion")

    # Teste que la liste d'Emma contient 2 pommes
    def test_13_list_display_one_item(self):
        self.assertTrue(self.query.get_list("Emma") == "- 2 Pomme", "The list should be have one item after inserting one item")

    # Teste que la personne Emma possède bien 5 pommes après l'ajout de 3 pommes
    def test_14_add_quantity(self):
        self.query.add_quantity("Emma", "Pomme", 3)
        self.c.execute(''' SELECT qty FROM QUANTITY WHERE ITEMNAME='Pomme' AND PERSONNAME='Emma' ''')
        self.assertTrue(self.c.fetchone()[0]==5, "Quantity is not correctly added")

    # Teste que la liste d'Emma contient 5 pommes et 7 oranges
    def test_15_list_display_multiples_items(self):
        self.query.insert_quantity("Emma", "Orange", 7)
        list = self.query.get_list("Emma")
        self.assertTrue("7 Orange" in list and "5 Pomme" in list, "The list does not have all previously added items")

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.remove("test.db")

if __name__ == '__main__':
    unittest.main()

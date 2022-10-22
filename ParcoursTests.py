import sqlite3
import unittest
from unittest import mock
from Query import Query
from unittest.mock import patch
from pathlib import Path
import os
from Main import app, get_correct_name, get_correct_action, get_correct_item, get_correct_quantity

class ParcoursTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.my_file = Path("parcours_test.db")
        if cls.my_file.is_file():
            os.remove("parcours_test.db")
        cls.conn = sqlite3.connect('parcours_test.db')
        cls.c = cls.conn.cursor()
        cls.query = Query(cls.conn)
        cls.query.create_tables()

    def test_01_person_creation_if_not_exists(self):

        assert not self.query.person_exists("David")

        with mock.patch('sys.stdout'):
            with mock.patch('Main.get_correct_name', return_value = "David"):
                with mock.patch('Main.get_correct_action', return_value = "3"):
                    app('parcours_test.db')

        assert self.query.person_exists("David")



    def test_02_print_empty_list_if_new_person_created(self):

        assert not self.query.person_exists("Tom")

        with mock.patch('sys.stdout') as fake_stdout:
            with mock.patch('Main.get_correct_name', return_value = "Tom"):
                with mock.patch('Main.get_correct_action', return_value = "3"):
                    app('parcours_test.db')

        fake_stdout.assert_has_calls([
            mock.call.write('Lien avec la base de données émis avec succès'),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('Quel est votre nom ?'),
            mock.call.write('\n'),
            mock.call.write('Bonjour, Tom'),
            mock.call.write('\n'),
            mock.call.write('Utilisateur créé'),
            mock.call.write('\n'),
            mock.call.write('Votre liste est vide.'),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('1 - Ajouter un élément dans votre liste'),
            mock.call.write('\n'),
            mock.call.write('2 - Afficher votre liste'),
            mock.call.write('\n'),
            mock.call.write("3 - Quitter l'application"),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('Quelle action souhaitez-vous effectuer ?'),
            mock.call.write('\n'),
            mock.call.write('\nA bientôt !'),
            mock.call.write('\n')
        ])



    def test_03_end_action_and_keyboard_interrupt_have_same_effect(self):

        with mock.patch('sys.stdout') as fake_stdout_action_end:
            with mock.patch('Main.get_correct_name', return_value = "Tom"):
                with mock.patch('Main.get_correct_action', return_value = "3"):
                    app('parcours_test.db')

        with mock.patch('sys.stdout') as fake_stdout_keyboard_interrupt:
            with mock.patch('Main.get_correct_name', return_value = "Tom"):
                with mock.patch('Main.get_correct_action', side_effect = KeyboardInterrupt):
                    app('parcours_test.db')

        list_prints = [mock.call.write('Lien avec la base de données émis avec succès'),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('Quel est votre nom ?'),
            mock.call.write('\n'),
            mock.call.write('Bonjour, Tom'),
            mock.call.write('\n'),
            mock.call.write('Voici votre liste :'),
            mock.call.write('\n'),
            mock.call.write('Votre liste est vide.'),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('1 - Ajouter un élément dans votre liste'),
            mock.call.write('\n'),
            mock.call.write('2 - Afficher votre liste'),
            mock.call.write('\n'),
            mock.call.write("3 - Quitter l'application"),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('Quelle action souhaitez-vous effectuer ?'),
            mock.call.write('\n'),
            mock.call.write('\nA bientôt !'),
            mock.call.write('\n')]

        fake_stdout_action_end.assert_has_calls(list_prints)
        fake_stdout_keyboard_interrupt.assert_has_calls(list_prints)



    def test_04_not_insert_item_if_action_canceled(self):
        
        assert not self.query.item_exists("banane")

        with mock.patch('sys.stdout'):
            with mock.patch('Main.get_correct_name', return_value = "Tom"):
                with mock.patch('Main.get_correct_action', return_value = "1"):
                    with mock.patch('Main.get_correct_item', return_value = "banane"):
                        with mock.patch('Main.get_correct_quantity', side_effect = KeyboardInterrupt):
                            app('parcours_test.db')


        assert not self.query.item_exists("banane")



    def test_05_insert_item_and_quantity_if_action_successful(self):
        
        assert not self.query.item_exists("banane")
        assert not self.query.quantity_exists("David", "banane")

        with mock.patch('sys.stdout'):
            with mock.patch('Main.get_correct_name', return_value = "David"):
                with mock.patch('Main.get_correct_action', side_effect = ["1", "3"]):
                    with mock.patch('Main.get_correct_item', return_value = "banane"):
                        with mock.patch('Main.get_correct_quantity', return_value = "12"):
                            app('parcours_test.db')


        assert self.query.item_exists("banane")
        assert self.query.quantity_exists("David", "banane")

    def test_06_print_list_if_known_person_with_a_list(self):

        assert self.query.person_exists("David")

        with mock.patch('sys.stdout') as fake_stdout:
            with mock.patch('Main.get_correct_name', return_value = "David"):
                with mock.patch('Main.get_correct_action', return_value = "3"):
                    app('parcours_test.db')

        fake_stdout.assert_has_calls([
            mock.call.write('Lien avec la base de données émis avec succès'),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('Quel est votre nom ?'),
            mock.call.write('\n'),
            mock.call.write('Bonjour, David'),
            mock.call.write('\n'),
            mock.call.write('Voici votre liste :'),
            mock.call.write('\n'),
            mock.call.write(self.query.get_list("David")),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('1 - Ajouter un élément dans votre liste'),
            mock.call.write('\n'),
            mock.call.write('2 - Afficher votre liste'),
            mock.call.write('\n'),
            mock.call.write("3 - Quitter l'application"),
            mock.call.write('\n'),
            mock.call.write('\n'),
            mock.call.write('Quelle action souhaitez-vous effectuer ?'),
            mock.call.write('\n'),
            mock.call.write('\nA bientôt !'),
            mock.call.write('\n')
        ])

    @classmethod
    def tearDownClass(cls):
        cls.conn.close()
        os.remove("parcours_test.db")

if __name__ == '__main__':
    unittest.main()
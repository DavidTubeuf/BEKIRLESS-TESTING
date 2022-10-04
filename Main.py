import sqlite3
from Query import Query
from pathlib import Path

my_file = Path("test.db")
exists = my_file.is_file()

conn = sqlite3.connect('test.db')
query = Query(conn)

print("Opened database successfully")

if not exists :
    query.create_tables()

"""
print(query.person_exists('Tom'))
query.insert_person('Tom')
print(query.person_exists('Tom'))

print(query.item_exists('aubergine'))
query.insert_item('aubergine')
print(query.item_exists('aubergine'))

print(query.quantity_exists('Tom', 'aubergine'))
query.insert_quantity('Tom', 'aubergine', 2)
print(query.quantity_exists('Tom', 'aubergine'))

query.add_quantity('Tom', 'aubergine', 3)
query.print_list('Tom')
"""

print("Quel est votre nom ?")
person_name = input()
print('Bonjour, ' + person_name)

if query.person_exists(person_name):
    print("Voici votre liste :")
    query.print_list(person_name)

else:
    query.insert_person(person_name)
    print("Utilisateur créé")
    print("Votre liste est vide.")

choice = ""

while choice != "3" and choice != "4":
    print("1 - Ajouter un élément dans votre liste")
    print("2 - Afficher votre liste")
    print("3 - Déconnexion")
    print("4 - Quitter l'application")
    choice = input()

    if choice == "1":
        print("Quel objet voulez-vous ajouter ?")
        item = input()
        if not query.item_exists(item):
            query.insert_item(item)
        print("Quelle quantité voulez-vous ajouter ?")
        quantity = input()
        if query.quantity_exists(person_name, item):
            query.add_quantity(person_name, item, quantity)
        else:
            query.insert_quantity(person_name, item, quantity)
        print("Bien ajouté !")

    elif choice == "2":
        print(query.get_list(person_name))

    elif choice == "3" or choice == "4":
        print("A bientôt !")

    else:
        print("Veuillez entrer 1, 2, 3, ou 4.")

conn.close()
from multiprocessing.sharedctypes import Value
import sqlite3
from Query import Query
from pathlib import Path
import time

def get_correct_name():
    name = input()
    try:
        int(name)
        print("Votre nom ne peut pas être un nombre")
        return ""
    except ValueError:
        pass
    
    if(len(name)) < 2:
        print("Votre nom doit faire au moins 2 caractères")
        return ""
    if(len(name)) > 20:
        print("Votre nom doit faire au plus 20 caractères, il en fait " + str(len(name)))
        return ""

    return name

def get_correct_action():
    action = input()
    if action not in ["1", "2", "3"]:
        print("Vous devez écrire 1, 2 ou 3 pour indiquer l'action à effectuer")
        return ""
    
    return action

def get_correct_item():
    item = input()
    try:
        int(item)
        print("L'objet à ajouter ne peut pas être un nombre")
        return ""
    except ValueError:
        pass
    
    if(len(item)) < 2:
        print("L'objet à ajouter doit faire au moins 2 caractères")
        return ""
    if(len(item)) > 20:
        print("L'objet à ajouter doit faire au plus 20 caractères, il en fait " + str(len(item)))
        return ""

    return item

def get_correct_quantity():
    quantity = input()
    try:
        int_qty = int(quantity)
    except ValueError:
        print("La quantité à ajouter doit être un nombre")
        return ""
    
    if int_qty <= 0:
        print("La quantité à ajouter doit être strictement positive")
        return ""
    if int_qty > 100:
        print("La quantité à ajouter doit être inférieure ou égale à 100")
        return ""

    return quantity

def main():

    my_file = Path("liste_course.db")
    exists = my_file.is_file()

    conn = sqlite3.connect('liste_course.db')
    query = Query(conn)

    print("Opened database successfully")

    if not exists :
        query.create_tables()

    person_name = ""
    while person_name == "":
        print("\nQuel est votre nom ?")
        person_name = get_correct_name()
    print('Bonjour, ' + person_name)

    if query.person_exists(person_name):
        liste = query.get_list(person_name)
        if liste == "":
            print("Votre liste est vide.")
        else:
            print("Voici votre liste :")
            print(query.get_list(person_name))

    else:
        query.insert_person(person_name)
        print("Utilisateur créé")
        print("Votre liste est vide.")

    action = ""

    while action != "3" :
        print("\n1 - Ajouter un élément dans votre liste")
        print("2 - Afficher votre liste")
        print("3 - Quitter l'application")
        action = ""
        while action == "":
            print("\nQuelle action souhaitez-vous effectuer ?")
            action = get_correct_action()

        if action == "1":
            # partie item
            item = ""
            while item == "":
                print("\nQuel objet voulez-vous ajouter ?")
                item = get_correct_item()
            
            if not query.item_exists(item):
                query.insert_item(item)

            # partie quantity
            quantity = ""
            while quantity == "":
                print("\nQuelle quantité voulez-vous ajouter ?")
                quantity = get_correct_quantity()

            if query.quantity_exists(person_name, item):
                query.add_quantity(person_name, item, quantity)
            else:
                query.insert_quantity(person_name, item, quantity)
            print("Bien ajouté !")
            time.sleep(1)

        elif action == "2":
            print(query.get_list(person_name))

        elif action == "3":
            print("A bientôt !")


    conn.close()

if __name__ == '__main__':
    main()
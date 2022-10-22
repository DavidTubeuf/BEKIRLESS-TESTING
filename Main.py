import sqlite3
from Query import Query
from pathlib import Path
import time

def get_correct_name():
    """
    Récupère le nom de l'utilisateur par l'utilisateur
    
    Renvoie une Assertion Error si :
     - le nom est un nombre
     - le nom fait moins de 2 caractères
     - le nom fait plus de 20 caractères

    Renvoie une Keyboard Interrupt si :
     - l'utilisateur entre CTRL + C
    """
    name = input()
    try:
        int(name)
        assert False, "le nom de l'utilisateur ne peut pas être un nombre"
    except:
        pass

    assert len(name) >= 2, "le nom de l'utilisateur doit faire au moins 2 caractères"
    assert len(name) <= 20, "le nom de l'utilisateur doit faire au plus 20 caractères, il en fait " + str(len(name))

    return name

def get_correct_action():
    """
    Récupère une action à effectuer par l'utilisateur

    Renvoie une Assertion Error si :
     - l'action n'est pas une string entre "1", "2" et "3"

    Renvoie une Keyboard Interrupt si :
     - l'utilisateur entre CTRL + C
    """
    action = input()
    assert action in ["1", "2", "3"], "l'action n'est pas celle attendue"

    return action

def get_correct_item():
    """
    Récupère un objet à ajouter par l'utilisateur

    Renvoie une Assertion Error si :
     - l'objet est un nombre
     - le nom de l'objet fait moins de 2 caractères
     - le nom de l'objet fait plus de 20 caractères

    Renvoie une Keyboard Interrupt si :
     - l'utilisateur entre CTRL + C
    """
    item = input()
    try:
        int(item)
        assert False, "le nom de l'objet à ajouter ne peut pas être un nombre"
    except:
        pass

    assert len(item) >= 2, "le nom de l'objet doit faire au moins 2 caractères"
    assert len(item) <= 20, "le nom de l'objet doit faire au plus 20 caractères, il en fait " + str(len(item))

    return item

def get_correct_quantity():
    """
    Récupère une quantité à ajouter par l'utilisateur

    Renvoie une Assertion Error si :
     - la quantité n'est pas un nombre
     - la quantité est négative ou nulle
     - la quantité est supérieure à 100

    Renvoie une Keyboard Interrupt si :
     - l'utilisateur entre CTRL + C
    """
    quantity = input()
    try:
        int_qty = int(quantity)
    except ValueError:
        assert False, "la quantité à ajouter doit être un nombre"
    
    assert int_qty > 0, "la quantité à ajouter doit être strictement positive"
    assert int_qty <= 100, "la quantité à ajouter doit être inférieure ou égale à 100"

    return quantity


def end_of_programm(conn):
    """
    Actions à effectuer quand l'utilisateur décide d'arrêter le programme
    """
    conn.close()
    print("\nA bientôt !")
    return

def app(db_name):

    # lien ou création de la base de données
    my_file = Path(db_name)
    exists = my_file.is_file()

    conn = sqlite3.connect(db_name)
    query = Query(conn)

    print("Lien avec la base de données émis avec succès")

    if not exists :
        query.create_tables()

    # récupération du nom de l'utilisateur
    print()
    person_name = ""
    while person_name == "":
        print("Quel est votre nom ?")
        try:
            person_name = get_correct_name()
        except AssertionError:
            print("\nVeuillez repréciser,")
        except KeyboardInterrupt:
            return end_of_programm(conn)

    # accueil et affichage de la liste de l'utilisateur
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

    # boucle principale
    action = ""
    while action != "3" :
        print()
        print("1 - Ajouter un élément dans votre liste")
        print("2 - Afficher votre liste")
        print("3 - Quitter l'application")

        # choix de l'action à effectuer
        print()
        action = ""
        while action == "":
            print("Quelle action souhaitez-vous effectuer ?")
            try:
                action = get_correct_action()
            except AssertionError:
                print("\nVeuillez repréciser,")
            except KeyboardInterrupt:
                return end_of_programm(conn)

        if action == "1":
            # choix de l'objet à ajouter dans sa liste
            print()
            item = ""
            while item == "":
                print("Quel objet voulez-vous ajouter ?")
                try:
                    item = get_correct_item()
                except AssertionError:
                    print("\nVeuillez repréciser,")
                except KeyboardInterrupt:
                    return end_of_programm(conn)

            # choix de la quantité à ajouter 
            print()
            quantity = ""
            while quantity == "":
                print("Quelle quantité voulez-vous ajouter ?")
                try:
                    quantity = get_correct_quantity()
                except AssertionError:
                    print("\nVeuillez repréciser,")
                except KeyboardInterrupt:
                    return end_of_programm(conn)

            if not query.item_exists(item):
                query.insert_item(item)

            if query.quantity_exists(person_name, item):
                query.add_quantity(person_name, item, quantity)
            else:
                query.insert_quantity(person_name, item, quantity)
            print("Bien ajouté !")

            time.sleep(1)

        elif action == "2":
            print(query.get_list(person_name))

    return end_of_programm(conn)

if __name__ == '__main__':
    app("liste_course.db")
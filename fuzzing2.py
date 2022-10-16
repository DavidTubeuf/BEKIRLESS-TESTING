import atheris
import mock
import sys
from Main import get_correct_name, get_correct_action, get_correct_item, get_correct_quantity

# Test the given name in input,
def fuzzing_name(name):
    try:
        int(name)
        #print("Votre nom ne peut pas être un nombre")
        return ""
    except ValueError:
        pass
    
    if(len(name)) < 2:
        #print("Votre nom doit faire au moins 2 caractères")
        return ""
    if(len(name)) > 20:
        #print("Votre nom doit faire au plus 20 caractères, il en fait " + str(len(name)))
        return ""
    return name

def fuzzing_action(action):
    if action not in ["1", "2", "3"]:
        #print("Vous devez écrire 1, 2 ou 3 pour indiquer l'action à effectuer")
        return ""
    
    return action

def fuzzing_item(item):
    try:
        int(item)
        #print("L'objet à ajouter ne peut pas être un nombre")
        return ""
    except ValueError:
        pass
    
    if(len(item)) < 2:
        #print("L'objet à ajouter doit faire au moins 2 caractères")
        return ""
    if(len(item)) > 20:
        #print("L'objet à ajouter doit faire au plus 20 caractères, il en fait " + str(len(item)))
        return ""

    return item

def fuzzing_quantity(quantity):
    try:
        int_qty = int(quantity)
    except ValueError:
        #print("La quantité à ajouter doit être un nombre")
        return ""
    
    if int_qty <= 0:
        #print("La quantité à ajouter doit être strictement positive")
        return ""
    if int_qty > 100:
        #print("La quantité à ajouter doit être inférieure ou égale à 100")
        return ""

    return quantity

#fuzzing name
print("Test fuzzing name")
atheris.Setup(sys.argv, fuzzing_name)
atheris.instrument_all();
atheris.Fuzz()
print()

#fuzzing action
print("Test fuzzing action")
atheris.Setup(sys.argv, fuzzing_action)
atheris.instrument_all();
atheris.Fuzz()
print()

#fuzzing item
print("Test fuzzing item")
atheris.Setup(sys.argv, fuzzing_item)
atheris.instrument_all();
atheris.Fuzz()
print()

#fuzzing quantity
print("Test fuzzing quantity")
atheris.Setup(sys.argv, fuzzing_quantity)
atheris.instrument_all();
atheris.Fuzz()

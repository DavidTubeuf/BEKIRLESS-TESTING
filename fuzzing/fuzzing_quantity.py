import atheris
import mock
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from Main import get_correct_quantity

# Test the given quantity in input,
def fuzzing(val):
    returned_value = ""
    with mock.patch('builtins.input', return_value=str(val)):
        try :
            returned_value = get_correct_quantity()
        except AssertionError as msg:
            msg = str(msg)
            assert(msg == "la quantité à ajouter doit être un nombre"
                   or msg == "la quantité à ajouter doit être strictement positive"
                   or msg == "la quantité à ajouter doit être inférieure ou égale à 100"
                    or returned_value == str(val))

#fuzzing quantity
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

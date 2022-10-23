import unittest
import atheris
import mock
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from Main import get_correct_name

# Test the given name in input,
def fuzzing(val):
    returned_value = ""
    with mock.patch('builtins.input', return_value=str(val)):
        try :
            returned_value = get_correct_name()
        except AssertionError as msg:
            print("")
#            assert(msg == "le nom de l'utilisateur ne peut pas être un nombre"
#                    or msg == "le nom de l'utilisateur doit faire au moins 2 caractères"
#                    or msg == "le nom de l'utilisateur doit faire au plus 20 caractères"
#                    or returned_value == str(val))

#fuzzing name
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

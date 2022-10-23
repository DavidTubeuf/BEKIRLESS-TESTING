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
    with mock.patch('builtins.input', return_value=val):
        try :
            returned_value = get_correct_name()
        except AssertionErrir as msg:
            assert(msg == "le nom de l'utilisateur ne peut pas être un nombre"
                    or msg == "name can't be less than 2 letter"
                    or msg == "name can't be more than 20 letter"
                    or returned_value == val)

#fuzzing name
atheris.Setup(sys.argv, f.fuzzing)
atheris.instrument_all();
atheris.Fuzz()

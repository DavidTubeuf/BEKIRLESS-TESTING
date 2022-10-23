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
    with self.assertRaises(Exception) as cm:
        with mock.patch('builtins.input', return_value=val):
            returned_value = get_correct_name()
    the_exception = cm.exception
    res = str(the_exception)
    assert(res == "le nom de l'utilisateur ne peut pas être un nombre"
           || res == "name can't be less than 2 letter"
           || res == "name can't be more than 20 letter"
           || returned_value == val)

#fuzzing name
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

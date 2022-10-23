import atheris
import mock
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from Main import get_correct_action

# Test the given action in input,
def fuzzing(val):
    returned_value = ""
    with mock.patch('builtins.input', return_value=str(val)):
        try :
            returned_value = get_correct_action()
        except AssertionError as msg:
            msg = str(msg)
            assert(msg == "l'action n'est pas celle attendue"
                    or returned_value == str(val))

#fuzzing action
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

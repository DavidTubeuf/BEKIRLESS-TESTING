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
    with mock.patch('builtins.input', return_value=val):
        result = get_correct_quantity()
        assert (result == "" or result == val)

#fuzzing quantity
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

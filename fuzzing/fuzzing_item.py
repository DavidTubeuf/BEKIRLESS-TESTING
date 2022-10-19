import atheris
import mock
import sys
import os
import inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir) 

from Main import get_correct_item

# Test the given item in input,
def fuzzing(val):
    with mock.patch('builtins.input', return_value=val):
        result = get_correct_item()
        assert (result == "" or result == val)

#fuzzing item
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

import atheris
import mock
import sys
from ../Main import get_correct_quantity

# Test the given quantity in input,
def fuzzing(val):
    with mock.patch('builtins.input', return_value=val):
        result = get_correct_quantity()
        assert (result == "" or result == val)

#fuzzing quantity
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

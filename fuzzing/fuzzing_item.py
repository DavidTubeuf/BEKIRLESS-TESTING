import atheris
import mock
import sys
from ../Main import get_correct_item

# Test the given item in input,
def fuzzing(val):
    with mock.patch('builtins.input', return_value=val):
        result = get_correct_item()
        assert (result == "" or result == val)

#fuzzing item
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

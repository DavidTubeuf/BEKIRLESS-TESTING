import atheris
import mock
import sys
from ../Main import get_correct_name

# Test the given name in input,
def fuzzing(val):
    with mock.patch('builtins.input', return_value=val):
        result = get_correct_name()
        assert (result == "" or result == val)

#fuzzing name
atheris.Setup(sys.argv, fuzzing)
atheris.instrument_all();
atheris.Fuzz()

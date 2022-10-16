import atheris
import mock
import sys
from Main import get_correct_name, get_correct_action, get_correct_item, get_correct_quantity

# Test the given name in input,
def test_get_correct_name(name):
    with mock.patch('builtins.input', return_value=name):
        result = get_correct_name()
        assert (result == "" or result == name)

# Test the given name in input,
def test_get_correct_action(action):
    with mock.patch('builtins.input', return_value=action):
        result = get_correct_action()
        assert (result == "" or result == action)

# Test the given name in input,
def test_get_correct_item(item):
    with mock.patch('builtins.input', return_value=item):
        result = get_correct_item()
        assert (result == "" or result == item)

# Test the given name in quantity,
def test_get_correct_quantity(item):
    with mock.patch('builtins.input', return_value=quantity):
        result = get_correct_quantity()
        assert (result == "" or result == quantity)

#fuzzing name
atheris.Setup(sys.argv, test_get_correct_name)
atheris.instrument_all();
atheris.Fuzz()

#fuzzing item
atheris.Setup(sys.argv, test_get_correct_item)
atheris.instrument_all();
atheris.Fuzz()

#fuzzing action
atheris.Setup(sys.argv, test_get_correct_action)
atheris.instrument_all();
atheris.Fuzz()

#fuzzing quantity
atheris.Setup(sys.argv, test_get_correct_quantity)
atheris.instrument_all();
atheris.Fuzz()

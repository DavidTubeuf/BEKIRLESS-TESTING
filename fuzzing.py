import atheris
import mock
import sys
from Main import get_correct_name, get_correct_action, get_correct_item, get_correct_quantity

# Test the given name in input,
def test_get_correct_name(name):
    with mock.patch('builtins.input', return_value=name):
        assert get_correct_name() == ""

# Test the given name in input,
def test_get_correct_action(action):
    with mock.patch('builtins.input', return_value=action):
        assert get_correct_action() == ""

# Test the given name in input,
def test_get_correct_item(item):
    with mock.patch('builtins.input', return_value=item):
        assert get_correct_item() == ""

atheris.Setup(sys.argv, test_get_correct_name)
atheris.instrument_all();
atheris.Fuzz()

#fuzzing name
atheris.Setup(sys.argv, test_get_correct_item)
atheris.instrument_all();
atheris.Fuzz()

#fuzzing action
atheris.Setup(sys.argv, test_get_correct_action)
atheris.instrument_all();
atheris.Fuzz()

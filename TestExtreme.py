import mock
import sys
from Main import get_correct_name, get_correct_action, get_correct_item, get_correct_quantity

# Test the given name in input,
# if naming incorrect return "" with a print of the problem,
# or else return the name
def test_get_correct_name():
    # Test if name is a number
    # should return "" with print saying "name should not be a number"
    with mock.patch('builtins.input', return_value="1"):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value=1234):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value=123456789101112131415):
        assert get_correct_name() == ""
    
    # Test if name length is less than 2
    # should return "" with print saying "name can't be less than 2 letter"
    with mock.patch('builtins.input', return_value=""):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value="p"):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value="@"):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value="."):
        assert get_correct_name() == ""

    # Test if name length is more than 20
    # should return "" with print saying "name can't be more than 20 letter"
    with mock.patch('builtins.input', return_value="thisIsAMoreThanEnoughLongName"):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value="thisIsANameTooLongWithNumber123"):
        assert get_correct_name() == ""
    with mock.patch('builtins.input', return_value=str(sys.maxsize)+"ab"):
        assert get_correct_name() == ""

    # Test with correct naming
    # should return the given name
    with mock.patch('builtins.input', return_value=str(sys.maxsize)+"a"):
        assert get_correct_name() == str(sys.maxsize)+"a"
    with mock.patch('builtins.input', return_value="abc"):
        assert get_correct_name() == "abc"
    with mock.patch('builtins.input', return_value="toto1"):
        assert get_correct_name() == "toto1"


# Test the given action in input, action here is a number,
# if action is incorrect return "" with a print of the problem,
# or else return the action
def test_get_correct_action():
    # Test with nothing or invalid action
    # should return "" with print saying "we should use one of the shown action"
    with mock.patch('builtins.input', return_value=""):
        assert get_correct_action() == ""
    with mock.patch('builtins.input', return_value=sys.maxsize+1):
        assert get_correct_action() == ""
    with mock.patch('builtins.input', return_value=2**63-1):
        assert get_correct_action() == ""
    with mock.patch('builtins.input', return_value=-sys.maxsize-2):
        assert get_correct_action() == ""
    with mock.patch('builtins.input', return_value="toto1"):
        assert get_correct_action() == ""

    # Test with correct action
    # should return the action
    with mock.patch('builtins.input', return_value="1"):
        assert get_correct_action() == "1"
    with mock.patch('builtins.input', return_value="2"):
        assert get_correct_action() == "2"
    with mock.patch('builtins.input', return_value="3"):
        assert get_correct_action() == "3"
        

# Test the given item in input,
# if item is incorrect return "" with a print of the problem,
# or else return the item
def test_get_correct_item():
    # Test if item is a number
    # should return "" with print saying "item should not be a number"
    with mock.patch('builtins.input', return_value="1"):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value=1234):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value=123456789101112131415):
        assert get_correct_item() == ""
    
    # Test if item length is less than 2
    # should return "" with print saying "item can't be less than 2 letter"
    with mock.patch('builtins.input', return_value=""):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value="p"):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value="@"):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value="."):
        assert get_correct_item() == ""

    # Test if item length is more than 20
    # should return "" with print saying "item can't be more than 20 letter"
    with mock.patch('builtins.input', return_value="thisIsAMoreThanEnoughLongName"):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value="thisIsANameTooLongWithNumber123"):
        assert get_correct_item() == ""
    with mock.patch('builtins.input', return_value=str(sys.maxsize)+"ab"):
        assert get_correct_item() == ""

    # Test with correct item naming
    # should return the given item
    with mock.patch('builtins.input', return_value=str(sys.maxsize)+"a"):
        assert get_correct_item() == str(sys.maxsize)+"a"
    with mock.patch('builtins.input', return_value="abc"):
        assert get_correct_item() == "abc"
    with mock.patch('builtins.input', return_value="toto1"):
        assert get_correct_item() == "toto1"


# Test the given quantity in input,
# if quantity is incorrect return "" with a print of the problem,
# or else return the quantity
def test_get_correct_quantity():
    # Test with nothing or invalid quantity
    # should return "" with print saying "quantity should be a number"
    with mock.patch('builtins.input', return_value=""):
        assert get_correct_quantity() == ""
    with mock.patch('builtins.input', return_value=sys.maxsize+1):
        assert get_correct_quantity() == ""
    with mock.patch('builtins.input', return_value=2**63-1):
        assert get_correct_quantity() == ""
    with mock.patch('builtins.input', return_value=0):
        assert get_correct_quantity() == ""
    with mock.patch('builtins.input', return_value=-sys.maxsize-2):
        assert get_correct_quantity() == ""
    with mock.patch('builtins.input', return_value="toto1"):
        assert get_correct_quantity() == ""

    # Test with correct quantity
    # should return the quantity
    with mock.patch('builtins.input', return_value=1):
        assert get_correct_quantity() == 1
    with mock.patch('builtins.input', return_value=25):
        assert get_correct_quantity() == 25
    with mock.patch('builtins.input', return_value=50):
        assert get_correct_quantity() == 50
    with mock.patch('builtins.input', return_value=75):
        assert get_correct_quantity() == 75
    with mock.patch('builtins.input', return_value=100):
        assert get_correct_quantity() == 100


test_get_correct_name()
test_get_correct_action()
test_get_correct_item()
test_get_correct_quantity()

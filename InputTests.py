import unittest
import mock
import sys
from Main import get_correct_name, get_correct_action, get_correct_item, get_correct_quantity

class InputTests(unittest.TestCase):
    
    # Test the given name in input,
    # if naming incorrect return an assert error with the problem,
    # or else return the name
    def test_get_correct_name(self):
        
        # Test if name is a number
        # should return an assert error saying "name should not be a number"
        msgNum = "le nom de l'utilisateur ne peut pas être un nombre"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="1"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="1234"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="123456789101112131415"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        # Test if name length is less than 2
        # should return an assert error saying "name can't be less than 2 letter"
        msgLess = "le nom de l'utilisateur doit faire au moins 2 caractères"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=""):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="p"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="@"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="."):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)

        # Test if name length is more than 20
        # should return an assert error saying "name can't be more than 20 letter"
        msgMore = "le nom de l'utilisateur doit faire au plus 20 caractères"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="thisIsAMoreThanEnoughLongName"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="thisIsANameTooLongWithNumber123"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=str(sys.maxsize)+"ab"):
                get_correct_name()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)

        # Test with correct naming
        # should return the given name
        with mock.patch('builtins.input', return_value=str(sys.maxsize)+"a"):
            assert get_correct_name() == str(sys.maxsize)+"a"
        with mock.patch('builtins.input', return_value="abc"):
            assert get_correct_name() == "abc"
        with mock.patch('builtins.input', return_value="toto1"):
            assert get_correct_name() == "toto1"



    # Test the given action in input, action here is a number,
    # if action is incorrect return an assert error with the problem,
    # or else return the action
    def test_get_correct_action(self):
         
        # Test with nothing or invalid action
        # should return an assert error saying "we should use one of the shown action"
        msgAction = "l'action n'est pas celle attendue"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=""):
                get_correct_action()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgAction)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=sys.maxsize+1):
                get_correct_action()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgAction)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=2**63-1):
                get_correct_action()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgAction)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=-sys.maxsize-2):
                get_correct_action()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgAction)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="toto1"):
                get_correct_action()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgAction)
        
        # Test with correct action
        # should return the action
        with mock.patch('builtins.input', return_value="1"):
            assert get_correct_action() == "1"
        with mock.patch('builtins.input', return_value="2"):
            assert get_correct_action() == "2"
        with mock.patch('builtins.input', return_value="3"):
            assert get_correct_action() == "3"
       

    # Test the given item in input,
    # if item is incorrect return an assert error with the problem,
    # or else return the item
    def test_get_correct_item(self):
        
        # Test if item is a number
        # should return an assert error saying "item should not be a number"
        msgNum = "le nom de l'objet à ajouter ne peut pas être un nombre"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="1"):
                get_correct_item()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="1234"):
                get_correct_item()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="123456789101112131415"):
                get_correct_item()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)
        
        # Test if item length is less than 2
        # should return an assert error saying "item can't be less than 2 letter"
        msgLess = "le nom de l'objet doit faire au moins 2 caractères"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=""):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)
        
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="p"):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)
        
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="@"):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)
        
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="."):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)
        
        # Test if item length is more than 20
        # should return an assert error saying "item can't be more than 20 letter"
        msgMore = "le nom de l'objet doit faire au plus 20 caractères"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="thisIsAMoreThanEnoughLongName"):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)
        
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="thisIsANameTooLongWithNumber123"):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)
        
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value=str(sys.maxsize)+"ab"):
                assert get_correct_item() == ""
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)
        
        # Test with correct item naming
        # should return the given item
        with mock.patch('builtins.input', return_value=str(sys.maxsize)+"a"):
            assert get_correct_item() == str(sys.maxsize)+"a"
        with mock.patch('builtins.input', return_value="abc"):
            assert get_correct_item() == "abc"
        with mock.patch('builtins.input', return_value="toto1"):
            assert get_correct_item() == "toto1"

    
    # Test the given quantity in input,
    # if quantity is incorrect return an assert error with the problem,
    # or else return the quantity
    def test_get_correct_quantity(self):
        
        # Test with invalid quantity
        # should return an assert error saying "quantity should be a number"
        msgNum = "la quantité à ajouter doit être un nombre"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="a"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="abcd"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="abcdefghijklmnopqrstuvwxyz"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgNum)

        # Test with number below 0
        # should return an assert error saying "quantity should be above 0"
        msgLess = "la quantité à ajouter doit être strictement positive"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="0"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgLess)
        
        # Test with number above 100
        # should return an assert error saying "quantity should be below 100"
        msgMore = "la quantité à ajouter doit être inférieure ou égale à 100"
        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="101"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="115"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)

        with self.assertRaises(Exception) as cm:
            with mock.patch('builtins.input', return_value="100000"):
                get_correct_quantity()
        the_exception = cm.exception
        self.assertEqual(str(the_exception),msgMore)

        # Test with correct quantity
        # should return the quantity
        with mock.patch('builtins.input', return_value="1"):
            assert get_correct_quantity() == "1"
        with mock.patch('builtins.input', return_value="25"):
            assert get_correct_quantity() == "25"
        with mock.patch('builtins.input', return_value="50"):
            assert get_correct_quantity() == "50"
        with mock.patch('builtins.input', return_value="75"):
            assert get_correct_quantity() == "75"
        with mock.patch('builtins.input', return_value="100"):
            assert get_correct_quantity() == "100"

if __name__ == '__main__':
    unittest.main()


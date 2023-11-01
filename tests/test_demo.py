"""Demo test cases
"""
import unittest

def add(value1: int, value2: int) ->int:
    """Adding two numbers

    Args:
        value1 (int): integer value
        value2 (int): integer value

    Returns:
        int: return result in integer
    """
    return value1 + value2

class TestPlanet(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_add(self):
        """_summary_
        """
        value1 = 10
        value2 = 10
        result = add(value1, value2)
        self.assertEqual(result, 20)

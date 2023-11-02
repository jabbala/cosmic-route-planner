"""
RocketData Module

This module defines the RocketData class, which is responsible for encapsulating data 
related to the rocket sprite used in the interstellar environment. It includes attributes 
to manage the rocket's original sprite, the current sprites as well as the dimensions of the rocket.

"""
import unittest
from src.rocket_data import RocketData

class TestRocketData(unittest.TestCase):
    """
    Test cases for the RocketData class.

    This test suite includes test cases for the RocketData class, 
    which is responsible for managing data associated
    with the rocket sprite used in the interstellar environment.

    """

    def setUp(self):
        """
        Set up an instance of the RocketData class for testing.

        This method creates an instance of the RocketData class 
        before running each test case to ensure a clean testing environment.

        """
        self.rocket_data = RocketData()

    def test_initialization(self):
        """
        Test the initialization of RocketData.

        This test case checks that the orig_sprite_rocket,  sprite_rocket, rocket_width,
        and rocket_height attributes of the RocketData class are initially set to None.

        """
        self.assertIsNotNone(self.rocket_data.orig_sprite_rocket)
        self.assertIsNotNone(self.rocket_data.sprite_rocket)
        self.assertIsNotNone(self.rocket_data.rocket_width)
        self.assertIsNotNone(self.rocket_data.rocket_height)

if __name__ == '__main__':
    unittest.main()

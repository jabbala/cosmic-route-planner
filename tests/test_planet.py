"""Test case for planet.py's Plant class """
import unittest
from src.planet import Planet

class TestPlanet(unittest.TestCase):
    """Test case for the Planet class.

    This test case checks the attributes of the Planet class and ensures 
    that they are correctly initialized.

    Methods:
        test_planet_attributes: Checks if the Planet attributes 
        are set correctly.
        test_planet_default_attributes: Checks if the Planet attributes 
        have the correct default values.
    """

    def test_planet_attributes(self):
        """
        Test if the Planet class attributes are set correctly.
        """
        # Create a planet instance
        pos = (100, 200)
        color = (255, 0, 0)
        planet = Planet(pos, color)

        # Check if attributes match the expected values
        self.assertEqual(planet.pos, pos)
        self.assertEqual(planet.color, color)

    def test_planet_default_attributes(self):
        """
        Test if the Planet class attributes have the correct default values.
        """
        # Create a planet instance with default attributes
        planet = Planet((0, 0), (0, 0, 0))

        # Check if attributes match the default values
        self.assertEqual(planet.pos, (0, 0))
        self.assertEqual(planet.color, (0, 0, 0))

if __name__ == '__main__':
    unittest.main()

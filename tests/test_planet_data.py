"""Planet Data test cases
"""
import unittest
from src.planet_data import PlanetData
from src.planet import Planet

class TestPlanetData(unittest.TestCase):
    """Test cases for the PlanetData class.

    This test suite includes test cases for the PlanetData class, which is responsible for
    managing data associated with planets and their interstellar connections
    in the interstellar environment.

    """
    def setUp(self):
        """
        Set up an instance of the PlanetData class for testing.

        This method creates an instance of the PlanetData class before running 
        each test case to ensure a clean testing environment.

        """
        self.planet_data = PlanetData()

    def test_initialization(self):
        """
        Test the initialization of PlanetData.

        This test case checks that the planets and connections attributes of the 
        PlanetData class are initially empty after class initialization.

        """
        self.assertEqual(self.planet_data.planets, [])
        self.assertEqual(self.planet_data.connections, [])

    def test_add_planet(self):
        """
        Test adding a planet to PlanetData.

        This test case creates a sample planet, adds it to the PlanetData instance, 
        and checks if the planet is in the list of planets.

        """
        # Create a sample planet
        sample_planet = Planet((10, 20), (255, 0, 0))

        # Add the planet to the PlanetData instance
        self.planet_data.planets.append(sample_planet)

        # Check if the planet is in the list of planets
        self.assertIn(sample_planet, self.planet_data.planets)

    def test_add_connection(self):
        """
        Test adding a connection to PlanetData.

        This test case creates two sample planets, adds them to the PlanetData instance, 
        creates a sample connection, adds it to the PlanetData instance, and checks if the 
        connection is in the list of connections.

        """
        # Create two sample planets
        planet1 = Planet((10, 20), (255, 0, 0))
        planet2 = Planet((30, 40), (0, 0, 255))

        # Add the planets to the PlanetData instance
        self.planet_data.planets.append(planet1)
        self.planet_data.planets.append(planet2)

        # Create a sample connection
        sample_connection = [(planet1.pos[0], planet1.pos[1]), (planet2.pos[0], planet2.pos[1])]

        # Add the connection to the PlanetData instance
        self.planet_data.connections.append(sample_connection)

        # Check if the connection is in the list of connections
        self.assertIn(sample_connection, self.planet_data.connections)

if __name__ == '__main__':
    unittest.main()

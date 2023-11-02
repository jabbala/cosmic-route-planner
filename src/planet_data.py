class PlanetData:
    """Encapsulate data related to planets and interstellar connections.

    This class is responsible for managing data associated with planets 
    and their interstellar connections in the interstellar environment. 
    It includes attributes for storing planet objects and tracking connections between them.

    Attributes:
        - planets (list): A list of planet objects in the environment.
        - connections (list): A list of interstellar connections between planets.

    Example:
        # Create a PlanetData instance
        planet_data = PlanetData()

        # Add a new planet to the environment
        planet = Planet(position, color)
        planet_data.planets.append(planet)

        # Record a connection between two planets
        planet1 = planet_data.planets[0]
        planet2 = planet_data.planets[1]
        connection = [(planet1.pos[0], planet1.pos[1]), (planet2.pos[0], planet2.pos[1])]
        planet_data.connections.append(connection)
    """
    def __init__(self):
        self.planets = []
        self.connections = []

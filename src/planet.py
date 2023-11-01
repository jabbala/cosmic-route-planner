"""planet.py - Planet Class Module

This module defines the `Planet` class, which represents celestial bodies in the interstellar environment.
Each instance of the `Planet` class contains information about a planet's position and color.

Classes:
    - Planet: Represents a planet with its position and color.

Usage:
    from planet import Planet

Example:
    # Creating a new planet instance
    planet = Planet((x, y), (r, g, b))

    # Accessing planet attributes
    position = planet.pos
    color = planet.color

Author: Your Name
Date: Date of creation or last modification
"""

class Planet:
    """
    Represents a celestial body within the interstellar environment.

    Attributes:
        pos (tuple): A tuple representing the (x, y) position of the planet.
        color (tuple): A tuple representing the RGB color of the planet.

    Methods:
        None

    Example:
        # Creating a new planet instance
        planet = Planet((100, 200), (255, 0, 0))

        # Accessing planet attributes
        position = planet.pos  # (100, 200)
        color = planet.color  # (255, 0, 0)
    """

    def __init__(self, pos, color):
        self.pos = pos
        self.color = color
    
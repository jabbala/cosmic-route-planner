"""planet.py - Planet Class Module

This module defines the `Planet` class, which represents celestial
bodies in the interstellar environment. Each instance of the `Planet`
class contains information about a planet's position and color.

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

class Planet():
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

    def __init__(self, pos:int, color:int)->None:
        self.pos = pos
        self.color = color
    def set_poos(self, pos:int)->None:
        """set_pos is a setter method for variable pos

        Args:
            pos (int): position
        """
        self.pos = pos
    def get_pos(self)->int:
        """get_pos is a getter method for pos variable

        Returns:
            int: position
        """
        return self.pos
    def set_color(self, color:int)->None:
        """set_color is a setter method for color attribute/variable

        Args:
            color (int): color value
        """
        self.color = color
    def get_color(self)->None:
        """get_color is a getter method for color attribute/variable

        Returns:
            int: color value
        """
        return self.color
    
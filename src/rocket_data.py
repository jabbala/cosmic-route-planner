"""
RocketData Module

This module defines the RocketData class, which is responsible for 
encapsulating data related to the rocket sprite used in the interstellar environment. 
It includes attributes to manage the rocket's original sprite, the current sprite,
as well as the dimensions of the rocket.

"""
import pygame as pg
class RocketData:
    """
    Encapsulate data related to the rocket sprite.

    This class is responsible for managing data associated with 
    the rocket sprite used in the interstellar environment. It includes attributes for 
    the original sprite, the current sprite, as well as the dimensions of the rocket.

    Attributes:
        - orig_sprite_rocket (pygame.Surface): The original rocket sprite.
        - sprite_rocket (pygame.Surface): The current rocket sprite.
        - rocket_width (int): The width of the rocket sprite in pixels.
        - rocket_height (int): The height of the rocket sprite in pixels.

    Example:
        # Create a RocketData instance
        rocket_data = RocketData()

        # Set the original rocket sprite
        rocket_data.orig_sprite_rocket = pg.image.load('rocket.png')

        # Access the dimensions of the rocket sprite
        width = rocket_data.rocket_width
        height = rocket_data.rocket_height
    """
    def __init__(self):
        self.orig_sprite_rocket = pg.image.load('./images/rocket.png')
        self.sprite_rocket = self.orig_sprite_rocket
        self.rocket_width = self.sprite_rocket.get_rect().size[0]
        self.rocket_height = self.sprite_rocket.get_rect().size[1]

"""_summary_
"""
import sys
import numpy as np
import pygame as pg
from planet import Planet
from planet_data import PlanetData
from rocket_data import RocketData
class Environment():
    """Simulate an interstellar environment for cosmic route planning.

    This class represents an environment where a rocket can navigate between planets.
    It provides methods for initializing the environment, visualizing the journey,
    editing planet positions, rotating sprites, taking steps,
    and resetting the environment.

    Attributes:
        - width (int): The width of the screen in pixels.
        - height (int): The height of the screen in pixels.
        - planet_radius (int): The radius of planets in pixels.
        - planets (list): A list of planet objects in the environment.
        - connections (list): A list of interstellar connections between planets.
        - screen (pygame.Surface): The screen for displaying the environment.
        - orig_sprite_rocket (pygame.Surface): The original rocket sprite.
        - sprite_rocket (pygame.Surface): The current rocket sprite.
        - rocket_width (int): The width of the rocket sprite in pixels.
        - rocket_height (int): The height of the rocket sprite in pixels.
        - rotation (int): The rotation angle of the rocket sprite.
        - sprite_background (pygame.Surface): The background image of space.
        - rocket_speed (int): The speed of the rocket in pixels per step.
        - rocket_pos (list): The current position of the rocket [x, y].
        - current_pos (int): The index of the current planet position for the rocket.

    Methods:
        - draw_screen(view): Draw the environment with the specified view.
        - edit(): Allow editing the planet positions by clicking on the screen.
        - rotate_center(sprite, angle): Rotate a sprite image around its center.
        - step(action, view): Perform a step in the interstellar journey.
        - reset(): Reset the interstellar environment to its initial state.

    Example:
        # Create an environment instance
        env = Environment()

        # Perform actions...

        # Reset the environment
        env.reset()
    """
    def __init__(self):
        self.width = 600
        self.height = 600
        self.planet_radius = 10
        self.planet_data = PlanetData()
        self.rocket_data = RocketData()
        self.screen = pg.display.set_mode((self.width, self.height))
        self.rotation = 0
        self.sprite_background = pg.image.load('./images/space.jpg')
        self.sprite_background = pg.transform.smoothscale(
                self.sprite_background, (self.width, self.height)
            )
        self.rocket_speed = 10
        self.rocket_pos = [-50] * 2
        self.current_pos = 0
        self.draw_screen('none')
        self.edit()
    def draw_screen(self, view):
        """draw screen for the given view parameter

        Args:
            view (str): view - none/normal/beautiful
        """
        self.screen.fill((0,0,0))
        self.screen.blit(self.sprite_background, (0,0))
        if view == 'normal':
            for index, _ in enumerate(self.planet_data.connections):
                pg.draw.line(
                    self.screen,
                    (255, 255,0),
                    self.planet_data.connections[index][0],
                    self.planet_data.connections[index][1],
                    3
                )
        elif view == 'beautiful':
            for index, _ in enumerate(self.planet_data.connections):
                pg.draw.line(
                    self.screen,
                    (255, 255,0),
                    self.planet_data.connections[index][0],
                    self.planet_data.connections[index][1],
                    3
                )
        else:
            pass
        for planet in self.planet_data.planets:
            pg.draw.circle(self.screen, planet.color, planet.pos, self.planet_radius)
        self.screen.blit(
            self.rocket_data.sprite_rocket,
            (
                self.rocket_pos[0] - self.rocket_data.rocket_width/2,
                self.rocket_pos[1] - self.rocket_data.rocket_height/2
            )
        )
        pg.display.flip()
    def edit(self):
        """TODO: Write a detailed docstring for this function.
        """
        while True:
            position = pg.mouse.get_pos()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    color = (
                        np.random.randint(0, 256),
                        np.random.randint(0, 256),
                        np.random.randint(0, 256)
                    )
                    planet = Planet(position, color)
                    self.planet_data.planets.append(planet)
                elif event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        return
            self.draw_screen('none')
        print("Inside edit function")
    def rotate_center(self, sprite, angle):
        """Rotate a sprite image around its center.

        This method takes a sprite image and rotates it around its center
        by the specified angle. The rotated sprite maintains the same dimensions
        as the original sprite.

        Args:
            sprite (pygame.Surface): The sprite image to be rotated.
            angle (float): The angle (in degrees) by which to rotate the sprite.

        Returns:
            pygame.Surface: The rotated sprite image.

        Example:
            # Load a sprite image
            sprite_image = pg.image.load('rocket.png')

            # Rotate the sprite by 90 degrees
            rotated_sprite = self.rotate_center(sprite_image, 90)
        """
        sprite_rect = sprite.get_rect()
        rot_sprite = pg.transform.rotate(sprite, angle)
        sprite_rect.center = rot_sprite.get_rect().center
        rot_sprite = rot_sprite.subsurface(sprite_rect)
        return rot_sprite
    def step(self, action, view):
        """Perform a step in the interstellar journey.

        This method simulates the rocket's movement between planets and calculates
        the distance traveled. It may also update the interstellar connections
        and display the journey on the screen, depending on the specified view mode.

        Args:
            action (int): The index of the destination planet to travel to.
            view (str): The view mode, which can be 'normal' or 'beautiful'.

        Returns:
            float: The distance traveled between the current planet and the destination planet.

        Example:
            # Create an environment instance
            env = Environment()

            # Perform a step in the interstellar journey
            distance_traveled = env.step(1, 'normal')
        """
        p1_x = self.planet_data.planets[self.current_pos].pos[0]
        p1_y = self.planet_data.planets[self.current_pos].pos[1]
        p2_x = self.planet_data.planets[action].pos[0]
        p2_y = self.planet_data.planets[action].pos[1]
        distance = pow(pow(p1_x - p2_x, 2) + pow(p1_y - p2_y, 2), 0.5)
        if view in ['normal', 'beautiful']:
            self.planet_data.connections.append([(p1_x, p1_y), (p2_x, p2_y)])
            self.draw_screen(view)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        if view == 'beautiful':
            reached = False
            self.rocket_pos[0] = p1_x
            self.rocket_pos[1] = p1_y
            diff_x = p1_x - p2_x
            diff_y = p1_y - p2_y
            t_value = diff_y/(diff_x + 1e-12)
            x_value = pow(pow(self.rocket_speed, 2) / (pow(t_value, 2) + 1), 0.5)
            y_value = x_value * abs(t_value)
            if diff_y > 0:
                y_value = -y_value
            if diff_x > 0:
                x_value = -x_value
            if (x_value <= 0 and y_value <= 0) or (x_value <= 0 and y_value >= 0):
                angle = np.rad2deg(np.arctan(-t_value) + np.pi/2)
            else:
                angle = np.rad2deg(np.arctan(-t_value) - np.pi/2)
            if diff_x == 0:
                angle += 180
            self.rocket_data.sprite_rocket = self.rocket_data.orig_sprite_rocket
            self.rocket_data.sprite_rocket = self.rotate_center(self.rocket_data.sprite_rocket, angle)
            while not reached:
                self.rocket_pos[0] += x_value
                self.rocket_pos[1] += y_value
                distance = pow(
                    pow(self.rocket_pos[0] - p2_x, 2) + pow(self.rocket_pos[1] - p2_y, 2)
                    , 0.5)
                if distance < self.planet_radius or (diff_x == 0 and diff_y == 0):
                    self.rocket_pos[0] = p2_x
                    self.rocket_pos[1] = p2_y
                    reached = True
                pg.time.wait(50)
                self.draw_screen(view)
        self.current_pos = action
        return distance
    def reset(self):
        """Reset the interstellar environment to its initial state.

        This method clears the existing connections between planets,
        resets the current position of the rocket to the first planet,
        and positions the rocket off-screen as it starts a new
        interstellar journey.

        Attributes:
            - connections (list): A list of planet
                                connections to be cleared.
            - current_pos (int): The current position of the rocket,
                                set to the index of the first planet (0).
            - rocket_pos (list): The position of the rocket, set to
                                [-50, -50] to place it off-screen.

        Returns:
            None

        Example:
            # Create an environment instance
            env = Environment()

            # Perform actions...

            # Reset the environment
            env.reset()
        """
        self.planet_data.connections.clear()
        self.current_pos = 0
        self.rocket_pos = [-50] * 2
if __name__=="__main__":
    env = Environment()
    
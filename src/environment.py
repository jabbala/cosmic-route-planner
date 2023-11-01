"""_summary_
"""
import pygame as pg

class Environment():
    """TODO: Write a detailed docstring for this function.
    """
    def __init__(self):
        self.width = 600
        self.height = 600
        self.screen = pg.display.set_mode((self.width, self.height))
        self.draw_screen()
    def draw_screen(self):
        """draw screen for the given view parameter

        Args:
            view (str): view - none/normal/beautiful
        """
        self.screen.fill((0,0,0))
        pg.display.flip()
    def edit(self):
        """TODO: Write a detailed docstring for this function.
        """
        print("Inside edit function")
    def rotate_center(self):
        """TODO: Write a detailed docstring for this function.
        """
        print("Inside rotate center function")
    def step(self):
        """TODO: Write a detailed docstring for this function.
        """
        print("Inside step function")
    def reset(self):
        """TODO: Write a detailed docstring for this function.
        """
        print("Inside reset function")
if __name__=="__main__":
    env = Environment()
    
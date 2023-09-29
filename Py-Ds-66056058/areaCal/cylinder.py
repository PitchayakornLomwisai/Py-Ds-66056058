
from math import pi
from areaCal.shape import Shape
class Cylindervol(Shape):
    """
    This is the Cylindervol class. It represents a cylinder and calculates its volume.

    Attributes:
        radius (float): The radius of the cylinder's base.
        height (float): The height of the cylinder.

    Methods:
        volume(): Calculate the volume of the cylinder.
    """
    def __init__(self, radius, height):
        """
        Initialize a Cylindervol object with a given radius and height.

        Args:
            radius (float): The radius of the cylinder's base.
            height (float): The height of the cylinder.
        """
        self.radius = radius
        self.height = height

    def volume(self):
        """
        Calculate the volume of the cylinder using the formula: pi * radius^2 * height.

        Returns:
            float: The volume of the cylinder.
        """
        return pi * self.radius**2 * self.height

    def __str__(self):
        """
        Calculate the volume of the cylinder using the formula: pi * radius^2 * height.

        Returns:
            float: The volume of the cylinder.
        """
        return f'Cylinder Volume with radius {self.radius} and height {self.height}: {self.volume()}'



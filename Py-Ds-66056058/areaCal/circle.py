from areaCal.shape import Shape


class Circle(Shape):
    """
   This is the Circle class. It represents a circle and calculates its area.

   Attributes:
       radius (float): The radius of the circle.

   Methods:
       area(): Calculate the area of the circle.
   """
    def __init__(self, radius):
        """
        Initialize a Circle object with a given radius.

        Args:
            radius (float): The radius of the circle.
        """
        self.cir_area = 0.0
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle using the formula: pi * radius^2.

        Returns:
            float: The area of the circle.
        """
        self.cir_area = self.radius * self.radius * 3.14
        return self.cir_area

    def __str__(self) -> str:
        """
        Get a string representation of the Circle object.

        Returns:
            str: A string describing the circle's radius and area.
        """
        return 'Circle Area of ' + str(self.radius) + 'U :' + str(self.area())
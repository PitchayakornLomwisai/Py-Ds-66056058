from areaCal.shape import Shape


class Square(Shape):
    """
    This is the Square class. It represents a square and calculates its area.

    Attributes:
        width (float): The width of the square.

    Methods:
        area(): Calculate the area of the square.
    """
    def __init__(self, width):
        """
        Initialize a Square object with a given width.

        Args:
            width (float): The width of the square.
        """
        self.sqr_area = 0.0
        self.width = width

    def area(self):
        """
        Calculate the area of the square using the formula: width * width.

        Returns:
            float: The area of the square.
        """
        self.sqr_area = self.width * self.width
        return self.sqr_area

    def __str__(self) -> str:
        """
        Get a string representation of the Square object.

        Returns:
            str: A string describing the square's width and area.
        """
        return 'Square Area of ' + str(self.width) + 'U :' + str(self.area())


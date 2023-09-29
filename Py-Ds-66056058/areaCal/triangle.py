from areaCal.shape import Shape


class Triangle(Shape):
    """
        This is the Triangle class. It represents a triangle and calculates its area.

        Attributes:
            width (float): The width of the triangle's base.
            height (float): The height of the triangle.

        Methods:
            area(): Calculate the area of the triangle.
        """
    def __init__(self, width, height):
        """
        Initialize a Triangle object with a given width (base) and height.

        Args:
            width (float): The width (base) of the triangle.
            height (float): The height of the triangle.
        """
        self.width = width
        self.height = height
        self.tri_area = 0.0

    def __str__(self):
        """
        Get a string representation of the Triangle object.

        Returns:
            str: A string describing the triangle's width, height, and area.
        """
        return ('Triangle Area of '
                + str(self.width) + 'Ux' + str(self.height)
                + 'U :' + str(self.area()))
    def area(self):
        """
        Calculate the area of the triangle using the formula: (width * height) / 2.

        Returns:
            float: The area of the triangle.
        """
        self.tri_area = self.width * self.height * 0.5
        return self.tri_area
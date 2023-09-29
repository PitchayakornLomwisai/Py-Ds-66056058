from areaCal.shape import Shape


class Rectangle(Shape):
    """
        This is the Rectangle class. It represents a rectangle and calculates its area.

        Attributes:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Methods:
            area(): Calculate the area of the rectangle.
        """
    def __init__(self, width, height) -> None:
        """
        Initialize a Rectangle object with a given width and height.

        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        """
        self.width = width
        self.height = height
        self.rect_area = 0.0

    def __str__(self) -> str:
        """
        Get a string representation of the Rectangle object.

        Returns:
            str: A string describing the rectangle's width, height, and area.
        """

        return ('Rectangle Area of '
                + str(self.width) + 'Ux' + str(self.height)
                + 'U :' + str(self.area()))

    def area(self):
        """
        Calculate the area of the rectangle using the formula: width * height.

        Returns:
            float: The area of the rectangle.
        """
        self.rect_area = self.width * self.height
        return self.rect_area


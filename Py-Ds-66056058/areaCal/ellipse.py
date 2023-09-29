from areaCal.shape import Shape


class Ellipse(Shape):
    """
    This is the Ellipse class. It represents an ellipse and calculates its area.

    Attributes:
        radius1 (float): The first radius of the ellipse.
        radius2 (float): The second radius of the ellipse.

    Methods:
        area(): Calculate the area of the ellipse.
    """
    def __init__(self, ra1, ra2):
        """
    This is the Ellipse class. It represents an ellipse and calculates its area.

    Attributes:
        radius1 (float): The first radius of the ellipse.
        radius2 (float): The second radius of the ellipse.

    Methods:
        area(): Calculate the area of the ellipse.
    """
        self.ell_area = 0.0
        self.radius1 = ra1
        self.radius2 = ra2

    def area(self):
        """
        Calculate the area of the ellipse using the formula: pi * radius1 * radius2.

        Returns:
            float: The area of the ellipse.
        """
        self.ell_area = self.radius1 * self.radius2 * 3.14
        return self.ell_area

    def __str__(self) -> str:
        """
        Calculate the area of the ellipse using the formula: pi * radius1 * radius2.

        Returns:
            float: The area of the ellipse.
        """
        return 'Ellipse Area of ' + str(self.radius1) + 'Ux' + str(self.radius2) + 'U :' + str(self.area())

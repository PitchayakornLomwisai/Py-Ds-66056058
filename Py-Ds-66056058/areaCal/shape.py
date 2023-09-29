#%%
class Shape:
    """
    This is the Shape class. It represents a generic shape with an area calculation.

    Methods:
        area(): Calculate the area of the shape.
    """
    def __str__(self):
        """
        Get a string representation of the Shape object.

        Returns:
            str: A string describing the shape and its area.
        """
        return 'Blank Shape with ' + str(self.area()) + ' unit'

    def area(self):
        """
        Calculate the area of the shape. This method should be overridden by subclasses.

        Returns:
            float: The area of the shape.
        """
        return 0.0



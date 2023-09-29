
# area_calc.py
#%%
from areaCal.circle import Circle
from areaCal.square import Square
from areaCal.rectangle import Rectangle
from areaCal.triangle import Triangle
from areaCal.cylinder import Cylindervol


if __name__ == '__main__':

    rectangle_input = Rectangle(5,10)
    print(rectangle_input)
    circle_input = Circle(2)
    print(circle_input)

    square_input = Square(5)
    print(square_input)

    triangle_input = Triangle(2,2)
    print(triangle_input)

    cylinder_input = Cylindervol(5, 10)
    print(cylinder_input)







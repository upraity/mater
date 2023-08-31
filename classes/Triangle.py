class triangle:
    def _init_(tri, base, height):
        tri.base   = base
        tri.height = height
        tri.side1  = side1
        tri.side2  = side2
        tri.side3  = side3

    def _repr_(tri):
        return "Triangle base: " + str(tri.base) + ", height: " + str(tri.height) + "a:" + str(tri.side1) + ",b:" + str(tri.side2) + ",c:" + str(tri.side1)

    def set_base(tri, new_base):
        tri.base = new_base

    def set_height(tri, new_height):
        tri.height = new_height

    def set_side1(tri, new_side1):
        tri.side1 = new_side1

    def set_side2(tri, new_side2):
        tri.side2 = new_side2

    def set_side3(tri, new_Side3):
        tri.side3 = new_side3

    def base(tri):
        return tri.base

    def height(tri):
        return tri.height

    def side1(tri):
        return tri.side1

    def side2(tri):
        return tri.side2

    def side3(tri):
        return tri.side3

    def area(tri):
        return (tri.base * tri.height * 0.5)

    def perimeter(tri):
        return tri.side1 + tri.side2 + tri.side3

    def is_equalateral_triangle(tri):
        return tri.side1 == tri.side2 == tri.side3 == a

    def area_equalateral_tri(tri):
        return (a*a*1.731)/4

    def perimeter_equalateral_tri(tri):
        return 3*a

class Triangle:
    def __init__(tri, base, height):
        tri.base   = base
        tri.height = height

    def __repr__(tri):
        return "Triangle base: " + str(tri.base) + ", height: " + str(tri.height) 

    def set_base(tri, new_base):
        tri.base = new_base

    def set_height(tri, new_height):
        tri.height = new_height

    def base(tri):
        return tri.base

    def height(tri):
        return tri.height

    def area(tri):
        return (tri.base * tri.height * 0.5)


class Cube:
    def __init__(cube, side):
        cube.__side = side

    def __repr__(cube):
        return "<Cube side=" + cube.__side + ">"

    def set_side(cube, side):
        cube.__side = side

    def suface_area(cube):
        return (cube.__side**2)*6

    def volume(cube):
        return cube.__side**3
    
    def __eq__(cube, other_cube):
        return cube.volume() == other_cube.volume()
    
    def __ne__(cube, other_cube):
        return cube.volume() != other_cube.volume()

    def __lt__(cube, other_cube):
        return cube.volume() < other_cube.volume()
    
    def __gt__(cube, other_cube):
        return cube.volume() > other_cube.volume()
    
    def __le__(cube, other_cube):
        return cube.volume() <= other_cube.volume()
    
    def __ge__(cube, other_cube):
        return cube.volume() >= other_cube.volume()

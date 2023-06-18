class Square:
    def __init__(square, side):
        square.side_ = side
    
    def __repr__(square):
        return "<Square side=" + str(square.side_) + ">"
    
    def set_side(square, new_side):
        square.side_ = new_side
    
    def side(square):
        return square.side_
    
    def diagonal(square):
        return ((square.side_**2)*2)**0.5
    
    def perimeter(square):
        return square.side_ * 4
    
    def area(square):
        return square.side_ * square.side_
    
    def is_perfect(square):
        return square.area() == int(square.area())**2
    
    def __eq__(square, other_square):
        return square.area() == other_square.area()
    
    def __lt__(square, other_square):
        return square.area() < other_square.area()
    
    def __gt__(square, other_square):
        return square.area() > other_square.area()
    
    def __le__(square, other_square):
        return square.area() <= other_square.area()
    
    def __ge__(square, other_square):
        return square.area() >= other_square.area()
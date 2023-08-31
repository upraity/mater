class Rectangle:
    def __init__(rect, lenght, width):
        rect.lenght_ = lenght
        rect.width_ = width
    
    def __repr__(rect):
        return "<Recctangle lenght=" + str(rect.lenght_) + " width=" + str(rect.width_) + ">"
    
    def set_lenght(rect, new_lenght):
        rect.lenght_ = new_lenght
    
    def set_width(rect, new_width):
        rect.width_  = new_width
    
    def lenght(rect):
        return rect.lenght_
    
    def width(rect):
        return rect.width_
    
    def diagonal(rect):
        return (rect.lenght_**2 + rect.width_**2)**0.5
    
    def perimeter(rect):
        return 2 * (rect.lenght_ + rect.width_)
    
    def area(rect):
        return rect.lenght_ * rect.width_
    
    def is_square(rect):
        return rect.lenght_ == rect.width
    
    def __eq__(rect, other_rect):
        return rect.area() == other_rect.area()
    
    def __lt__(rect, other_rect):
        return rect.area() < other_rect.area()
    
    def __gt__(rect, other_rect):
        return rect.area() > other_rect.area()
    
    def __le__(rect, other_rect):
        return rect.area() <= other_rect.area()
    
    def __ge__(rect, other_rect):
        return rect.area() >= other_rect.area()

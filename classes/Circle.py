class Circle:
    def __init__(circle, radius):
        circle.radius_ = radius
    
    def __repr__(circle):
        return "<Circle radius=" + str(circle.radius_) + ">"
    
    def set_radius(circle, new_radius):
        circle.radius_ = new_radius
    
    def radius(circle):
        return circle.radius_
    
    def diameter(circle):
        return 2 * circle.radius_
    
    def perimeter(circle):
        return 2 * (22/7) * circle.radius_
    
    def area(circle):
        return (22/7) * circle.radius_ * circle.radius_
    
    def semicircle(circle):
        return SemiCircle(circle.radius_) 
    
    def __eq__(circle, other_circle):
        return circle.area() == other_circle.area()
    
    def __lt__(circle, other_circle):
        return circle.area() < other_circle.area()
    
    def __gt__(circle, other_circle):
        return circle.area() > other_circle.area()
    
    def __le__(circle, other_circle):
        return circle.area() <= other_circle.area()
    
    def __ge__(circle, other_circle):
        return circle.area() >= other_circle.area()
class SemiCircle:
    def __init__(semic, radius):
        semic.radius_ = radius
    
    def __repr__(semic):
        return "<Semicircle radius=" + str(semic.radius_) + ">"
    
    def set_radius(semic, new_radius):
        semic.radius_ = new_radius
    
    def radius(semic):
        return semic.radius_
    
    def diameter(semic):
        return 2 * semic.radius_
    
    def perimeter(semic):
        return (22/7) * semic.radius_ + semic.radius_ * 2
    
    def area(semic):
        return (22/7/2) * semic.radius_ * semic.radius_
    
    def circle(semic):
        return Circle(semic.radius_)
    
    def __eq__(semic, other_semic):
        return semic.area() == other_semic.area()
    
    def __lt__(semic, other_semic):
        return semic.area() < other_semic.area()
    
    def __gt__(semic, other_semic):
        return semic.area() > other_semic.area()
    
    def __le__(semic, other_semic):
        return semic.area() <= other_semic.area()
    
    def __ge__(semic, other_semic):
        return semic.area() >= other_semic.area()
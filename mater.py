#Mater

#A math librery..
#Always in devlopment...


def is_prime(num: int) -> bool:
    """Return the num is prime or not"""
    if num < 2: return False
    for i in range(2, num//2+1):
        if not num % i : return False
    return True

def factorial(n: int) -> int:
    """Return factorial for n. Defined as, n! = n * (n-1) * (n-2) ... (2) * (1)."""
    f = 1
    while n:
        f*=n
        n-=1
    return f

def alternative_factorial(n: int) -> int:
    """Return alternative factorial of n. Defined as, alternatingfactorial(n) =  n! - (n-1)! + (n-2)! - (n-3)!"... (1)!."""
    af = 0
    for k in range(1, n+1):
        af += ((-1)**(n-k)) * factorial(k)
    return af

def double_factorial(n: int) -> int:
    """Return double factorial of n. Defined as n!! = (n)(n-2)(n-4)....(2) for even, (n)(n-2)(n-4)....(1) for odd."""
    df = 1
    while n > 0:
        df *= n
        n -= 2
    return df

def super_factorail(n: int) -> int:
    """Return Super factorial of n. Defined as, superfactorial(n) = (n)! * (n-1)! * (n-2)! ... (2)! * (1)!."""
    sf = 1
    while n:
        sf *= factorial(n)
        n -= 1
    return sf

def hyper_factorail(n: int) -> int:
    """Return Hyper Factorial of n. Defined as, hyperfactorial(n) = (n**n) * ((n-1)**(n-1)) * ((n-2)**(n-2)) ... (2**2) * (1**1)."""
    hf = 1
    while n:
        hf *= n**n
        n -= 1
    return hf

def ultra_factorial(n: int) -> int:
    """Return Ultra factorial of n. Defined as, n!**n!."""
    return factorial(n)**factorial(n)

def primorial(n: int) -> int:
    """Return primorial of n"""
    p = 1
    for i in range(n+1):
        if is_prime(i):
            p *= i
    return p

def ultra_primorial(n):
    """Return Ultra primorial of n. Defined as, n# ** n#"""
    return primorial(n)**primorial(n)

def pow(x: int,  y: int) -> int:
    """Return x raised to the power if y"""
    return x**y

def sqrt(x: int) -> float:
    """Return square root of x in int if x in a perfect square else float"""
    return x**0.5

def is_palindrome(num: int) -> bool:
    """Return the num is Palindrome or not"""
    r = 0
    t = num
    while t > 0:
        r = (r * 10) + t % 10
        t//=10
    return r == num

def average(*nums) -> float:
    """Find the average of given numbers"""
    return sum(nums) / len(nums)

def cbrt(n: int) -> float:
    """Return cube root of given number"""
    return n ** (1/3)

def xroot(n: int, x: int) -> float:
    """Return x root n"""
    return n ** (1/x)

def dpfactors(n: int) -> list[int]:
    """Return a list of distnic prime factors of n"""
    dpf = []
    d = 2
    while n > 1:
        if not n % d:
            if d not in dpf: dpf.append(d)
            n //= d
        else:
            d += 1
    return dpf

def is_power_of2(n) -> bool:
    """Return the given number id power of two or not"""
    return not (n & (n-1))

def floor(x) -> int:
    """Return the floor of x as Itigral"""
    return int(x // 1)

def is_even(n: int) -> bool:
    """Return the number n is even or not"""
    return n & 1 == 0

def is_odd(n: int) -> bool:
    """Return the number n is odd or not"""
    return n & 1 == 1

def is_armstrong(n: int) -> bool:
    """Cheak the given number is armstrong number or not"""
    p = len(str(n))
    t = n
    s = 0
    while t > 0:
        s += (t % 10)**p
        t //= 10
    return n == s

def divisors(n: int) -> set[int]:
    """Return the set of proper divisors of n"""
    d = {1, n}
    for i in range(2, n//2+1):
        if not n % i:
            d.add(i)
    return d

def is_amicables(n: int, m: int) -> bool:
    """Cheak the give number pair is amicabel pair or not"""
    return sum(divisors(n))-n == m and sum(divisors(m))-m == n

def quadratic_roots(a,b,c) -> (float, float):
    """Return roots for given quardic ecuation by shridharacharya method. Input coefficients of the equation"""
    return (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a), (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)

def ackermann(m: int, n: int) -> int:
    """Ackermann function"""
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))


#Classes


#Class Square

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


#Class Rectanlge

class Rectangle:
    def __init__(rect, lenght, width):
        rect.lenght_ = lenght
        rect.width_ = width
    
    def __repr__(rect):
        return "<Recctangle lenght=" + str(rect.lenght_) + " width=" + str(rect.width_) + ">"
    
    def set_lenght(rect, new_lwnght):
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


#Class Circle

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


#SemiCircle

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
 
 
#Matrix 

class Matrix:
    
    def __init__(matrix, nums: list[list[int, float]]):
        if not all(len(nums[0]) == len(l) for l in nums):
            raise Exception("Invalid Matrix formate")
        
        matrix.rows = len(nums)
        matrix.columns = len(nums[0])
        matrix.shape = (matrix.rows, matrix.columns)
        matrix.values = nums
        
    def __str__(matrix):
        return str(matrix.values).replace(" ", "").replace("[[", "").replace("],[", "\n").replace(",", " ").replace("]]", "")
    
    def __repr__(matrix):
        return "<Matrix object " + str(matrix.rows) + "x" + str(matrix.columns) +  ">"
            
    def __eq__(matrix, B):
        return matrix.values == B.values
    
    def __add__(matrix, B):
        if matrix.shape != B.shape:
            raise Excaption("Matrix can't be added of defrent sizes.")
        C = Matrix([[0]*B.columns for _ in range(B.rows)])
        for i in range(C.rows):
            for j in range(C.columns):
                C.values[i][j] = matrix.values[i][j] + B.values[i][j]
        return C
    
    def __min__(matrix, B):
        if matrix.shape != B.shape:
            raise Excaption("Matrix can't be added of defrent sizes.")
        C = Matrix([[0]*B.columns for _ in range(B.rows)])
        for i in range(C.rows):
            for j in range(C.columns):
                C.values[i][j] = matrix.values[i][j] - B.values[i][j]
        return C
    
    def __mul__(matrix, B):
        if type(B) == type(0):
            C = Matrix([[0]*matrix.rows for _ in range(matrix.columns)])
            for i in range(C.rows):
                for j in range(C.columns):
                    C.values[i][j] = matrix.values[i][j] * B
            return C
        
        elif type(B) == type(matrix):
            if matrix.columns != B.rows:
                raise Exception("Matrix can't be multipyeid")
            
            C = Matrix([[0]*matrix.rows for _ in range(B.columns)])
            
            for i in range(matrix.rows):
               for j in range(B.columns):
                   for k in range(matrix.rows):
                       C.values[i][j] += matrix.values[i][k] * B.values[k][j]
            return C
        else:
            raise Exception("Matrix cant be multipyt with, " + str(type(B)))
    
    def add(matrix, B):
        if len(matrix.values[0]) != len(B[0]) or len(matrix.values) != len(B):
            raise Excaption("Matrix can't be added of defrent sizes.")
        for i in range(matrix.rows):
            for j in range(matrix.columns):
                matrix.values[i][j] = matrix.values[i][j] + B[i][j]
    
    def sub(matrix, B):
        if len(matrix.values[0]) != len(B[0]) or len(matrix.values) != len(B):
            raise Excaption("Matrix can't be subtracted of defrent sizes.")
        for i in range(matrix.rows):
            for j in range(matrix.columns):
                matrix.values[i][j] = matrix.values[i][j] - B[i][j] 
    
    def mul(matrix, B):
        if type(B) == type(0):
            C = Matrix([[0]*matrix.rows for _ in range(matrix.columns)])
            for i in range(C.rows):
                for j in range(C.columns):
                    matrix.values[i][j] = matrix.values[i][j] * B
        elif type(B) == type(Matrix):
            if matrix.columns != B.rows:
                raise Exception("Matrix can't be multipyeid")
            
            C = Matrix([[0]*matrix.rows for _ in range(B.columns)])
            
            for i in range(matrix.rows):
               for j in range(B.columns):
                   for k in range(matrix.rows):
                       C.values[i][j] += matrix.values[i][k] * B.values[k][j]
            matrix = C
        else:
            raise Exception("Matrix cant be multiplied with", str(type(B)))
    
    def row(matrix, index: int):
        if index >= matrix.rows or index < 0: raise ValueErorr("Row index out of range")
        return matrix.values[index]
    
    def column(matrix, index: int):
        if index >= matrix.columns or index < 0: raise ValueErorr("Column index out of range")
        return  [r[index] for r in matrix.values]
    
    def add_row(matrix, row: list, index=None):
        if len(row) != matrix.columns:
            raise Exception("Row must be the size of metrix columns")
        if not all(type(e) == type(0) or type(e) == type(0.0) for e in row):
            raise Exception("Matrix elemnts can only be of type int or float")
        if not index: index = matrix.columns
        matrix.values.insert(index, row)
        matrix.rows += 1
    
    def add_column(matrix, column: list, index=None):
        if len(column) != matrix.rows:
            raise Exception("Columns must be the size of metrix rows")
        if not all(type(e) == type(0) or type(e) == type(0.0) for e in column):
            raise Exception("Matrix elemnts can only be of type int or float")
        if not index: index = matrix.columns
        for r, e in enumerate(column):
            matrix.values[r].insert(index, e)
        matrix.columns += 1

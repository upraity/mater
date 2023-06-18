def is_palindrome(num: int) -> bool:
    """Return the num is Palindrome or not"""
    r = 0
    t = num
    while t > 0:
        r = (r * 10) + t % 10
        t//=10
    return r == num                                       

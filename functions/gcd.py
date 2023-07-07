def gcd(a: int, b:int) -> int:
    while a and b:
        a, b = b % a, a
    return b











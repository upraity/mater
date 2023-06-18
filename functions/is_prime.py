def is_prime(num: int) -> bool:
    """Return the num is prime or not"""
    if num < 2: return False
    for i in range(2, num//2+1):
        if not num % i : return False
    return True
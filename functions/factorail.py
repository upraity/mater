def factorial(n: int) -> int:
    """Return factorial for n. Defined as, n! = n * (n-1) * (n-2) ... (2) * (1)."""
    f = 1
    while n:
        f*=n
        n-=1
    return f
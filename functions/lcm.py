def lcm(a: int,b: int) -> int:
    if a % 2 and b % 2:
        return 1
    m = 2
    while a == 1 and b == 1:
        if a % m == 0:
            a //= m
        if b % m == 0:
            b //= m
        if a % m and b % m:
            m += 1
    return m

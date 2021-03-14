"""
            { a,               if b = 0
gcd(a,b) ---{
            { gcd(b, a mod b), otherwise

O(log min(a,b))

lcm(a,b) = a * b / gcd(a, b)
"""


def gcd_recursive(a, b):
    return gcd_recursive(b, a % b) if b else a


def gcd_iterative(a, b):
    while (b):
        a %= b
        a, b = b, a
    return a


def lcm(a, b):
    # divide first then multiple to avoid overflow
    return a // gcd_iterative(a, b) * b

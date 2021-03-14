"""
using the property of associativity treat exp in base 2
exp in base 2 will have exactly floor(log_2(n)) + 1 digits 
it only takes O(log n) multiplications to calculate the exponent
"""


def binexp_recursive(a, exp):
    if exp == 0:
        return 1
    res = binexp_recursive(a, exp // 2)
    if exp % 2:
        return res * res * a
    else:
        return res * res


def binexp_iterative(a, exp):
    res = 1
    while (exp > 0):
        if (exp & 1):
            res = res * a
        a = a * a
        exp >>= 1
    return res

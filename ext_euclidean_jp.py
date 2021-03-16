"""
find a * x + b * y = g (x and y are the coefficient)

starting from base coefficient x,y = 1,0 going back wards
find x_1,y_1 that makes (a,b) to (b,a mod b)
b * x_1 + (a mod b) * y_1 = g
rewrite (a mod b) as (a - (a // b) * b)
then        g = b * x_1 + (a - (a // b) * b) * y_1
rearrange   g = a * y_1 + b * (x_1 - y_1 * (a // b))
therefore   x = y_1, y = x_1 - y_1 * (a // b)
"""


def ext_gcd_recursive(a: int, b: int):
    if (b == 0):
        return a, 1, 0
    q, x_1, y_1 = ext_gcd_recursive(b, a % b)
    x = y_1
    y = x_1 - y_1 * (a // b)
    return q, x, y


def ext_gcd_iterative(a: int, b: int):
    x, y = 1, 0
    x_1, y_1, a_1, b_1 = 0, 1, a, b
    while (b_1):
        q = a_1 // b_1
        x, x_1 = x_1, x - q * x_1
        y, y_1 = y_1, y - q * y_1
        a_1, b_1 = b_1, a_1 - q * b_1
    return a_1
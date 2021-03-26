from ext_euclidean_jp import ext_gcd_iterative


def linear_diophantine_can_find(a, b, c):
    g, x, y = ext_gcd_iterative(abs(a), abs(b))
    if (c % g):
        return False, 0, 0, g

    x *= c // g
    y *= c // g
    if (a < 0):
        x = -x
    if (b < 0):
        y = -y
    return True, x, y, g

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

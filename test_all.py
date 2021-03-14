import pytest
import math
from binexp_jp import *
from euclidean_jp import *


def test_binexp():
    assert(binexp_recursive(3, 13) == (1594323))
    assert(binexp_iterative(4, 13) == math.pow(4, 13))


def test_euclidean():
    assert (gcd_iterative(121, 11) == math.gcd(121, 11))
    assert (gcd_recursive(250, 75) == math.gcd(250, 75))
    assert (lcm(2, 5) == math.lcm(2, 5))

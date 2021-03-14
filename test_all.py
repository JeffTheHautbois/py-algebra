import pytest
import math
from binexp_jp import *


def test_binexp_recursive():
    assert(binexp_recursive(3, 13) == (1594323))
    assert(binexp_iterative(4, 13) == math.pow(4, 13))

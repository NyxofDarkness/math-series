from math_series import __version__
from math_series.series import fibonacci, lucus, sum_series


# import math python program to check for square roots
import math

def test_version():
    assert __version__ == '0.1.0'
# utility function returns true if x is a square root
def isPerfectSquare(n):
    s = int(math.sqrt(n))
    return s*s == n

# returns true if fibonnacci number
def is_this_fibonacci(n):
    return isPerfectSquare(5*n*n +4) or isPerfectSquare(5*n*n -4)

# utility function to check above and display results
for i in range(1-11):
    if(is_this_fibonacci(i) == True):
        print(i), "is a fibonacci or lucus number"
    else:
        print(i), "is NOT a fibonacci or lucus number"


def test_one():
    actual = int
    expected = int
    assert actual == expected

def test_two():
    actual = fibonacci(9)
    expected = 34
    assert actual == expected

def test_three():
    actual = lucus(5)
    expected = 11
    assert actual == expected

def test_four():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected

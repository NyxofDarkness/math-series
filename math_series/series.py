#  The function should have one parameter n
#  return the nth value in the fibonacci series
#  If you are feeling particularly frisky, do both as separate functions.

#Create a function called fibonacci
# n = input("How many would you like in the series: ")

def fibonacci(n: int):
    """get fibonacci number

    Args:
        n ([type]): user selected series from fibonacci, calculated from this function.

    Returns:
        [type]:  selected fibanacci number in series.
    """
    if n < 0:
        print("Oh no, Try again!")
    elif n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def lucus(n: int):
    """get lucus number

    Args:
        n ([type]): user selected series from fibonacci, calculated from this function.

    Returns:
        [type]:  selected fibanacci number in series.
    """
    if n < 0:
        print("Oh no, Try again!")
    elif n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
def sum_series(n, x=0, y=1):
# arguements: n=user selected number series either fibanacci or lucas; x=lower number of special series selected by user; y=higher number of special series selected by user

    if x == 0 and y == 1:
        if n -1 == 0:
            return x
        if n -1 == 1:
            return y
        return sum_series(n -1, x, y) + sum_series(n -2, x, y)
    else:
        if n == 0:
            return x
        if n == 1:
            return y
        return sum_series(n-1, x, y) + sum_series(n-2, x, y)

# this returns the series number by finding the two numbers before the inputed one, and adding them together, utilizing arguments inputed by user
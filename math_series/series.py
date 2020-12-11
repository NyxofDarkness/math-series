#  The function should have one parameter n
#  return the nth value in the fibonacci series
#  If you are feeling particularly frisky, do both as separate functions.

#Create a function called fibonacci
# n = input("How many would you like in the series: ")

def fibonacci(n):
    # areuments: n= user selected series from fibonacci, calculated from this function.
    if n<0:
        # This is in case the number is less than zero, because our code doesnt account for that! (maybe a good stretch goal!)
        print("Oh no, Try again!")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (n-1)+(n-2)
        # this returns the fibonnacci number by finding the two numbers before the inputed one, and adding them together

def lucus(n):
    # arguments: n= user selected series from lucas, calculated from this function.
    if n<0:
        print("oh no, try again!")
    elif n==2:
        return 0
    elif n==1:
        return 1
    else:
        return (n-1)+(n-2)
        # this returns the fibonnacci number by finding the two numbers before the inputed one, and adding them together

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
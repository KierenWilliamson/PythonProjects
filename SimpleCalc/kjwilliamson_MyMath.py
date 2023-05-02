# Name: Kieren Williamson
# Class: Comp 163-001
# Date: March 24, 2023,
# Description: This program defines common algebraic expressions that can also be found
# as methods of the Math module without importing the Math module.

def calc_add(value1, value2):
    result = value1 + value2
    return result


def calc_subtract(value1, value2):
    result = value1 - value2
    return result


def calc_multiply(value1, value2):
    result = value1 * value2
    return result


def calc_divide(value1, value2):
    if value2 == 0:
        return 'Undefined'
    elif value1 == 0:
        return 0.0
    else:
        result = value1 / value2
        return result


def calc_modulo(value1, value2):
    result = value1 % value2
    return result


def absolute(value1):
    if value1 >= 0:
        return value1
    else:
        result = value1 * -1
        return result


def floorDiv(value1, value2):
    """function that executes floor division upon two integers"""
    if value2 == 0:
        return 'Undefined'
    elif value1 == 0:
        return 0
    else:
        result = value1 // value2
        return int(result)


def power(value1, value2):
    if value2 == 0:
        return 1
    elif value2 == 1:
        return value1
    elif value2 < 0:
        result = value1
        for i in range(absolute(value2) - 1):
            result *= value1
        return 1/result
    else:
        result = value1
        for i in range(value2-1):
            result *= value1
        return result


def root(value1, value2):
    """returns the nth root of an integer"""
    guess = 1
    guess_prime = guess - (((guess ** value2) - value1) / (value2 * (guess ** (value2 - 1))))
    if value1 == 0:
        return 0
    elif value2 == 1:
        return value1
    else:
        while not absolute(guess_prime - guess) < (10 ** -10):
            guess = guess_prime
            guess_prime = guess - (((guess ** value2) - value1) / (value2 * (guess ** (value2 - 1))))
        else:
            return guess_prime


def gcd(value1, value2):
    """finds the greatest common divisor of two integers"""
    if value1 == 0:
        return int(value2)
    elif value2 == 0:
        return int(value1)
    else:
        return absolute(gcd(value2, value1 % value2))


def lcm(value1, value2):
    """finds the least common multiple of two integers"""
    return absolute(int((value1 * value2) / (gcd(value1, value2))))


def sine(value1):
    """Finds the sine of a radian measure"""
    pi = 3.141592653589793
    counter = 0
    if -pi <= value1 <= pi:
        value_prime = value1 * ((-value1**2) / (((2 * counter) + 3) * ((2 * counter) + 2)))
        summation = value1 + value_prime
        while not absolute(value_prime) < (10 ** -10):
            counter += 1
            value_prime = value_prime * ((-value1**2) / (((2 * counter) + 3) * ((2 * counter) + 2)))
            summation += value_prime
        else:
            return summation
    elif value1 < -pi:
        value1 += 2 * pi
        return sine(value1)
    elif value1 > pi:
        value1 -= 2 * pi
        return sine(value1)


def cosine(value1):
    """Finds the cosine of a radian measure"""
    pi = 3.141592653589793
    counter = 0
    if -pi <= value1 <= pi:
        value_prime = 1 * ((-value1 ** 2) / (((2 * counter) + 2) * ((2 * counter) + 1)))
        summation = 1 + value_prime
        while not absolute(value_prime) < (10 ** -10):
            counter += 1
            value_prime = value_prime * ((-value1 ** 2) / (((2 * counter) + 2) * ((2 * counter) + 1)))
            summation += value_prime
        else:
            return summation
    elif value1 < -pi:
        value1 += 2 * pi
        return sine(value1)
    elif value1 > pi:
        value1 -= 2 * pi
        return sine(value1)


def tangent(value1):
    """Finds the tangent of a radian measure"""
    pi = 3.141592653589793
    if -pi <= value1 <= pi:
        result = (sine(value1) / cosine(value1))
        return result
    elif value1 < -pi:
        value1 += 2 * pi
        return sine(value1)
    elif value1 > pi:
        value1 -= 2 * pi
        return sine(value1)

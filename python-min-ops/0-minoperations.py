import math


def minOperations(n):

    logarithm = math.log((n - 1), 2)
    return math.ceil(logarithm * 2)

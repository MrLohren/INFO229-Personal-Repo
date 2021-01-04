from math import sqrt
def isprime(n):

    if n <= 1:
        return False

    for i in range(2, int(n**(1/2))+1):
        if n%i == 0:
            return False

    return True   
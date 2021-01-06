import pytest
from  primes import isprime

def sum_of_primes(lista):
    total = 0

    for i in lista:
        if isprime(i):
            total += i

    return total

@pytest.mark.parametrize("lista, suma", [([2,3,4,5,6], 10), ([13,17,23], 53)])
def test_list_prime(lista, suma):
    assert sum_of_primes(lista) == suma
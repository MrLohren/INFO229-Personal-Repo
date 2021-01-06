import pytest

def fibonacci(n):
    if n == 1:
        return 1

    if n == 0:
        return 0
        
    return fibonacci(n-1) + fibonacci(n-2)

@pytest.mark.parametrize("rango, resultado",[(2, 1),(6, 8),(10, 55)])
def test_fibonacci(rango, resultado):
    assert fibonacci(rango) == resultado
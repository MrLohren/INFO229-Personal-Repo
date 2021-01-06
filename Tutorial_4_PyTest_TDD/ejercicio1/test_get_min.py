import pytest

@pytest.mark.parametrize("minimo, arreglo",[(1, [1,2,3,4,5]),(2,[2,3,4,5,6])])
def test_get_min(minimo, arreglo):
    assert minimo == min(arreglo)
import pytest

def aloh(string):
    return string[::-1]

@pytest.mark.parametrize("pal, lap", [("hola", "aloh"),("ana", "ana"),("toyota", "atoyot")])
def test_aloh(pal,lap):
    assert aloh(pal) == lap
import sys

sys.path.append('../src/prime_fl2635')

from prime_fl2635 import is_prime


def test_is_prime():
    # prime numbers
    assert is_prime(2) == True
    assert is_prime(7) == True
    # composite numbers
    assert is_prime(8) == False
    assert is_prime(9) == False

import math

def is_prime(n):
    """
    Check if a number is prime.

    This function checks whether a given integer is a prime number.

    Args:
        n (int): The integer to check for primality.

    Returns:
        bool: True if the input number is prime, False otherwise.

    Example:
        >>> is_prime(5)
        True
        >>> is_prime(4)
        False
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
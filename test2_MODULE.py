# Test 2
import unittest


def is_integer(number):
    """Returns True if number is an integer"""
# using complex numbers

    if number == "j" or number == "i":
        return False

    return True


if __name__ == '__main__':
    unittest.main()
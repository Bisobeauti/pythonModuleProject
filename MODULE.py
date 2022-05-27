

import unittest
# Test 1


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 5, 10]), 17, "Should be 17")

    def test_sum_tuple(self):
        self.assertEqual(sum([2, 5, 10]), 17, "Should be 17")

        if __name__ == '__main__':
            unittest.main()

# Test 2


def is_integer(number):
    """Returns True if number is an integer"""
# using complex numbers

    if number == "j" or number == "i":
        return False

    return True


if __name__ == '__main__':
    unittest.main()

# Test 3

    """multiply two numbers

    This is the test:
    >>> multiply(2,2)
    4
    """
    def multiply(a, b):
        return a * b

if __name__ == '__main__':
    unittest.main()

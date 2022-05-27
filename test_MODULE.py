import unittest
# Test 1


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([2, 5, 10]), 17, "Should be 17")

    def test_sum_tuple(self):
        self.assertEqual(sum([2, 5, 10]), 17, "Should be 17")

        if __name__ == '__main__':
            unittest.main()
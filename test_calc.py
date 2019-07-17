import unittest
from test1 import add, mul

class calc_test(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1,2), 3)

    def test_mul(self):
        self.assertEqual(mul(1,2), 2)


if __name__ == '__main__':
    unittest.main()



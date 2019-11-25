import unittest

def is_kaprekar(n):
    nSquare = n*n
    for i in range(len(str(nSquare))):
        left = 0
        if 0 < i:
            left = str(nSquare)[0:i]
        right = str(nSquare)[i:]
        if int(left) + int(right) == n:
            return True
    return False

class testKapekar(unittest.TestCase):
    def testKapekars(self):
        self.assertTrue(is_kaprekar(0))
        self.assertTrue(is_kaprekar(1))
        self.assertFalse(is_kaprekar(2))
        self.assertFalse(is_kaprekar(5))
        self.assertFalse(is_kaprekar(65))
        self.assertTrue(is_kaprekar(99))
        self.assertTrue(is_kaprekar(297))


def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()

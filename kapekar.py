import unittest

def is_kaprekar(n):
    if not n:
        return True
    if n<=3 and n**2==0+n:
        return True
    else:
        return False
    if n>3 and n**2%2==0:
        if int(str(n**2).split()[0])+int(str((n**2).split()[1]))==n**2:
            return True
        else:
            return False
    if n>3 and (n**2)%2!=0:
        if int(str((n**2)[:0]))+int(str(n**2)[0:])==n**2:
            return True
        else:
            return False


class testKapekar(unittest.TestCase):
    def testKapekars(self):
        self.assertTrue(is_kaprekar(0))
        self.assertTrue(is_kaprekar(1))
        self.assertFalse(is_kaprekar(2))

        # Add your further cases here

def main():
    unittest.main(verbosity=2)


if __name__ == '__main__':
    main()

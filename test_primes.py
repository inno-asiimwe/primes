import unittest
from primes import list_primes, is_int

class PrimeNumberTest(unittest.TestCase):

    def setUp(self):
        self.primes = list_primes(100)

    def test_is_int_interger(self):
        """Testing whether is_int returns true with an Interger """
        b = is_int(4)
        self.assertTrue(b)
    def test_is_int_non_interger(self):
        """Testing whether is_int returns false with non Interger an interger"""
        b = is_int('two')
        self.assertFalse(b)

    



import unittest
from primes import list_primes, is_int, is_greater_than_two

class PrimeNumberTest(unittest.TestCase):
    
    def setUp(self):
        self.primes = list_primes(100)

    
    def test_is_int_interger(self):
        """Testing whether is_int returns true with an Interger """
        test_value = is_int(4)
        self.assertTrue(test_value)

    def test_is_int_non_interger(self):
        """Testing whether is_int returns false with non Interger an interger"""
        test_value = is_int('two')
        self.assertFalse(test_value)

    def test_input_greater_than_2(self):
        """Method tests whether is_greater_than_two returns True with 2 or a number greater than 2"""
        self.assertTrue(is_greater_than_two(4))

    def test_input_less_than_2(self):
        """Method tests whether is_greater_thsn_two returns Falls with a number less than 2"""
        self.assertFalse(is_greater_than_two(1))

    def test_non_interger_input(self):
        """method tests whether is_greater_than_two raise a type Error with a non numeric value"""
        self.assertRaises(TypeError, is_greater_than_two('four'))

    def test_list_primes_for_prime(self):
        """Method tests if a given prime is in a list of prime numbers returned by list_primes"""
        my_primes = list_primes(100)
        self.assertIn(7, my_primes)

    def test_list_primes_for_non_prime(self):
        """Method tests if a non prime is present in a list of primes"""
        my_primes = list_primes(100)
        self.assertNotIn(6, my_primes)

    def test_output_for_upperlimit_if_prime(self):
        """Method tests if the given number is included in the list of primes if it is prime"""
        my_primes = list_primes(5)
        self.assertEqual(my_primes, [2,3,5])




    
        

    



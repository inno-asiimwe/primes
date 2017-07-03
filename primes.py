def list_primes(number):
    primes = []
    non_primes = []
    if is_greater_than_two(number):
        for integer in range(2, number + 1):
            if integer not in non_primes:
                primes.append(integer)

                for i in range(integer * integer, number + 1, integer):
                    non_primes.append(i)
    else:
        raise ValueError("number should be greater than or equal to two")

    return primes
            
        

def is_int(number):
    """The method returns True for Integers and false for everything else"""
    if isinstance(number, int):
        return True
    else:
        return False

def is_greater_than_two(number):
    """Function returns true when the  given number is greater or equal two, 
    false numbers less than two, and raises type error for an interger"""
    if is_int(number):
        if number >= 2:
            return True
        else:
            return False
    else:
        raise TypeError("input should be an integer")

"""Recursion exercises"""

import doctest


def recursion_multiply(n1, n2):
    """1. Write a function that takes in two numbers and recursively
    multiplies them together.

    >>> recursion_multiply(2,2)
    4

    >>> recursion_multiply(10,2)
    20

    >>> recursion_multiply(0,2)
    0

    """

    if n1 < 1:
        return 0
    else:
        return n2 + recursion_multiply(n1 - 1, n2)


def recursion_exponential(base_n, exponent_n):
    """
    2. Write a function that takes in a base and an exp and recursively 
    computes base exp. Do not use the ** operator!

    >>> recursion_exponential(2,2)
    4

    >>> recursion_exponential(10,2)
    100

    recursion_exponential(2,10)
    1,024

    >>> recursion_exponential(10,0)
    1

    >>> recursion_exponential(0,10)
    0
    """

    if exponent_n < 1:
        return 1

    if base_n < 1:
        return 0

    else:
        return base_n * recursion_exponential(base_n, exponent_n -1)


def recursion_n_to_0(n):
    """
    3. Write a function using recursion to print numbers from n to 0.
    Function returns nothing

    """

    if n < 1:
        return 0
    else:
        return n
    
    recursion_n_to_0(n - 1)

# need to check this! to print all the way to n
def recursion_0_to_n(start_num, end_num):
    """
    # 4. Write a function using recursion to print numbers from 0 to
    n (you just need to change one line in the program of problem 1).
    """

    if end_num < 1:
        return
    else:
        print start_num
        return recursion_0_to_n(start_num + 1, end_num -1)

 
def reverse_string(string, new_str, str_length):
    """
    5. Write a function using recursion that takes in a string and returns
    a reversed copy of the string. The only string operation you are allowed
     to use is string concatenation.

    >>> reverse_string("string", '', 6)
    'gnirts'
    """

    if str_length < 1:   
        return new_str

    else:        
        char = string[(str_length - 1)]
        new_str += char
        
    return reverse_string(string, new_str, str_length - 1)


# print reverse_string("string", '', 6)


"""
6. Write a function using recursion to check if a number n is prime (you
have to check whether n is divisible by any number below n).

>>> is_prime(5)
True

>>> is_prime(4)
False

>>> is_prime(15)
False
"""

def is_prime(n):
    if n % recursion_n_to_0(n - 1) == 0:
        return False
    else:
        return True

       
print is_prime(5)



def fibonacci(n):
    """
    7. Write a recursive function that takes in one argument n and 
    computes Fn, the nth value of the Fibonacci sequence. Recall that
    the Fibonacci sequence is defined by the relation Fn = Fn-1 + Fn-2
    where F0 = 0 and F1 = 1
    >>> fibonacci(5)
    5

    >>> fibonacci(1)
    1

    >>> fibonacci(3)
    2
    """
    
    if n <= 1:
        return n

    return fibonacci(n - 2) + fibonacci(n - 1)

print fibonacci(5)



def main():
    import doctest
    import timeit

    recursion_exponential(2,10)
    
    print "this is recursion multiply result", recursion_multiply(3,2)
    print timeit.timeit(lambda: recursion_multiply(3,2), number=100)

    print "this is recursion exponential result", recursion_exponential(2,10)
    print timeit.timeit(lambda: recursion_exponential(2,10), number=100)

    print "this recursion print n to 0 time"
    recursion_n_to_0(10)
    # print timeit.timeit(lambda: recursion_n_to_0(10), number=100)

    print "this recursion print 0 to n time"
    recursion_0_to_n(0, 10)   


    print "this is fibonacci result", fibonacci(5)
    print timeit.timeit(lambda: fibonacci(5), number=100)


    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU BE AWESOME!\n"


if __name__ == '__main__':
    
    main()
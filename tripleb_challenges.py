import doctest

def consecutive_int(num_array):
    """
    return longest occurance of an consecutive appearance of an 
    integer in a list

    >>> consecutive_int([1,1,1,1])
    4

    >>> consecutive_int([1,2,2,1])
    2

    >>> consecutive_int([1,1,1,2,2,2,2,1,1,1])
    4

    """

    count = []
    start = [num_array[0]]

    i = 1
    while i < len(num_array):
        if num_array[i] == start[-1]:
            start.append(num_array[i])
           
        else:
            count.append(len(start))
            start = [num_array[i]]

        i += 1

    count.append(len(start))
    
    return max(count)



def nearest_pow_of_2(n):
    """
    Find a nearest power of 2 to a number n
    
    >>> nearest_pow_of_2(2)
    2

    >>> nearest_pow_of_2(10)
    8

    >>> nearest_pow_of_2(100)
    64
    """


    pow_list = [1]
    i = 0
    while pow_list[-1] < n:
        pow_2 = pow(2,i)
        pow_list.append(pow_2)

        i += 1
    if pow_list[-1] > n:
        pow_list.pop()

    return pow_list[-1]



"""
A palindrome is a string which reads the same forwards as backwards, 
for example 'abba' or 'racecar' or 'bob'. 
Write a function which returns the length of the longest palindromic 
substring of a given string. For example, the longest palindromic 
substring of 'bobcat' is 'bob', so you'd return 3. 
You do not need to come up with an optimized algorithm for this.
A simple search through all substrings is fine. 

>>> longest_palidrome_substr('abba')
4

>>> longest_palidrome_substr('bobcat')
3

>>> longest_palidrome_substr('acyclic')
3
"""
# helper function
def palindrome_count(a_string):
    mid = len(a_string)/2
    i = 0
    j = len(a_string) - 1

    if a_string[0] == a_string[-1]:
        while i < mid:
            if a_string[i] == a_string[j]:
                return len(a_string)
            
            else:
                return False
            
            i += 1
            j -= 1


def longest_palidrome_substr(a_string):    
    mid = len(a_string)/2

    if a_string[0] == a_string[-1]:
        return palindrome_count(a_string)
    
    elif a_string[0] == a_string[mid-1]:
        str1 = a_string[0:mid]
        return palindrome_count(str1)

    elif a_string[mid] == a_string[-1]:
        str2 = a_string[0:mid]
        return palindrome_count(str2)
            


def interleave(str1, str2):
    """
    A function that takes two strings and interleaves the 
    characters
    >>> interleave('abcd', '1234')
    'a1b2c3d4'

    >>> interleave('abcd', '1')
    'a1bcd'
    """
    new_str = ''
    
   # case if strings are same length
    if len(str1) == len(str2):
        i = 0
        while i < len(str1):
            new_str += str1[i]
            new_str += str2[i]
            i += 1
            
    # case if str2 is shorter than string 1:
    # run loop until string 2 ends, and append the rest of str1
    if len(str2) < len(str1):
        j = 0
        while j < len(str2):
            new_str += str1[j]
            new_str += str2[j]
            j += 1
        
        new_str += str1[len(str2):]
                
            
    return new_str


if doctest.testmod().failed == 0:
    print "\n*** All doctest integration tests passed!\n"
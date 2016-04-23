"""Is the word an anagram of a palindrome?

A palindrome is a word that reads the same forward and backwards
(eg, "racecar", "tacocat"). An anagram is a rescrambling of a word
(eg for "racecar", you could rescramble this as "arceace").

Determine if the given word is a re-scrambling of a palindrome.
The word will only contain lowercase letters, a-z.



>>> is_anagram_of_palindrome("a")
True

>>> is_anagram_of_palindrome("ab")
False

>>> is_anagram_of_palindrome("aab")
True

>>> is_anagram_of_palindrome("arceace")
True

>>> is_anagram_of_palindrome("arceaceb")
False

"""


def is_anagram_of_palindrome(word):
    """Is the word an anagram of a palindrome?"""

    letter_set = set(word)
    word_dict = {}

    for letter in letter_set:
        
        # counts appearance of letter in string with count()
        word_dict[letter] = word.count(letter)


    num_odd_letters = []

    for key in word_dict:
        
        # checks if letter appears an odd number of times
        # appends to list if a letter appears an odd number of times
        if word_dict[key] % 2 != 0:
            num_odd_letters.append(word_dict[key])

    # in a valid palindrome an odd letter can appears one time. 
    if len(num_odd_letters) <= 1:
        return True

    # if the list is empty all the letters appeared an even number of times. 
    else:
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod(verbose=True).failed == 0:
        print "\n*** ALL TEST PASSED. AWESOMESAUCE!\n"

# Big O-Notation analysis:
# set lookup is O(1)
# counting each value of string O(n)
# Lookup by dictinary key is O(1)
# 
# This solution has O(n) runtime?


        

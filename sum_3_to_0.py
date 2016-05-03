""" 
Write a function to determine if any 3 integers in an array sum to 0.

If so, return True if, else False

>>> sum_three_to_zero([1,-1,3,5,2,-2])
True

>>> sum_three_to_zero([1,1,1,1,1])
False

>>> sum_three_to_zero([1,-1])
False

>>> sum_three_to_zero([1,-1, 0])
True

"""

def sum_three_to_zero(lst):
    """ 
    Write a function to determine if any 3 integers in an array sum to 0.
    """
    # validity check
    if len(lst) < 3:
        return False
    
    if sum(lst) == 0:
        return True

    # sort integer list from low-high to prevent duplicates during iterations
    lst = sorted(lst)

    # set ranges for iteration lists for other sum_three values
    j_lst = lst[1::]
    k_lst = lst[2::]
    
    # initialize list of integers that store 3 values that sum to three
    sum_three = [None, None, None]

    # nested for-loops
    for i in lst:
        sum_three[0] = i

        for j in j_lst:
            sum_three[1] = j
        
            for k in k_lst:
                sum_three[2] = k
                
                if sum(sum_three) == 0: 

                    return True

    if sum(sum_three) != 0:

        return False


def main():
    import doctest
    import timeit

    print sum_three_to_zero([1,-1,3,5,2,-2])  
    print timeit.timeit(lambda: sum_three_to_zero([1,-1,3,5,2,-2]), number=100)

    if doctest.testmod().failed == 0:
        print "\n*** All tests passed!\n"


if __name__ == '__main__':
    main()
    pass


def sum_three_to_zero2(lst):
    """ 
    Write a function to determine if any 3 integers in an array sum to 0.
    """
    positive = []
    negative = []

    for i in lst:
        if i > 0:
            positive.append(i)

        if i < 0:
            negative.append(i)
   
    if abs(sum(negative)) in positive:
        return True

    else:
        return False

print sum_three_to_zero2([1,-1,3,5,2,-2])
print sum_three_to_zero2([1,1,1,1,1])

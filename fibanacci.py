import timeit

# Uses python3
def calc_fib(n):
    """Classic recursion solution to finding nth fibanacci number """

    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)



def fib_loop(n):
    """Return nth fibanacci number iteration.

    function stores calculated values by swapping variable assignments

     """

    a,b = 1,1 #set and b to 1
    for i in range(n-1): #for range([0,1,2,3]), iterate 4 times
                         # initialize loop 
        a,b = b, a+b # during loop assign a to b
                     # and then b = a + b
    
    return a # fib_loop(5) returns 5

def fib_loop2(n):
    """Return nth fibanacci number iteration.

    function stores calculated values by swapping variable assignments
    # this doesn't work
    """

    a = 1
    b = 1

    for i in range(n-1):
        a = b
        b = a + b
    
    return a # fib_loop2(5) this returns 8 instead of 5???? 
             # b/c over evaluating when the variable is called. 

def fib_loop3(n): 
    """Calcuates fibanacci sequence using an array/list.

    function adds last 2 list elements and then appends that value to list"""

    fibo=[0,1]
    for i in range(n-1):
        fibo.append(fibo[-1]+fibo[-2])

    return fibo[-1]

def memoize(fn, n):
    """Memoized or cached recursion solution to finding nth fibanacci number 
    
    function runs calc_fib() and stores results in a dictionary/ hash table,
    last value in dictionary
    """
    cached = {}
    if n not in cached:
        cached[n] = calc_fib(n)
        return cached[n]



# running functions solutions and comparing runtimes
print calc_fib(5)
print 'calc_fib time is', timeit.timeit(lambda :calc_fib(10), number=100)
print fib_loop(5)
print 'calc_loop time is', timeit.timeit(lambda :fib_loop(10), number=100)
print fib_loop2(5)
print 'calc_loop2 time is',timeit.timeit(lambda :fib_loop2(10), number=100)
print fib_loop3(5)
print 'calc_loop3 time is',timeit.timeit(lambda :fib_loop2(10), number=100)
print memoize(calc_fib, 5)
print 'memoize time is,', timeit.timeit(lambda :memoize(calc_fib, 5), number=100)

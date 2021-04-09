# version code 80e56511a793+
# Please fill out this stencil and submit using the provided submission script.





## 1: (Problem 1.7.1) Python Comprehensions: Filtering
def myFilter(L, num):
    '''
    Input:
      -L: a list of numbers
      -num: a positive integer
    Output:
      -a list of numbers not containing a multiple of num
    Examples:
      >>> myFilter([1,2,4,5,7],2)
      [1, 5, 7]
      >>> myFilter([10,15,20,25],10)
      [15, 25]
    '''
    new_L = []
    [new_L.append(item) for item in L if item % num != 0]
    return new_L





## 2: (Problem 1.7.2) Python Comprehensions: Lists of Lists

def my_lists(L):
    '''
    >>> my_lists([1,2,4])
    [[1], [1, 2], [1, 2, 3, 4]]
    >>> my_lists([0,3])
    [[], [1, 2, 3]]
    '''
    W = []
    for i in L:
        P = []
        k = 1
        for t in range(i):
            P.append(t+1)
        W.append(P)
    return W



## 3: (Problem 1.7.3) Python Comprehensions: Function Composition
def myFunctionComposition(f, g):
    '''
    Input:
      -f: a function represented as a dictionary such that g of f exists
      -g: a function represented as a dictionary such that g of f exists
    Output:
      -a dictionary that represents a function g of f


    '''
    newDict = {}
    for num in f:
        newDict[num] = g.get(f.get(num))
    return newDict



## 4: (Problem 1.7.4) Summing numbers in a list
def mySum(L):
    '''
    Input:
      a list L of numbers
    Output:
      sum of the numbers in L
Be sure your procedure works for the empty list.
    Examples:
      >>> mySum([1,2,3,4])
      10
      >>> mySum([3,5,10])
      18
    '''
    current = 0
    for x in L:
	    current += x
    return current



## 5: (Problem 1.7.5) Multiplying numbers in a list
def myProduct(L):
    '''
python submit.py The_Field_problems.py
    Input:
      -L: a list of numbers
    Output:
      -the product of the numbers in L
Be sure your procedure works for the empty list.

    '''
    current = 1
    for x in L:
        current *= x
    return current



## 6: (Problem 1.7.6) Minimum of a list
def myMin(L):
    '''
python submit.py The_Field_problems.py
    Input:
      a list L of numbers
    Output:
      the minimum number in L
Be sure your procedure works for the empty list.
Hint: The value of the Python expression float('infinity') is infinity.
    Examples:
    >>> myMin([1,-100,2,3])
    -100
    >>> myMin([0,3,5,-2,-5])
    -5
    '''
    current = 100000000
    for x in L:
        if ( current > x ):
            current = x
    return current



## 7: (Problem 1.7.7) Concatenation of a List
def myConcat(L):
    '''
    Input:
      -L:a list of strings
    Output:
      -the concatenation of all the strings in L
Be sure your procedure works for the empty list.
    Examples:
    >>> myConcat(['hello','world'])
    'helloworld'
    >>> myConcat(['what','is','up'])
    'whatisup'
    '''
    pass



## 8: (Problem 1.7.8) Union of Sets in a List
def myUnion(L):
    '''
    Input:
      -L:a list of sets
    Output:
      -the union of all sets in L
Be sure your procedure works for the empty list.
    Examples:
    >>> myUnion([{1,2},{2,3}])
    {1, 2, 3}
    >>> myUnion([set(),{3,5},{3,5}])
    {3, 5}
    '''
    pass



## 9: (Problem 1.7.10) Complex Addition Practice
# Each answer should be a Python expression whose value is a complex number.

complex_addition_a = ...
complex_addition_b = ...
complex_addition_c = ...
complex_addition_d = ...



## 10: (Problem 1.7.12) Combining Complex Operations
#Write a procedure that evaluates ax+b for all elements in L

def transform(a, b, L):
    '''
    Input:
      -a: a number
      -b: a number
      -L: a list of numbers
    Output:
      -a list of elements where each element is ax+b where x is an element in L
    Examples:
    >>> transform(3,2,[1,2,3])
    [5, 8, 11]
    '''
    pass



## 11: (Problem 1.7.13) GF(2) Arithmetic
GF2_sum_1 = ... # answer with 0 or 1
GF2_sum_2 = ...
GF2_sum_3 = ...


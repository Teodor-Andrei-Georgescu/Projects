import doctest

def sum_even_values(list1 : list[int]) -> int:
    '''
    Function must be given a list and it will return the sum of all the even 
    numbers within the list.
    
    >>> sum_even_values([1,2,3])
    2
    >>> sum_even_values([1,2,4])
    6
    >>> sum_even_values([6,2,4])
    12
    >>> sum_even_values([6,2,4,-2])
    10
    >>> sum_even_values([6,2,4,-4])
    8
    >>> sum_even_values([])
    0

    
    '''
    sum = 0
    list1_len = len(list1)
    for index in range(list1_len):
        if list1[index] % 2 == 0:
            sum += list1[index]
    return sum

def count_above(list1 : list[float], threshold : float) ->int:
    '''
    This function takes a list of number and a threshold value.
    It looks throught the list and returns how many vaues are above the threshold.
    
    >>> count_above([12,3,2,22,-2],2)
    3
    >>> count_above([1.2,2.4,2.7],2.1)
    2
    >>> count_above([],2.1)
    0
    >>> count_above([2.1],2.1)
    0
    >>> count_above([2.1,2],2.1)
    0
    >>> count_above([2.1,2,2.2],2.1)
    1
    >>> count_above([2.1,2,-2.2],2.1)
    0
    '''
    bigger_than = 0
    list1_len = len(list1)
    for index in range(list1_len):
        if list1[index] > threshold: 
            bigger_than += 1
    return bigger_than

def add1(list1: list[int]) -> list:
    '''
    This function takes a list and return a new list with each value increased by 1.
    
    >>> add1([12,4,3,-2])
    [13, 5, 4, -1]
    >>> add1([])
    []
    >>> add1([0])
    [1]
    '''
    list1_len = len(list1)
    list2 =[]
    for index in range(list1_len):
        number = list1[index] + 1
        list2.append(number)
    return list2

def are_all_even(list1 : list[int]) -> bool:
    '''
    This function takes a list and determines if all the numbers in the list are
    even.
    
    >>> are_all_even([2,4,6,12])
    True
    >>> are_all_even([2,4,6,1])
    False
    >>> are_all_even([])
    True
    >>> are_all_even([-2])
    True
    >>> are_all_even([-2,1])
    False
    '''
    total = 0
    list1_len = len(list1)
    for index in range(list1_len):
        if list1[index] % 2 == 0:
            total += 1
    return list1_len == total
    
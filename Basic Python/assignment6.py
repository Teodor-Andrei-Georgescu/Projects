import doctest

def is_multiple(number_1 : int, number_2 : int) ->bool:
    '''
    When given two integers the function will print of the first value is a multiple of the second.
    This is a helper function.
    '''
    truefalse = False
    if number_1 == 0:
        truefalse = True
    elif number_2 == 0:
        truefalse = False
    elif number_1% number_2 == 0:
        truefalse = True
    return truefalse
    
def multiply_by(list1 : list, multiplier : int) -> list[int]:
    '''
    This function takes two arguments:
    1.A list containing anything
    2. An integer that will act as the multiplier
    
    >>> multiply_by([23,2],3)
    [69, 6]
    >>> multiply_by([],3)
    []
    >>> multiply_by([],0)
    []
    >>> multiply_by([23,4],0)
    [0, 0]
    >>> multiply_by(['b','a'],0)
    ['', '']
    >>> multiply_by(['b','a'],3)
    ['bbb', 'aaa']
    >>> multiply_by(['b',-2],3)
    ['bbb', -6]

    '''
    list2 = []
    for index in range(len(list1)):
        number = list1[index] * multiplier
        list2.append(number)
    return list2

def remove_multiples(list1 : list[int], multiple : int) ->list:
    '''
    
    >>> remove_multiples([0,3,6,8],1)
    []
    >>> remove_multiples([0,3,6,8],0)
    [3, 6, 8]
    >>> remove_multiples([1,3,6,8],0)
    [1, 3, 6, 8]
    >>> remove_multiples([],3)
    []
    >>> remove_multiples([1,3,6,8],4)
    [1, 3, 6]
    >>> remove_multiples([1,3,6,8],3)
    [1, 8]
    '''
    list2 = []
    for index in range(len(list1)):
        if not is_multiple(list1[index],multiple):
            list2.append(list1[index])
    return list2

def remove_ends_with(list1 : list[str], ending : str) -> list:
    '''
    This function takes a list fo strings and another ending string.
    It will return a list with all the values that do not end in the ending string.
    
    >>> remove_ends_with(['hi','bat','rati'],'ti')
    ['hi', 'bat']
    >>> remove_ends_with(['hi','bat','rati'],'e')
    ['hi', 'bat', 'rati']
    >>> remove_ends_with(['hi','bat','rati'],'i')
    ['bat']
    >>> remove_ends_with(['hi','bait','rati'],'i')
    ['bait']
    >>> remove_ends_with([],'i')
    []
    >>> remove_ends_with(['hi','bait','ratI'],'I')
    ['bait']
    >>> remove_ends_with(['hi','bat','rati'],'')
    ['hi', 'bat', 'rati']
    '''
    list2 =[]
    ending = ending.lower()
    for index in range(len(list1)):
        str = list1[index]
        str = str.lower()
        if not ending == str[-len(ending):]:
            list2.append(list1[index])
    return list2

def get_index_of_largest(list1 : list[int]) -> int:
    '''
    This function takes a list of number and returns the index of the largest number.
    
    Preconditions = List must have atleast 1 value
    
    >>> get_index_of_largest([1,4,7,2])
    2
    >>> get_index_of_largest([1,4,7,7])
    3
    >>> get_index_of_largest([1,4,7,6])
    2
    >>> get_index_of_largest([1,4,7])
    2
    '''
    old_number = list1[0]
    largest_number = 0
    for index in range(0,len(list1)):
        number = list1[index]
        if number >= list1[largest_number]:
            largest_number = index 
    return largest_number

def does_contain_proper_divisor(list1 : list[int], number: int) -> bool:
    '''
    This function takes a list and another integer as arguments.
    It will then check to see if any of the values in the list are proper divisors
    of other integer value entered.
    
    >>> does_contain_proper_divisor([5,3,0],2)
    False
    >>> does_contain_proper_divisor([1,3,0],2)
    True
    >>> does_contain_proper_divisor([7,3,0],3)
    False
    >>> does_contain_proper_divisor([7,3,6],3)
    False
    >>> does_contain_proper_divisor([7,3,6],13)
    False
    >>> does_contain_proper_divisor([7,3,6],12)
    True
    >>> does_contain_proper_divisor([],12)
    False
    >>> does_contain_proper_divisor([],0)
    False
    >>> does_contain_proper_divisor([7,3,6],0)
    True
    '''
    if list1 == []:
        return False 
    elif number == 0:
        return True
    for index in range(len(list1)):
        list_num = list1[index]
        if list_num != number and list_num != 0 and (number % list_num) == 0:
            return True
    return False 


def are_all_less_than_threshold(list1 : list[int], threshold : int) -> bool:
    '''
    Takes 2 arguments:
    1.A list of integer
    2. A threshold value
    The funtion will then say if all the values in the list are less than the
    threshold vlaue or not.
    
    >>> are_all_less_than_threshold([2,3,4],6)
    True
    >>> are_all_less_than_threshold([2,3,4],4)
    False
    >>> are_all_less_than_threshold([2,3,4],2)
    False
    >>> are_all_less_than_threshold([2,3,4],8)
    True
    '''
    for index in range(len(list1)):
        if list1[index] >= threshold:
            return False
    return True


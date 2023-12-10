import doctest

FLIGHT_INFO = tuple[(str,str,float)]

def swap(list1 : list, value1 : int, value2 : int)->None:
    '''
    This function takes a list of values and two additonal values.
    The two additonal values indcate which values in list swap places. 
    '''
    swap1 = list1[value1]
    swap2 = list1[value2]
    list1[value1] = swap2
    list1[value2] = swap1
    
def index_of_smallest(list1 : list)->int:
    '''
    This function takes a list and retruns the index of the smallest value
    
    >>> index_of_smallest([12, 6, 2, 22, -14, 10, -2])
    4
    >>> index_of_smallest( ['a', 'b', 'd', 'c', 'a'])
    0
    >>> index_of_smallest( ['a', 'b', 'd', 'c', 'A'])
    4
    >>> index_of_smallest([])
    -1
    '''
    if list1 == []:
        return -1
    else:
        smallest = 0
        for index in range(len(list1)):
            if list1[index] < list1[smallest]:
                smallest = index
    return smallest
    
def total_duration(list1: list[FLIGHT_INFO])->int:
    '''
    This function takes a list of flight information containing:
    1.Starting city(must start with captial)
    2.Ending city(must start with capital
    3.Duration of flight( must be > 0)
    Then it returns the total flight duration.
    
    >>> total_duration([('Victoria', 'Mexico City', 5.5), ('Vancouver', 'Toronto', 4)])
    9.5
    >>> total_duration([('Victoria', 'Mexico City', 3), ('Vancouver', 'Toronto', 4)])
    7
    '''
    total = 0
    for index in range(len(list1)):
        total += list1[index][2]
    return total

def get_destinations_from(list1 : list[FLIGHT_INFO], start_city : str)->list:
    '''
    This function takes a list of flight information containing:
    1.Starting city(must start with captial)
    2.Ending city(must start with capital
    3.Duration of flight( must be > 0)
    The takes another argument starting a starting city and the function then
    returns a list of all possible end desinations form that starting city.
    
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Victoria','Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)],'Victoria')
    ['Vancouver', 'Calgary']
    >>> get_destinations_from([('Victoria', 'Vancouver', 0.75), ('Vancouver', 'Toronto', 4), ('Toronto','Calgary', 1.5), ('Victoria', 'Vancouver', 0.5)],'Victoria')
    ['Vancouver']
    '''
    result_list =[]
    for index in range(len(list1)):
        if list1[index][0] == start_city and list1[index][1] not in result_list:
            result_list.append(list1[index][1])
    return result_list

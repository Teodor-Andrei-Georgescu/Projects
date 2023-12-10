import doctest

def is_proper_divisor(num1 : int, num2 : int) -> bool:
    '''
    This function takes two integer values and determines if the first value is a factor of the second.
    
    Precondition = both integer values >= 0
    >>> is_proper_divisor(2,4)
    True
    >>> is_proper_divisor(0,2)
    False
    >>> is_proper_divisor(2,0)
    True
    >>> is_proper_divisor(1,1)
    False
    >>> is_proper_divisor(0,0)
    True
    
    '''
    if num1 == num2:
        if num1 == 0 and num2 == 0 :
            return(True)
        else:
            return(False)
    elif num1 == 0 and num2!= 0:
        return(False)
    elif num1 > num2 and num2 != 0:
        return(False)
    else:
        return (num2 % num1) == 0

def sum_of_proper_divisors(num : int) -> int:
    '''
    When given an integer this functon will return the sum if its proper divisors/factors.
    
    >>> sum_of_proper_divisors(0)
    0
    >>> sum_of_proper_divisors(1)
    0
    >>> sum_of_proper_divisors(2)
    1
    >>> sum_of_proper_divisors(3)
    1
    >>> sum_of_proper_divisors(4)
    3
    >>> sum_of_proper_divisors(12)
    16
     
    '''
    divisor_sum = 0
    for factor in range(1, num):
        if (num % factor) == 0:
            divisor_sum += factor
    return(divisor_sum)

def get_abundance(num :int) -> int:
    '''
    When given an integer this functon will return its abundance.
    If there number is not abundant it will return 0.
    
    Precondition = The given integer > 0 
    
    >>> get_abundance(1)
    0
    >>> get_abundance(6)
    0
    >>> get_abundance(8)
    0
    >>> get_abundance(10)
    0
    >>> get_abundance(12)
    4
    >>> get_abundance(16)
    0
    ''' 
    sum_of_divisors = sum_of_proper_divisors(num)
    if sum_of_divisors <= num:
        return 0
    else:
        return(sum_of_divisors - num)

def get_multiples(beginning_number : int, the_multiple : int, number_of_multiples : int) -> str:
    '''
    Function must be given three integers:
    1. The beginning number of the sequence
    2. The multiple
    3. Number of multiples that should be displayed in sequence
   
    Precondition = "Beginning number" value must be a multiple of "the multiple" value given
    and all values given must be >= 0
   
    >>> get_multiples(8, 2, 7)
    '8 10 12 14 16 18 20'
    >>> get_multiples(8, 2, 0)
    ''
    >>> get_multiples(8, 2, 1)
    '8'
    '''
    return_str = ''
    if beginning_number < the_multiple:
        inital_sequence_start = beginning_number
    else :
        inital_sequence_start = beginning_number // the_multiple
    sequence_end = inital_sequence_start + number_of_multiples
    for sequence in range(inital_sequence_start, sequence_end):
        multiple = sequence * the_multiple
        return_str += str(multiple) + ' '
    return(return_str[:-1])


def print_multiplication_table(hstart_number : int, table_width : int, vstart_number : int, table_height : int):
    '''
    This function prints out a multipication tabke based on the given specifications.
    1.Horizontal start number 
    2.The table wdidth
    3.The vertical start number
    4.The table height 
    
    Preconidtion = The vertical and horizontal start values >= 0 and
    the table width and height values > 0
    
    >>> print_multiplication_table(0,3,4,10)
     0 1 2 
     4 0 4 8
     5 0 5 10
     6 0 6 12
     7 0 7 14
     8 0 8 16
     9 0 9 18
     10 0 10 20
     11 0 11 22
     12 0 12 24
     13 0 13 26
    >>> print_multiplication_table(1,1,1,1)
     1 
     1 1
    >>> print_multiplication_table(2,6,8,10)
     2 3 4 5 6 7 
     8 16 24 32 40 48 56
     9 18 27 36 45 54 63
     10 20 30 40 50 60 70
     11 22 33 44 55 66 77
     12 24 36 48 60 72 84
     13 26 39 52 65 78 91
     14 28 42 56 70 84 98
     15 30 45 60 75 90 105
     16 32 48 64 80 96 112
     17 34 51 68 85 102 119

    >>> print_multiplication_table(1,5,12,4)
     1 2 3 4 5 
     12 12 24 36 48 60
     13 13 26 39 52 65
     14 14 28 42 56 70
     15 15 30 45 60 75
     '''
    hend = hstart_number + table_width
    vend = vstart_number + table_height
    return_str = ' '
   
    for horizontal_axis in range(hstart_number, hend):
        return_str += str(horizontal_axis) + ' '
    print(return_str)
    for vertical_axis in range(vstart_number,vend):
        print('',vertical_axis,end=' ')
        the_multiple = get_multiples(hstart_number, vertical_axis, table_width)
        return_str2 = str(the_multiple)
        print(return_str2)

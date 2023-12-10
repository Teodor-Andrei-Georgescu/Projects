import doctest

def compute_harmonic_series(num : int) -> float:
    '''
    This function will take an integer and compute and returns the sum of the harmonic series to thatt integer.
    
    Precondition = The integer value given must be >= 0
    
    >>> compute_harmonic_series(0)
    0
    >>> compute_harmonic_series(1)
    1.0
    >>> compute_harmonic_series(2)
    1.5
    >>> compute_harmonic_series(3)
    1.8333333333333333
    >>> compute_harmonic_series(4)
    2.083333333333333
    '''
    if num == 0:
        return 0       
    else:
        series_total = 0
        for harmonic_series in range(1,num+1):
            series = 1 / harmonic_series
            series_total += series
        return series_total

def get_fibonnaci_sequence(num : int) -> str:
    '''
    This function takes an integer and returns a string of the Fibonacci sequence to same value as the given integer
    
    Preconiditon = The integer value given >= 0
    
    >>> get_fibonnaci_sequence(0)
    ''
    >>> get_fibonnaci_sequence(1)
    '0'
    >>> get_fibonnaci_sequence(2)
    '0,1'
    >>> get_fibonnaci_sequence(3)
    '0,1,1'
    >>> get_fibonnaci_sequence(4)
    '0,1,1,2'
    '''
    first_num = 0 
    second_num = 1
    return_string = '0,1,'
    
    if num == 0:
        return '' 
    elif num == 1:
        return('0')
    else:
        for fibonacci in range(3,num + 1):
            new_num = first_num + second_num
            first_num = second_num
            second_num = new_num
            return_string += str(new_num) + ','
        return(return_string[:-1])
    
def print_pattern(height : int, width : int, character1 : str, character2 : str) -> None:
    '''
    This function takes in two characters as strings and 2 integers for height and width.
    Based on these inputed values it will print out a pattern based on those specifcations.
    
    Precondition = Both inputed integer values > 0
    
    >>> print_pattern(4,3, '!@', '$$$')
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    !@$$$!@$$$!@$$$
    $$$!@$$$!@$$$!@
    
    >>> print_pattern(1,1,'!@','$$$')
    !@$$$
    '''
    for row in range(height):
        for thickness in range(width):
            row_even_or_odd = row % 2
            if row_even_or_odd == 0:
                pattern = (character1 + character2) * width
            else:
                pattern = (character2 + character1) * width
        print(pattern)
        

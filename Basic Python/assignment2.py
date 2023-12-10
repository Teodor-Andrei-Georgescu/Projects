import doctest

def add_to_cart(item_price : int, cart_balance: int, account_balance : int):
    '''
    This function add the price of an item to your cart.
    The function will then print out the total price of all the items in the cart.
    If the cart value is greater than your account balance it will print out the required additional funds.
    >>> add_to_cart(10, 20, 25)
    not enough funds! You need an additional $ 5
    >>> add_to_cart(10, 20, 30)
    cart balance $ 30
    '''
    if (item_price + cart_balance) > account_balance:
        required_funds = (item_price + cart_balance) - account_balance
        print(f'not enough funds! You need an additional $ {round(required_funds,0)}')
    else:
        total_cart_balance = item_price + cart_balance
        print(f'cart balance $ {round(total_cart_balance, 0)}')

def print_smallest(value_1 : int, value_2 : int, value_3 : int):
    '''
    Given 3 values this function prints the smallest value.
    >>> print_smallest(1,2,3)
    1
    >>> print_smallest(1,2,2)
    1
    >>> print_smallest(1,1,1)
    1
    >>> print_smallest(2,1,3)
    1
    >>> print_smallest(3,1,2)
    1
    >>> print_smallest(3,2,1)
    1
    >>> print_smallest(2,2,1)
    1
    >>> print_smallest(2,1,2)
    1
    '''
    if value_1 >= value_2 > value_3 or value_2 >= value_1 > value_3:
        print(value_3)
    elif value_1 >= value_3 > value_2 or value_3 >= value_1 > value_2:
        print(value_2)
    else:
        print(value_1)

def is_multiple_of(number_1 : int, number_2 : int):
    '''
    When given two integers the function will print of the first value is a multiple of the second.
    >>> is_multiple_of(12,3)
    12 is a multiple of 3
    >>> is_multiple_of(12,-3)
    12 is a multiple of -3
    >>> is_multiple_of(12,5)
    12 is not a multiple of 5
    >>> is_multiple_of(12,0)
    12 is not a multiple of 0
    >>> is_multiple_of(0,5)
    0 is a multiple of 5
    '''
    if number_1 == 0:
        print(f'{number_1} is a multiple of {number_2}')
    elif number_2 == 0 or (number_1 % number_2) != 0  :
        print(f'{number_1} is not a multiple of {number_2}')
    else: 
        print(f'{number_1} is a multiple of {number_2}')

def print_triangle_type(angle_1 : int, angle_2 : int, angle_3 :int):
    '''
    Given the value of all 3 angle in a triangle this function will print out the corresponding type of triangle.
    >>> print_triangle_type(5,5,5)
    invalid triangle
    >>> print_triangle_type(-60,60,60)
    invalid triangle
    >>> print_triangle_type(60,-60,60)
    invalid triangle
    >>> print_triangle_type(60,60,-60)
    invalid triangle
    >>> print_triangle_type(60,60,60)
    acute
    >>> print_triangle_type(60,30,90)
    right
    >>> print_triangle_type(60,90,30)
    right
    >>> print_triangle_type(90,60,30)
    right
    >>> print_triangle_type(40,40,100)
    obtuse
    >>> print_triangle_type(40,100,40)
    obtuse
    >>> print_triangle_type(100,40,40)
    obtuse
    '''
    if (angle_1 + angle_2 + angle_3) != 180 or angle_1 <= 0 or angle_2 <= 0 or angle_3 <= 0:
        print('invalid triangle')
    elif angle_1 == 90 or angle_2 == 90 or angle_3 == 90:
        print('right')
    elif angle_1 > 90 or angle_2 > 90 or angle_3 > 90:
        print('obtuse')
    else:
        print('acute')

def print_time_in_seconds(number_of_days : int, number_of_hours : int, number_of_minutes : int, number_of_seconds : int):
    '''
    When given the number of days, hours, minutes, and seconds this function will convert everything to seconds and print the total number of seconds.
    >>> print_time_in_seconds(1,1,1,1)
    total time: 90061 seconds
    >>> print_time_in_seconds(1,1,1,-1)
    invalid time
    >>> print_time_in_seconds(1,1,-1,1)
    invalid time
    >>> print_time_in_seconds(1,-1,1,1)
    invalid time
    >>> print_time_in_seconds(-1,1,1,1)
    invalid time
    >>> print_time_in_seconds(1,1,1,0)
    total time: 90060 seconds
    >>> print_time_in_seconds(1,1,0,1)
    total time: 90001 seconds
    >>> print_time_in_seconds(1,0,1,1)
    total time: 86461 seconds
    >>> print_time_in_seconds(0,1,1,1)
    total time: 3661 seconds
    '''
    if number_of_days < 0 or number_of_hours < 0 or number_of_minutes < 0 or number_of_seconds < 0:
        print('invalid time')
    else:
        total_hours = number_of_days * 24 + number_of_hours
        total_minutes = total_hours * 60 + number_of_minutes
        total_seconds = total_minutes * 60 + number_of_seconds
        print(f'total time: {total_seconds} seconds')
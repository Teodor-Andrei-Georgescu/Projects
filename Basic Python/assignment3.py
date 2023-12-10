import doctest

KM_TO_M = 1000
GST = 0.05
PST = 0.07
SHIPPING_CHARGE = 4.50
DAYS_TO_HOURS = 24
HOURS_TO_MINUTES = 60
MINUTES_TO_SECONDS = 60
TEN_TO_TWENTY_BOX_DISCOUNT = 0.9 
TWENTY_PLUS_BOX_DISCOUNT = 0.8
NEW_CUSTOMER_DISCOUNT = 0.9

def get_smallest(num_1 : int, num_2 : int, num_3 : int) -> int:
    '''
    Given 3 values this function prints the smallest value.
    >>> get_smallest(1,2,3)
    1
    >>> get_smallest(1,2,2)
    1
    >>> get_smallest(1,1,1)
    1
    >>> get_smallest(2,1,3)
    1
    >>> get_smallest(3,1,2)
    1
    >>> get_smallest(3,2,1)
    1
    >>> get_smallest(2,2,1)
    1
    >>> get_smallest(2,1,2)
    1
    '''
    if num_1 >= num_2 > num_3 or num_2 >= num_1 > num_3:
        return(num_3)
    elif num_1 >= num_3 > num_2 or num_3 >= num_1 > num_2:
        return(num_2)
    else:
        return(num_1)
def get_time_in_seconds(number_of_days : int, number_of_hours : int, number_of_minutes : int, number_of_seconds : int) -> int:
    '''
    When given the number of days, hours, minutes, and seconds this function will convert everything to seconds and print the total number of seconds.
    
    Preconidition = all values must be >= 0
    
    >>> get_time_in_seconds(1,1,1,0)
    90060
    >>> get_time_in_seconds(1,1,0,1)
    90001
    >>> get_time_in_seconds(1,0,1,1)
    86461
    >>> get_time_in_seconds(0,1,1,1)
    3661
    >>> get_time_in_seconds(0,0,0,0)
    0
    '''
    total_hours = number_of_days * DAYS_TO_HOURS + number_of_hours
    total_minutes = total_hours * HOURS_TO_MINUTES + number_of_minutes
    total_seconds = total_minutes * MINUTES_TO_SECONDS + number_of_seconds
    return(total_seconds)

def get_average_speed(distance_travelled_in_km : float, number_of_days : int, number_of_hours : int, number_of_minutes : int, number_of_seconds : int) -> float:
    '''
    This function must be given 5 values:
    1 Distance travelled in kilometers 
    2.Number of days 
    3.Number of hours 
    4.Number of minutes 
    5.Number of seconds 
    Then this function will print out the speed in meters per second.
    
    Preconditon = All time arguments must be ints and atleast one must be > 0. The distance argument can be float but >= 0.
    
    >>> get_average_speed(170863.9, 1, 1, 1, 1)
    1897.2018964923775
    >>> get_average_speed(170863.9, 0, 0, 0, 1)
    170863900.0
    >>> get_average_speed(170863.9, 0, 0, 1, 0)
    2847731.6666666665
    >>> get_average_speed(170863.9, 0, 1, 0, 0)
    47462.194444444445
    >>> get_average_speed(170863.9, 1, 0, 0, 0)
    1977.5914351851852

    '''
    time_in_seconds = get_time_in_seconds(number_of_days, number_of_hours, number_of_minutes, number_of_seconds)
    distance_travelled_in_meters = distance_travelled_in_km * KM_TO_M
    speed_in_meters_per_second = distance_travelled_in_meters / time_in_seconds
    return(speed_in_meters_per_second)

def get_box_charge(num_boxes : int, price_per_box : float) -> float:
    '''
    Function must be given number of boxes and price per box. 
    This function will then print the total price of all the boxes including the discounts.
    
    Precondition = number of boxes can not be negative and price per box must be great then 0.
    
    >>> get_box_charge(0, 12.5)
    0.0
    >>> get_box_charge (9, 10)
    90
    >>> get_box_charge (10, 10)
    90.0
    >>> get_box_charge (19, 10)
    171.0
    >>> get_box_charge (20, 10)
    160.0
    '''
    total_charge = num_boxes * price_per_box
    if 19 >= num_boxes >= 10:
        new_total = total_charge * TEN_TO_TWENTY_BOX_DISCOUNT
    elif num_boxes >= 20:
        new_total = total_charge * TWENTY_PLUS_BOX_DISCOUNT
    else:
        new_total = total_charge
    return(new_total)

def get_order_charge(new_or_old_customer : bool, num_boxes1 : int, price_per_box1 :float, num_boxes2 : int, price_per_box2 : float) -> float:
    '''
    This function must be given:
    1.If the customer is new (Truefor new customer)
    2.Number of boxes for first prescription
    3.Price per box for first prescription
    4.Number of boxes for second prescription
    5.Price per box for second prescription
    
    After given the values the function will print the total amount due after adding all discounts and taxes.
    
    Precondition = number of any boxes is not negative and price per box is greater than 0.
    
    >>> get_order_charge(False, 1, 12.5, 2, 9.5)
    39.78
    >>> get_order_charge(True, 1, 12.5, 2, 9.5)
    36.252
    >>> get_order_charge(False, 11, 12.5, 5, 9.5)
    191.8
    >>> get_order_charge(True, 11, 12.5, 5, 9.5)
    172.62
    '''
    prescription_total_charge = get_box_charge(num_boxes1, price_per_box1) + get_box_charge(num_boxes2, price_per_box2)
    if new_or_old_customer == True :
        discounted_total = prescription_total_charge * NEW_CUSTOMER_DISCOUNT
        tax_amount = discounted_total * (GST + PST)
        tax_included_price = discounted_total + tax_amount
        if 100 > tax_included_price > 0:
            total_charge = tax_included_price + SHIPPING_CHARGE
            return(total_charge)
        else:
            return(tax_included_price)
    else:
        tax_amount = prescription_total_charge * (GST + PST)
        tax_included_price = prescription_total_charge + tax_amount
        if 100 > tax_included_price > 0:
            total_charge = tax_included_price + SHIPPING_CHARGE
            return(total_charge)
        else:
            return(tax_included_price)

def place_order(account_balance : float ,new_or_old_customer : bool, num_boxes1 : int, price_per_box1 :float, num_boxes2 : int, price_per_box2 : float) -> bool:
    '''
    This function must be given:
    1.Account balance
    2.If the customer is new (True for new, False for old)
    3.Number of boxes for first prescription
    4.Price per box for first prescription
    5.Number of boxes for second prescription
    6.Price per box for second prescription
    
    After given the values the function will print true or false to indcate if the order could be placed.
    True means the account balance is >= total price and that the order can be placed.
    False means the exact opposite.
    
    Precondition = number of any boxes and account balance is not negative and price per box is greater than 0.
    
    >>> place_order(40.50, False , 1, 12.5, 2, 9.5)
    True
    >>> place_order(39.78, False, 1, 12.5, 2, 9.5)
    True
    >>> place_order(39.77, False, 1, 12.5, 2, 9.5)
    False
    '''
    total_price = get_order_charge(new_or_old_customer, num_boxes1, price_per_box1, num_boxes2, price_per_box2)
    return account_balance >= total_price   


def get_middle(word : str) -> str:
    '''
    When this function is given a string it will return the middle of the string.
    
    >>> get_middle('Victoria')
    'to'
    >>> get_middle('Vancouver')
    'o'
    >>> get_middle('')
    ''
    >>> get_middle('hello')
    'l'
    >>> get_middle('andrei')
    'dr'
    '''
    str_len = len(word)
    even_or_odd = str_len % 2
    if even_or_odd == 0:
        middle = str_len // 2
        return word[middle-1: middle+1]
    else:
        almost_middle = (str_len-1) // 2
        return word[almost_middle]
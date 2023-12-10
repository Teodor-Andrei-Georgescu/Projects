import doctest

GST = 0.05
PST = 0.1

def get_longer(string_1 : str, string_2 : str) -> str:
    '''
    When given two string this function will return the longer of the two.
    
    >>> get_longer('hi','yo')
    'hi'
    >>> get_longer('yo','hi')
    'yo'
    >>> get_longer('hi','there')
    'there'
    >>> get_longer('andrei','mark')
    'andrei'
    '''
    string_1_length = len(string_1)
    string_2_length = len(string_2)
    if string_1_length == string_2_length or string_1_length > string_2_length:
        return string_1 
    else:
        return string_2

def get_tax(food_price : float, alcohol_price : float) -> float:
    '''
    When given the price of food and alcohol this function will return the total tax.
    
    Precondition = money owed for food and alcohol is >= $0
    
    >>> get_tax(28.75, 45.98)
    8.3345
    >>> get_tax(0,0)
    0.0
    '''
    food_tax = food_price * GST
    alcohol_tax = alcohol_price * (GST + PST)
    return(food_tax + alcohol_tax)

def get_bill_share(food_price : float, alcohol_price : float, num_people : int) -> float:
    '''
    This function must be given the price of food and alcohol and number of people.
    It will then calclate how much each person must pay, including tax, if the bill is to be shared.
    
    Preconidtion = money owed for food aand alcohol >= 0 and number of pople >= 1.
    
    >>> get_bill_share(18.93, 0, 2)
    9.93825
    >>> get_bill_share(0, 0, 1)
    0.0
    '''
    tax = get_tax(food_price, alcohol_price)
    amount_per_person = (tax + food_price + alcohol_price) / num_people
    return(amount_per_person)
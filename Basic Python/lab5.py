import doctest

def name_age_category_helper_function(age:int, name : str) -> str:
    '''
    Helper function that decides the proper greeting based on the age and name given.
    '''
    greeting = 'hello ' + name
    if age < 18:
        greeting += ' child'
    elif 64 >= age >= 18:
        greeting += ' adult'
    else:
        greeting += ' senior'
    return greeting


def print_name_age_v1():
    '''
    Prompts user to enter their name and age.
    Then prints out coresponding greeting.
    
    Preconditon: Age >=0
    '''
    name = input('enter name: ')
    age = input('enter age: ')
    age = int(age)
    greeting = name_age_category_helper_function(age, name)
    print(greeting)

def print_name_age_v2():
    '''
    Prompts user to enter their name and age.
    Then prints out coresponding greeting.
    '''    
    name = input('enter name: ')
    age = input('enter age: ')
    if age.isdigit() == False:
        print(f'{name} you are lying about your age')
    else:
        age = int(age)
        greeting = name_age_category_helper_function(age, name)
        print(greeting)

def get_num(num : int)-> int:
    '''
    Take a minium value then prompts the user to enter a value.
    It will ask user to keep inputing number unitl it is a valid number and greater
    than the minimum number.
    
    Precondition = Minimum number >= 0
    '''
    prompt = 'enter a valid number: '
    number = input(prompt)
    while True:
        if number.isdigit() == False:
            number = input(prompt)
        elif int(number) >= num:
            return int(number)
        else:
            number = input(prompt)
    
        
        
def print_name_age_v3():
    '''
    Prompts user to enter their name and age.
    Then prints out coresponding greeting.
    '''     
    name = input('enter name: ')
    print('enter age: ')
    age = get_num(0)
    greeting = name_age_category_helper_function(age, name)
    print(greeting)    
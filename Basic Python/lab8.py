import doctest 

#Takes in a persons name as a string, and a persons age as a integer
#(['Andrei', 18])
Person = tuple([str,int])

def file_to_person_list(filename : str) -> list[Person]:
    '''
    This function takes a file name in and returns a list of peoples names and ages.
    
    >>> file_to_person_list('lab8-name-age.txt')
    [('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)]
    '''
    result_list = []
    file = open(filename,'r')
    line = file.readline()
    while line != '':
        line = line.strip('\n')
        line = line.split(' ')
        line[1] = int(line[1])
        result_list.append(tuple(line))
        line = file.readline()
    file.close()
    return result_list

def get_average_age(list1 : list[Person]) -> int:
    '''
    This function takes a list of peopls information:
    1.Name
    2.Age
    Then it returns the average age of all those in the list.
    
    Precondtion = list != ''
    
    >>> get_average_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)])
    31
    '''
    count = 0
    total = 0
    for index in range(len(list1)):
        count += 1
        total += list1[index][1]
    avrg = total // count
    return (avrg)

def get_above_age(list1 : list[Person], threshold : int)-> list[Person]:
    '''
    This function takes a list of personal information:
    1.name
    2.age
    Then takes and age threshold value.
    The function will return a list of person infromation of those whose age is
    higher than the threshold value.
    
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)],31)
    [('Jose', 53), ('Rajan', 65)]
    >>> get_above_age([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)],90)
    []
    >>> get_above_age([],31)
    []
    '''
    result_list = []
    for index in range(len(list1)):
        if list1[index][1] > threshold:
            result_list.append(list1[index])
    return result_list

def to_file(list1 : list[Person], filename: str)-> None:
    '''
    Funtiokn takes a list of personal information containing:
    1.Name
    2.Age
    Then takes a file name, and it will write the given list of infromation
    in the given file name.
    
    >>> to_file([('Lynden', 6), ('Tian', 27), ('Daljit', 18), ('Jose', 53), ('Jingwen', 17), ('Rajan', 65)], 'text_file.txt')
    '''
    file = open(filename, 'w')
    for index in range(len(list1)):
        if (len(list1)-1) != index:
            file.write(f'{list1[index][0]}, {list1[index][1]}\n')
        else:
            file.write(f'{list1[index][0]}, {list1[index][1]}')
    file.close()

def write_names_above_avg_age(input_file : str, output_file : str) ->None:
    '''
    This funtion takes the name of an input file and an output file.
    It will read through the person information in the input file,
    find the average age, then print the information of those above the average 
    age in the output file.
    
    >>> write_names_above_avg_age('lab8-name-age.txt','text_file.txt')
    '''
    people_list = file_to_person_list(input_file)
    avg = get_average_age(people_list)
    people_above_avg_age_list = get_above_age(people_list,avg)
    to_file(people_above_avg_age_list,output_file)
import doctest

import student

Student = student.Student

def get_students(filename : str)-> list[Student]:
    '''
    The function takes in a file name and returns a list of Student objects using the data in the given file.
    
    Precondition: The file entered contains valid rows of data and all student id are unique. 
    
    >>> get_students('student_data.csv')
    [Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)]
    '''
    result_list =[]
    file = open(filename, 'r')
    line = file.readline()
    while line != '':
        line = line.strip()
        line= line.split(',')
        stdnt = Student(line[0],line[1])
        result_list.append(stdnt)
        line = file.readline()
    
    file.close()
    return result_list

def get_student(list1 = list[Student])-> list[str]:
    '''
    The function takes in a list of Student instances and creates and returns a new list of just the 
    student ids of all Student instances in the list.
    
    >>> get_student([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)])
    ['V00123456', 'V00123457', 'V00123458', 'V00123459']
    '''
    result_list = []
    for index in range(len(list1)):
        sid = list1[index].get_sid()
        result_list.append(sid)
    return result_list

def count_above(list1 : list[Student], threshold : int)->int:
    '''
    The function takes in a list of Student instances and a threshold grade, and returns a count of the number of Students instances in the list that
    have a grade above the threshold. 
    
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 90)
    1
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 100)
    0
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 0)
    4
    >>> count_above([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)], 89)
    1
    '''
    count = 0
    for index in range(len(list1)):
        grade = list1[index].get_grade()
        if grade > threshold: 
            count += 1
    return count

def get_average_grade(list1: list[Student]) -> float:
    '''
    The function takes in a list of Student instances and calculates and returns the average grade of 
    all Student instances in the list as a floatingpoint number. 
    
    Precondition: the list of Student instances entered is not empty.

    >>> get_average_grade([Student('V00123456', 89), Student('V00123457', 99), Student('V00123458', 30), Student('V00123459', 78)])
    74.0
    '''
    total= 0
    for index in range(len(list1)):
        total += list1[index].get_grade()
    average = total / len(list1)
    return average
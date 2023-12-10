import doctest

class Student:
    """ Student with unique id (sid) and current grade (grade)"""

    def __init__(self, sid: str, grade: int) -> None:
        """ initializes an instance of a Student with sid and grade
        >>> stdnt = Student('V00123456', 89)
        """
        self.__sid = sid
        self.__grade = grade

    def __str__(self) -> str:
        """ return a formatted string with sid and grade of self Student
        >>> stdnt = Student('V00123456', 89)
        >>> str(stdnt)
        'V00123456: 89/100'
        """
        return f'{self.__sid}: {self.__grade}/100'

    def __repr__(self) -> str:
        """ return a formatted string  with student attributes
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt
        Student('V00123456', 89)
        """        
        return f"Student('{self.__sid}', {self.__grade})"
    
    
    # TODO: add documentation for these instance methods
    def get_sid(self)->str:
        '''
        This function returns a student sid.
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt.get_sid()
        'V00123456'
        '''
        return self.__sid

    def get_grade(self)-> str:  
        '''
        This funtion returns a students grade.
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt.get_grade()
        89
        '''
        return self.__grade

    def set_grade(self, grade):
        '''
        This function updates the students grade to a new value.
        >>> stdnt = Student('V00123456', 89)
        >>> stdnt.set_grade(80)
        '''
        self.__grade = grade
        
def is_sid_equal(student1: Student, student2 : Student)->bool:
    '''
    This function will compare 2 student objects and will return wether or not
    thier sids are the same.

    >>> is_sid_equal(Student('V00123456', 89),Student('V00123456', 45))
    True
    >>> is_sid_equal(Student('V00123456', 89),Student('V00123451', 45))
    False
    '''
    return student1.get_sid() == student2.get_sid()
def is_grade_above(self, threshold : int)-> bool:
    '''
    This function cpares a studnets grade with the grade threshold and returns
    if the students grades is above the threshold.
    
    >>> stdnt = Student('V00123456', 89)
    >>> is_grade_above(stdnt,90)
    False
    >>> is_grade_above(stdnt,80)
    True
    '''
    
    grade = self.get_grade()
    
    return grade > threshold
    

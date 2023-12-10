import doctest

class Date:
    """ Date: represents a date in the Gregorian calendar used worldwide.
    Precondition, month, day, year must make a valid calendar date.
    """   

    def __init__(self, month: int, day: int, year: int) -> None:
        """ initializes attributes of Date instance
        >>> dt = Date(12, 19, 2020)
        """
        self.__month  = month
        self.__day    = day
        self.__year   = year


    def get_month(self) -> int:
        """ returns month of self Date instance
        >>> dt = Date(12, 19, 2020)
        >>> dt.get_month()
        12
        """
        return self.__month

    def get_day(self) -> int:
        """ returns day of self Date instance
        >>> dt = Date(12, 19, 2020)
        >>> dt.get_day()
        19
        """        
        return self.__day
 
    def get_year(self) -> int:
        """ returns year of self Date instance
        >>> dt = Date(12, 19, 2020)
        >>> dt.get_year()
        2020
        """          
        return self.__year
    
    def __str__(self) -> str:
        """ returns a readable string with month, day, year of Date
        >>> dt = Date(12, 19, 2020)
        >>> str(dt)
        '12-19-2020'
        """
        return f'{self.__month}-{self.__day}-{self.__year}'
    
    def __repr__(self) -> str:
        """ returns a string representation of self Date
        >>> dt = Date(12, 19, 2020)
        >>> repr(dt)
        'Date(12, 19, 2020)'
        """
        return f'Date({self.__month}, {self.__day}, {self.__year})'

    def __eq__(self, other: 'Date') -> bool:
        """ returns True if self Date has same month, day, year as 
        other Date, otherwise False
        >>> dt12192020a = Date(12, 19, 2020)
        >>> dt12192020b = Date(12, 19, 2020)
        >>> dt12192021  = Date(12, 19, 2021)
        >>> dt12182020  = Date(12, 18, 2020)
        >>> dt11192020  = Date(11, 19, 2020)
        
        >>> dt12192020a == dt12192020a
        True
        >>> dt12192020a == dt12192020b
        True
        >>> dt12192020a == dt12192021
        False
        >>> dt12192020a == dt12182020
        False
        >>> dt12192020a == dt11192020
        False
        """
        return (self.__month == other.__month and self.__day == other.__day and self.__year == other.__year)
    
    def is_after(self, other_date: 'Date') -> bool:
        '''
        This function takes in two arguments:
        1) the hidden reference to the Date instance itself (self).
        2) an additional instance of a date (other).
        The function then returns True if the date represented by self is after 
        the date that is represented by other in the calendar and False otherwise.
        
        >>> dt12192020a = Date(12, 19, 2020)
        >>> dt12192020b = Date(12, 19, 2020)
        >>> dt12192021  = Date(12, 19, 2021)
        >>> dt12182020  = Date(12, 18, 2020)
        >>> dt11192020  = Date(11, 19, 2020)
        
        >>> dt12182020.is_after(dt11192020)
        True
        >>> dt12192021.is_after(dt12182020)
        True
        >>> dt12192020a.is_after(dt12192020b)
        False
        >>> dt12192020b.is_after(dt12192021)
        False
        '''
        if self == other_date:
            return False
        is_date_self_after_date_other = True
        day_self = self.get_day()
        month_self = self.get_month()
        year_self = self.get_year()
        day_other = other_date.get_day()
        month_other = other_date.get_month()
        year_other = other_date.get_year()
        if year_self > year_other:
            is_date_self_after_date_other = True
        elif year_self == year_other and month_self > month_other:
            is_date_self_after_date_other = True
        elif year_self == year_other and month_self == month_other and year_self > year_other:
            is_date_self_after_date_other = True
        else:
            is_date_self_after_date_other = False    
        return is_date_self_after_date_other
            
        
    

    
    
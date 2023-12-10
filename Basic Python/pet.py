import doctest

from date import Date

class Pet:
    """ Pet: represents a domesticated pet with name, species and birthdate """

    def __init__(self, name: str, species: str, birthdate: Date) -> None:
        """ initializes attributes of Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        """
        self.__name      = name
        self.__species   = species
        self.__birthdate = birthdate

    def get_name(self) -> str:
        """ returns name of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> dog.get_name()
        'Rover'
        """
        return self.__name

    def get_species(self) -> str:
        """ returns species of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> dog.get_species()
        'Dog'
        """
        return self.__species
    
    def get_birthdate(self) -> Date:
        """ returns date of self Pet instance
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        
        >>> dog.get_birthdate()
        Date(12, 19, 2020)
        """
        return self.__birthdate
    
    def __str__(self) -> str:
        """ returns a readable string with name, species, birthdate of Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> str(dog)
        'Rover is a Dog. Born: 12-19-2020'
        """
        return f'{self.__name} is a {self.__species}. Born: {self.__birthdate}'
    
    def __repr__(self) -> str:
        """ returns a string representation of self Pet
        >>> dt = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dt)
        >>> repr(dog)
        "Pet('Rover', 'Dog', Date(12, 19, 2020))"
        """
        return f"Pet('{self.__name}', '{self.__species}', {repr(self.__birthdate)})"
    
    def __eq__(self, other: 'Pet') -> bool:
        '''
        When an object of a Pet is compared to another object 
        of a Pet using '==', the function returns True if the name, species, and 
        birthdate of the two Pet objects are the same and returns 
        False otherwise. 
        
        >>> dtd1 = Date(12, 19, 2020)
        >>> dog = Pet('Rover', 'Dog', dtd1)
        >>> dtc = Date(10, 24, 2021)
        >>> cat = Pet('Tom', 'Cat', dtc)
        >>> dtd2 = Date(12, 19, 2020)
        >>> dog2 = Pet('Dolly', 'Dog', dtd2)
        >>> dtc2 = Date(10, 24, 2021)
        >>> cat2 = Pet('Tom', 'Cat', dtc2)
        
        >>> dog == cat
        False
        >>> cat == cat2
        True
        >>> dog == dog2
        False
        '''
        return (self.get_birthdate() == other.get_birthdate() and self.get_name() == other.get_name() and self.get_species() == other.get_species())






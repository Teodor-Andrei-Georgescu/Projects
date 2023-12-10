import doctest

DATE = tuple[(int, int, int)]
# DATE is a type alias that represents a valid date (year number, month number, day number).
# Theyear, month, and day values are assumed to be valid numbers.
# Example: (2003, 10, 24)

SHOW_INFORMATION = tuple[(str, str, list[str], list[str], DATE)]
# SHOW_INFORMATION is a type alias that represents a Netflix show information (type of show, title of show, list of directors, list of actors, date the show was added).
# Example: ('Series', 'The Queens Gambit', ['Marielle Heller'], ['Anya Taylor Joy', 'Thomas Brodie Sangster', 'Harry Melling'], (10, 23, 2020))

def multiply_by(list1 : list[int], list2 : list[int])->None:
    '''
    This function takes a two lists and multiples the first by the second and 
    return the result as a list.
    '''
    if len(list1) < len(list2):
        for index in range(len(list1)):
            list1[index] *= list2[index] 
    else:
        for index in range(len(list2)):
            list1[index] *= list2[index] 

def create_date(date_as_str : str)-> DATE:
    '''
    This function takes a date as a string in a specficed order:
    'Day-month'year' where dayand year must be 2 digits long and month must be 
    the first 3 letter with the first letter capitalized
    
    Then it returnes the date as a tuple.
    
    >>> create_date('10-Jan-18')
    (2018, 1, 10)
    >>> create_date('22-Feb-00')
    (2000, 2, 22)
    >>> create_date('22-Dec-00')
    (2000, 12, 22)
    '''
    date_as_list = date_as_str.split('-')
    day = date_as_list[0]
    month = date_as_list[1]
    year = date_as_list[2]
    year = '20' + str(year)
    year = int(year)
    day = int(day)
    if month == 'Jan':
        month = 1
    elif month == 'Feb':
        month = 2
    elif month == 'Mar':
        month = 3
    elif month == 'Apr':
        month = 4
    elif month == 'May':
        month = 5
    elif month == 'Jun':
        month = 6
    elif month == 'Jul':
        month = 7
    elif month == 'Aug':
        month = 8
    elif month == 'Sep':
        month = 9
    elif month == 'Oct':
        month = 10
    elif month == 'Nov':
        month = 11
    else:
        month = 12 
    date_as_tuple = []
    date_as_tuple.append(year)
    date_as_tuple.append(month)
    date_as_tuple.append(day)
    return tuple(date_as_tuple)

def create_show(show_type : str, show_title : str, directors : str, actors :str, date : str)-> SHOW_INFORMATION:
    '''
    This function take 5 arguments as strings:
    1.Show type
    2.Show title
    3.Directors
    4.Actors 
    5.Date
    It then returns a tuple with all the information together.
    
    >>> create_show('Movie', 'The Invention of Lying', 'Ricky Gervais:Matthew Robinson','Ricky Gervais:Jennifer Garner:Jonah Hill:Rob Lowe:Tina Fey', '02-Jan-18')
    ('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2))

    >>> create_show('TV Show', 'The Mind Explained', '', 'Emma Stone', '12-Sep-09')
    ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))
    
    >>> create_show('Movie', 'The Bad Kids', 'Keith Fulton:Louis Pepe', '', '01-Apr-17')
    ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1))
    '''
    date = create_date(date)
    if directors != '':
        directors = directors.split(':')
    else:
        directors = []
    if actors != '':
        actors = actors.split(':')
    else:
        actors = []
    result_tuple = []
    result_tuple.append(show_type)
    result_tuple.append(show_title)
    result_tuple.append(directors)
    result_tuple.append(actors)
    result_tuple.append(date)
    return tuple(result_tuple)

def get_titles(info : list[SHOW_INFORMATION]) ->list[str]:
    '''
    This function takes a list of intflix shows and thier information
    then returns a list with the show titles.
    
    >>> get_titles([('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['Ricky Gervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2009, 9, 12))])
    ['The Invention of Lying', 'The Mind Explained']
    '''
    titles = []
    for index in range(len(info)):
        titles.append(info[index][1])
    return titles 

def is_actor_in_show(info : SHOW_INFORMATION, is_actor : str) -> bool:
    '''
    This function takes a list of a show and its information and andiaction string
    which will be a name of the actor.
    The function will to see if that actor is in the show.
    
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['RickyGervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Rob Lowe')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['RickyGervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'roB lowE')
    True
    >>> is_actor_in_show(('Movie', 'The Invention of Lying', ['Ricky Gervais', 'Matthew Robinson'], ['RickyGervais', 'Jennifer Garner', 'Jonah Hill', 'Rob Lowe', 'Tina Fey'], (2018, 1, 2)), 'Emma Stone')
    False
    '''
    is_actor = is_actor.lower()
    for index in range(len(info[3])):
        actor_in = info[3][index]
        actor_in = actor_in.lower()
        if actor_in == is_actor:
            return True
    return False

def count_shows_before_date(info : list[SHOW_INFORMATION], date_threshold : DATE)-> int:
    '''
    This function takes a list of show information if multiple shows
    then takes a another date as and argument and will return how many shows are
    the entered dated.
    
    >>> count_shows_before_date([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)),('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen','Jemima Kirke'], (2018, 9, 21)),('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],(2018, 12, 12))
    2
    ''' 
    result = 0
    year = date_threshold[0]
    month = date_threshold[1]
    day = date_threshold[2]
    for index in range(len(info)):
        if info[index][4][0] < year:
            result += 1
        elif info[index][4][0] == year and info[index][4][1] < month:
            result += 1
        elif info[index][4][0] == year and info[index][4][1] == month and info[index][4][2] < day:
            result += 1
    return result

def get_shows_with_actor(info : list[SHOW_INFORMATION], is_actor : str) -> list:
    '''
    This function takes a list of differnt show information and the name of an actor.
    It will then return the information of all the shows in which the actor plays
    a role.
    
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera','Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],'Emma Stone')
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],'emmA sTone')
    [('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))]
    >>> get_shows_with_actor([('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera', 'Christopher Mintz-Plasse', 'Bill Hader', 'Seth Rogen', 'Martha MacIsaac', 'Emma Stone', 'Aviva Baumann', 'Joe Lo Truglio', 'Kevin Corrigan'], (2019, 9, 1)), ('Movie', 'The Bad Kids', ['Keith Fulton', 'Louis Pepe'], [], (2017, 4, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux', 'Sally Field', 'Gabriel Byrne', 'Sonoya Mizuno', 'Julia Garner', 'Billy Magnussen', 'Jemima Kirke'], (2018, 9, 21)), ('TV Show', 'The Mind Explained', [], ['Emma Stone'], (2019, 9, 12))],'Ricky Gervais')
    []
    '''
    result_list = []
    for index in range(len(info)):
        is_in = is_actor_in_show(info[index],is_actor)
        if is_in:
            result_list.append(info[index])
    return result_list
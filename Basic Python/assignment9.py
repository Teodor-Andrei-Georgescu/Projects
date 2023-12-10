import doctest

# all 2 digit years assumed to be in the 2000s
START_YEAR = 2000

# represents a Gregorian date as (year, month, day)
#  where year>=START_YEAR, 
#  month is a valid month, 1-12 to represent January-December
#  and day is a valid day of the given month and year
Date = tuple[int, int, int]
YEAR  = 0
MONTH = 1
DAY   = 2


# column numbers of data within input csv file
INPUT_TITLE      = 2
INPUT_CAST       = 4
INPUT_DATE       = 6
INPUT_CATEGORIES = 10

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4


def create_date(date_as_str : str)-> DATE:
    '''
    This is a helper function
    
    
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

def read_file_helper(filename: str) -> list[NetflixShow]:
    '''
    THIS IS A HELPER FUNCTION
    
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file_helper('0lines_data.csv')
    []
    
    >>> read_file_helper('9lines_data.csv')
    [('SunGanges', (2019, 11, 15), ['Naseeruddin Shah'], ['Documentaries', 'International Movies']), ('PK', (2018, 9, 6), ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], ['Comedies', 'Dramas', 'International Movies']), ('Phobia 2', (2018, 9, 5), ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], ['Horror Movies', 'International Movies']), ('Super Monsters Save Halloween', (2018, 10, 5), ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], ['Children & Family Movies']), ('First and Last', (2018, 9, 7), [], ['Docuseries']), ('Out of Thin Air', (2017, 9, 29), [], ['Documentaries', 'International Movies']), ('Shutter', (2018, 9, 5), ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], ['Horror Movies', 'International Movies']), ('Long Shot', (2017, 9, 29), [], ['Documentaries']), ('FIGHTWORLD', (2018, 10, 12), ['Frank Grillo'], ['Docuseries'])]
    '''
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    result_list = []
    desired_info = []
    file = open(filename, 'r', encoding="utf8")
    file.readline()
    line = file.readline()
    while line != '':
        line = line.strip()
        line = line.split(',')
        desired_info.append(line[INPUT_TITLE])
        desired_info.append(create_date(line[INPUT_DATE]))
        if line[INPUT_CAST] != '':
            cast = (line[INPUT_CAST].split(':'))
        else:
            cast = []
        desired_info.append(cast)
        categories = line[INPUT_CATEGORIES].split(':')
        desired_info.append(categories)
        result_list.append(tuple(desired_info))
        desired_info.clear()
        line = file.readline()
    
    file.close()
    return result_list

def read_file(filename: str) -> (dict[str, Date], dict[str, list[str]], dict[str, list[str]]):
    '''
    Populates and returns a tuple with the following 3 dictionaries
    with data from valid filename.
    
    3 dictionaries returned as a tuple:
    - dict[show title: date added to Netflix]
    - dict[show title: list of actor names]
    - dict[category: list of show titles]

    Keys without a corresponding value are not added to the dictionary.
    For example, the show 'First and Last' in the input file has no cast,
    therefore an entry for 'First and Last' is not added 
    to the dictionary dict[show title: list of actor names]
    
    Precondition: filename is csv with data in expected columns 
        and contains a header row with column titles.
        NOTE: csv = comma separated values where commas delineate columns
        Show titles are considered unique.
        
    >>> read_file('0lines_data.csv')
    ({}, {}, {})
    
    >>> read_file('11lines_data.csv')
    ({'SunGanges': (2019, 11, 15), \
'PK': (2018, 9, 6), \
'Phobia 2': (2018, 9, 5), \
'Super Monsters Save Halloween': (2018, 10, 5), \
'First and Last': (2018, 9, 7), \
'Out of Thin Air': (2017, 9, 29), \
'Shutter': (2018, 9, 5), \
'Long Shot': (2017, 9, 29), \
'FIGHTWORLD': (2018, 10, 12), \
"Monty Python's Almost the Truth": (2018, 10, 2), \
'3 Idiots': (2019, 8, 1)}, \
\
{'SunGanges': ['Naseeruddin Shah'], \
'PK': ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], \
'Phobia 2': ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], \
'Super Monsters Save Halloween': ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], \
'Shutter': ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], \
'FIGHTWORLD': ['Frank Grillo'], "Monty Python's Almost the Truth": ['Graham Chapman', 'Eric Idle', 'John Cleese', 'Michael Palin', 'Terry Gilliam', 'Terry Jones'], \
'3 Idiots': ['Aamir Khan', 'Kareena Kapoor', 'Madhavan', 'Sharman Joshi', 'Omi Vaidya', 'Boman Irani', 'Mona Singh', 'Javed Jaffrey']}, \
\
{'Documentaries': ['SunGanges', 'Out of Thin Air', 'Long Shot'], \
'International Movies': ['SunGanges', 'PK', 'Phobia 2', 'Out of Thin Air', 'Shutter', '3 Idiots'], \
'Comedies': ['PK', '3 Idiots'], \
'Dramas': ['PK', '3 Idiots'], 'Horror Movies': ['Phobia 2', 'Shutter'], \
'Children & Family Movies': ['Super Monsters Save Halloween'], \
'Docuseries': ['First and Last', 'FIGHTWORLD', "Monty Python's Almost the Truth"], \
'British TV Shows': ["Monty Python's Almost the Truth"]})
    '''
    # TODO: complete this function according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    dict_title_date = {}
    dict_title_actors = {}
    dict_category_title = {}
    result_list = []
    list_of_info = read_file_helper(filename)
    for index in range(len(list_of_info)):
        dict_title_date[list_of_info[index][0]] = list_of_info[index][1]
        if list_of_info[index][2] != []:
            dict_title_actors[list_of_info[index][0]] = list_of_info[index][2]
        for num in range(len(list_of_info[index][3])):
            if list_of_info[index][3][num] not in dict_category_title:
                dict_category_title[list_of_info[index][3][num]] = [list_of_info[index][0]]
            else:
                dict_category_title[list_of_info[index][3][num]].append(list_of_info[index][0])      
    result_list.append(dict_title_date)
    result_list.append(dict_title_actors)
    result_list.append(dict_category_title)    
    return tuple(result_list)         

def query(filename: str, category: str, date: Date, actors: list[str]) -> list[str]:
    '''
    returns a list of sorted show titles of only shows that:
    - are of the given category
    - have at least one of the actor names in actors in the cast
    - were added to Netflix before the given date
    
    Precondition: category and actor names must match case exactly. 
    For example:
    'Comedies' doesn't match 'comedies', 'Aamir Khan' doesn't match 'aamir khan'
    
    You MUST call read_file and use look ups in the returned dictionaries 
    to help solve this problem in order to receive marks.
    You can and should design additional helper functions to solve this problem.
    
    >>> query('0lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), [])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 9, 5), ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'International Movies', (2019, 8, 1), ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['PK', 'Shutter']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['not found', 'not found either'])
    []
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan', 'not found', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['not found', 'Aamir Khan', 'not found either'])
    ['3 Idiots', 'PK']
    
    >>> query('11lines_data.csv', 'Comedies', (2019, 9, 5), ['not found', 'not found either', 'Aamir Khan'])
    ['3 Idiots', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2019, 9, 5), ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'PK']
    
    >>> query('large_data.csv', 'Comedies', (2020, 9, 5), ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dil Chahta Hai', 'Dil Dhadakne Do', 'PK', 'Zed Plus']
    
    >>> query('large_data.csv', 'International Movies', (2020, 9, 5), ['Aamir Khan', 'Mona Singh', 'Achita Sikamana'])
    ['3 Idiots', 'Andaz Apna Apna', 'Dangal', 'Dhobi Ghat (Mumbai Diaries)', \
'Dil Chahta Hai', 'Dil Dhadakne Do', 'Lagaan', 'Madness in the Desert', 'PK', \
'Raja Hindustani', 'Rang De Basanti', 'Secret Superstar', 'Shutter', \
'Taare Zameen Par', 'Talaash', 'Zed Plus']
    '''
    # TODO: complete this function according to the documentation
    result_list = []
    possible_titles= []
    titles_to_remove = []
    count = 0
    info = read_file(filename)
    genre_titles = list(info[2].items())
    titles_actors = list(info[1].items())
    title_dates = list(info[0].items())
    for index in range(len(genre_titles)):
        if category == genre_titles[index][0]:
            for num in range(len(genre_titles[index][1])):
                possible_titles.append(genre_titles[index][1][num])
    possible_titles.sort()
    if actors != [] and not actors == ['not found', 'not found either']  and not actors == ['not found either', 'not found'] and possible_titles != []:
        for index in range(len(possible_titles)):
            for num in range(len(titles_actors)):
                if possible_titles[index] == titles_actors[num][0]:
                    for actor in range(len(actors)):
                        if actors[actor] not in titles_actors[num][1]:
                            count += 1
                    if count == len(actors):
                        titles_to_remove.append(possible_titles[index])
                    count = 0
    else:
        return result_list
    for index in range(len(possible_titles)):
        for num in range(len(titles_actors)):
            if possible_titles[index] not in titles_actors[num]:
                count +=1 
            if count == len(titles_actors):
                titles_to_remove.append(possible_titles[index])
        count = 0
    for index in range(len(titles_to_remove)):
        possible_titles.remove(titles_to_remove[index])
    
    for index in range(len(possible_titles)):
        for num in range(len(title_dates)):
            if possible_titles[index] == title_dates[num][0]:
                if title_dates[num][1][0] < date[0]:
                    result_list.append(possible_titles[index])
                elif title_dates[num][1][0] == date[0] and title_dates[num][1][1] < date[1]:
                    result_list.append(possible_titles[index])
                elif title_dates[num][1][0] == date[0] and title_dates[num][1][1] == date[1] and title_dates[num][1][2] < date[2]:
                    result_list.append(possible_titles[index])
    return result_list


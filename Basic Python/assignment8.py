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

# represents a Netflix show as (show type, title, directors, cast, date added)
#  where none of the strings are empty strings
NetflixShow = tuple[str, str, list[str], list[str], Date]
TYPE      = 0
TITLE     = 1
DIRECTORS = 2
CAST      = 3
DATE      = 4

# column numbers of data within input csv file
INPUT_TYPE      = 1
INPUT_TITLE     = 2
INPUT_DIRECTORS = 3
INPUT_CAST      = 4
INPUT_DATE      = 6

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

def read_file(filename: str) -> list[NetflixShow]:
    '''
    reads file into list of NetflixShow format.

    Precondition: filename is in csv format with data in expected columns
        and contains a header row with the column titles.
        NOTE: csv = comma separated values where commas delineate columns

    >>> read_file('0lines_data.csv')
    []
    
    >>> read_file('9lines_data.csv')
    [('Movie', 'SunGanges', ['Valli Bindana'], ['Naseeruddin Shah'], (2019, 11, 15)), ('Movie', 'PK', ['Rajkumar Hirani'], ['Aamir Khan', 'Anuskha Sharma', 'Sanjay Dutt', 'Saurabh Shukla', 'Parikshat Sahni', 'Sushant Singh Rajput', 'Boman Irani', 'Rukhsar'], (2018, 9, 6)), ('Movie', 'Phobia 2', ['Banjong Pisanthanakun', 'Paween Purikitpanya', 'Songyos Sugmakanan', 'Parkpoom Wongpoom', 'Visute Poolvoralaks'], ['Jirayu La-ongmanee', 'Charlie Trairat', 'Worrawech Danuwong', 'Marsha Wattanapanich', 'Nicole Theriault', 'Chumphorn Thepphithak', 'Gacha Plienwithi', 'Suteerush Channukool', 'Peeratchai Roompol', 'Nattapong Chartpong'], (2018, 9, 5)), ('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29)), ('Movie', 'Shutter', ['Banjong Pisanthanakun', 'Parkpoom Wongpoom'], ['Ananda Everingham', 'Natthaweeranuch Thongmee', 'Achita Sikamana', 'Unnop Chanpaibool', 'Titikarn Tongprasearth', 'Sivagorn Muttamara', 'Chachchaya Chalemphol', 'Kachormsak Naruepatr'], (2018, 9, 5)), ('Movie', 'Long Shot', ['Jacob LaMendola'], [], (2017, 9, 29)), ('TV Show', 'FIGHTWORLD', ['Padraic McKinley'], ['Frank Grillo'], (2018, 10, 12))]
    '''
    # TODO: complete this method according to the documentation
    # Important: DO NOT delete the header row from the csv file,
    # your function should read the header line and ignore it (do nothing with it)
    # All files we test your function with will have this header row!
    result_list = []
    file = open(filename, 'r', encoding="utf8")
    file.readline()
    line = file.readline()
    while line != '':
        line = line.strip()
        line = line.split(',')
        del(line[0])
        del(line[4])
        del(line[5])
        del(line[5])
        del(line[5])
        del(line[5])
        del(line[5])
        line[DATE]= create_date(line[DATE])
        if line[DIRECTORS] != '':
            line[DIRECTORS] = (line[DIRECTORS].split(':'))
        else:
            line[DIRECTORS] = []
        if line[CAST] != '':
            line[CAST] = (line[CAST].split(':'))
        else:
            line[CAST] = []
        result_list.append(tuple(line))
        line = file.readline()
    
    file.close()
    return result_list

def get_oldest_titles(show_data: list[NetflixShow]) -> list[str]:
    '''
    returns a list of the titles of NetflixShows in show_data
    with the oldest added date

    >>> shows_unique_dates = [('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2018, 10, 5)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> shows_duplicate_oldest_date = [('Movie', 'Super Monsters Save Halloween', [], ['Elyse Maloway', 'Vincent Tong', 'Erin Matthews', 'Andrea Libman', 'Alessandro Juliani', 'Nicole Anthony', 'Diana Kaarina', 'Ian James Corlett', 'Britt McKillip', 'Kathleen Barr'], (2017, 9, 29)), ('TV Show', 'First and Last', [], [], (2018, 9, 7)), ('Movie', 'Out of Thin Air', ['Dylan Howitt'], [], (2017, 9, 29))]

    >>> get_oldest_titles([])
    []
    >>> get_oldest_titles(shows_unique_dates)
    ['Out of Thin Air']
    >>> get_oldest_titles(shows_duplicate_oldest_date)
    ['Super Monsters Save Halloween', 'Out of Thin Air']
    '''
    # TODO: complete this function according to the documentation
    result_list = []
    oldest_index = []
    smallest = 0
    if show_data != []:
        for index in range(1,len(show_data)):
            if show_data[index][DATE][YEAR] < show_data[smallest][DATE][YEAR]:
                smallest = index
            elif show_data[index][DATE][YEAR] == show_data[smallest][DATE][YEAR] and show_data[index][DATE][MONTH] < show_data[smallest][DATE][MONTH]:
                smallest = index
            elif show_data[index][DATE][YEAR] == show_data[smallest][DATE][YEAR] and show_data[index][DATE][MONTH] == show_data[smallest][DATE][MONTH] and show_data[index][DATE][DAY] < show_data[smallest][DATE][DAY]:
                smallest = index
            elif show_data[index][DATE][YEAR] == show_data[smallest][DATE][YEAR] and show_data[index][DATE][MONTH] == show_data[smallest][DATE][MONTH] and show_data[index][DATE][DAY] == show_data[smallest][DATE][DAY]:
                oldest_index.append(index)
        oldest_index.append(smallest)
        oldest_index.sort()
        if oldest_index != []:     
            for length in range(len(oldest_index)):
                index = oldest_index[length]    
                result_list.append(show_data[index][TITLE])
    return result_list
        
def get_actors_in_most_shows(shows: list[NetflixShow]) -> list[str]:
    '''
    returns a list of actor names that are found in the casts of the most shows

    >>> l_unique_casts = [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> one_actor_in_multiple_casts = [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], (2018, 9, 21)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]

    >>> actors_in_multiple_casts = [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'], (2019, 9, 1)), ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], (2018, 9, 21)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], (2019, 12, 31))]

    >>> get_actors_in_most_shows([])
    []

    >>> get_actors_in_most_shows(l_unique_casts)
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers', 'Michael Cera', 'Emma Stone', 'Paresh Rawal']

    >>> get_actors_in_most_shows(one_actor_in_multiple_casts)
    ['Jonah Hill']

    >>> get_actors_in_most_shows(actors_in_multiple_casts)
    ['Om Puri', 'Jonah Hill']
    '''
    # TODO: complete this function according to the documentation
    result_list = []
    actors = {}
    most_seen = []
    biggest = 0
    if shows != []:
        for index in range(len(shows)):
            for num in range(len(shows[index][CAST])):
                actor = shows[index][CAST][num]
                if actor not in actors:
                    actors[actor] = 0
                actors[actor] += 1
        actors_names = []
        actors_appearances= []
        items = actors.items()  
        for index in items:
            actors_names.append(index[0]), actors_appearances.append(index[1])
        for index in range(1,len(actors_appearances)):
            if actors_appearances[index] > actors_appearances[biggest]:
                biggest = index
        most_seen.append(biggest)
        for index in range(len(actors_appearances)):
            if actors_appearances[index] == actors_appearances[biggest] and index not in most_seen:
                most_seen.append(index)
        most_seen.sort()
        for index in range(len(most_seen)):
            spot = most_seen[index]
            result_list.append(actors_names[spot])
    return result_list    



def get_shows_with_search_terms(show_data: list[NetflixShow], terms: list[str]) -> list[NetflixShow]:
    '''
    returns a list of only those NetflixShow elements in show_data
    that contain any of the given terms in the title.
    Matching of terms ignores case ('roAD' is found in 'Road to Sangam') and
    matches on substrings ('Sang' is found in 'Road to Sangam')

    Precondition: the strings in terms are not empty strings

    >>> movies = [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> terms1 = ['House']
    >>> terms1_wrong_case = ['hoUSe']

    >>> terms_subword = ['Sang']

    >>> terms2 = ['House', 'Road', 'Basanti']
    >>> terms2_wrong_case = ['house', 'ROAD', 'bAsanti']

    >>> get_shows_with_search_terms([], [])
    []

    >>> get_shows_with_search_terms(movies, [])
    []

    >>> get_shows_with_search_terms([], terms1)
    []

    >>> get_shows_with_search_terms(movies, terms1)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms1_wrong_case)
    [('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12))]

    >>> get_shows_with_search_terms(movies, terms_subword)
    [('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]

    >>> get_shows_with_search_terms(movies, terms2_wrong_case)
    [('Movie', 'Rang De Basanti', ['Rakeysh Omprakash Mehra'], ['Aamir Khan', 'Siddharth', 'Atul Kulkarni', 'Sharman Joshi', 'Kunal Kapoor', 'Alice Patten', 'Soha Ali Khan', 'Waheeda Rehman', 'Kiron Kher', 'Om Puri', 'Anupam Kher', 'Madhavan'], (2018, 8, 2)), ('Movie', "Viceroy's House", ['Gurinder Chadha'], ['Hugh Bonneville', 'Gillian Anderson', 'Manish Dayal', 'Huma Qureshi', 'Michael Gambon', 'David Hayman', 'Simon Callow', 'Denzil Smith', 'Neeraj Kabi', 'Tanveer Ghani', 'Om Puri', 'Lily Travers'], (2017, 12, 12)), ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri', 'Pavan Malhotra', 'Javed Sheikh', 'Swati Chitnis', 'Masood Akhtar', 'Sudhir Nema', 'Rakesh Srivastava'], (2019, 12, 31))]
    '''
    # TODO: complete this function according to the documentation
    result_list = []
    lower_terms = []
    for index in range(len(terms)):
        lower_terms.append(terms[index].lower())
    lower_terms.sort()
    for index in range(len(lower_terms)):
        for num in range(len(show_data)):
            if lower_terms[index] in show_data[num][TITLE].lower():
                result_list.append(show_data[num])
    
    return result_list
                    
                       


def query(show_data: list[NetflixShow]) -> list[str]:
    '''
    Returns a list of only the show titles from show_data
    that are acted in by the 'most popular' actors
    where the 'most popular' is defined as the actors in the most shows.
    The returned list is in sorted order and does not contain duplicate entries.

    >>> l_unique_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Michael Cera'], (2019, 9, 1)), \
    ('TV Show', 'Maniac', [], ['Emma Stone'], (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], (2019, 12, 31))]
    
    >>> one_actor_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal'], \
    (2019, 12, 31))]
    
    >>> actors_in_multiple_casts = [\
    ('Movie', "Viceroy's House", ['Gurinder Chadha'],\
    ['Hugh Bonneville', 'Om Puri', 'Lily Travers'], (2017, 12, 12)),\
    ('Movie', 'Superbad', ['Greg Mottola'], ['Jonah Hill', 'Michael Cera'],\
    (2019, 9, 1)),\
    ('TV Show', 'Maniac', [], ['Emma Stone', 'Jonah Hill', 'Justin Theroux'], \
    (2018, 9, 21)),\
    ('Movie', 'Road to Sangam', ['Amit Rai'], ['Paresh Rawal', 'Om Puri'], \
    (2019, 12, 31))]
    
    >>> query([])
    []
    
    >>> query(l_unique_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    
    >>> query(one_actor_in_multiple_casts)
    ['Maniac', 'Superbad']

    >>> query(actors_in_multiple_casts)
    ['Maniac', 'Road to Sangam', 'Superbad', "Viceroy's House"]
    '''
    # TODO: complete this function according to the documentation
    result_list = []
    popular_actors = get_actors_in_most_shows(show_data)
    for index in range(len(popular_actors)):
        for num in range(len(show_data)):
            if popular_actors[index] in show_data[num][CAST] and show_data[num][TITLE] not in result_list:
                result_list.append(show_data[num][TITLE])
    result_list.sort()
    return result_list
        
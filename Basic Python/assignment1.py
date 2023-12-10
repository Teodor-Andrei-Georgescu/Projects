PI = 3.14

def print_bear():
    """
    This function prints ascii art of a bear.
    
    Art was taken from:https://www.asciiart.eu/animals/bears
    """
    print(' __         __')
    print('/  \\.-"""-./  \\')
    print('\\    -   -    /')
    print(' |   o   o   |')
    print(' \\  .-\'\'\'-.  /')
    print('  \'-\\__Y__/-\'')
    print('     `---`')

def print_spider():
    """
    This function prints ascii art of a spider.
    
    Art by Max Strandberg
    Taken from:https://www.asciiart.eu/animals/spiders
    """
    print('  / _ \\')
    print('\\_\\(_)/_/')
    print(' _//"\\\\_ ')
    print('  /   \\')

def print_logo():
    """
    This function prints the bear art and spider art two times each.
    The print alternates between both pieces of art with a spacer in between.
    """
    spacer='/~~~~~~~~\\'
    print(spacer)
    print_bear()
    print(spacer)
    print_spider()
    print(spacer)
    print_bear()
    print(spacer)
    print_spider()
    print(spacer)

def calculate_surface_area(height: float, diameter: float):
    """
    Calculates the total surface area of a cylinder given the height and diameter.
    It prints the result to the first decimal place.
    >>> calculate_surface_area(1.2,1.2)
    6.8
    >>> calculate_surface_area(1,10)
    188.4
    """
    cylinder_circumference = PI * diameter
    cylinder_wall_area = cylinder_circumference * height
    # The area of the round wall around the cylinder was just calculated.
    radius = diameter / 2
    circle_area = (PI * radius ** 2) * 2
    # The area of the circle was calculated. 
    # It was multiplied by 2 because there are two circle faces in a cylinder.
    total_surface_area = cylinder_wall_area + circle_area
    print(round(total_surface_area, 1))

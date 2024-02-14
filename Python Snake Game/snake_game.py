import pygame as game
import time
import random

'''
Initalizing the display screen for the game along with other variables
'''
# Initialize the Pygame library
game.init()

#Set the width and height of the game window
screen_width = 720
screen_height = 480

#Define the colors used in the game
green = (0,225,0)
red = (255,0,0)
black = (0,0,0)
white = (255,255,255)
orange =(255,100,10)

#Set the speed and size of the snake
snake_speed = 10
snake_size = 10

#Set the selected difficulty level
difficulty= ''

#Create the Pygame surface object representing the game window
screen = game.display.set_mode((screen_width,screen_height))
game.display.set_caption("Snake game by Teodor Andrei Georgescu")

#Create the Pygame clock object used for controlling the game speed
clock = game.time.Clock()

#Create the Pygame font object used for rendering text
font_style = game.font.SysFont(None, 30)

'''
This function is used to display messages to the users screen
'''
def message(msg,color):
    #Fill the screen with black color
    screen.fill(black)
    g_msg = font_style.render(msg, True, color)

    #Calculate the dimensions of the message surface
    g_msg_width, g_msg_height= g_msg.get_size()

    #Calculate the x and y coordinates to center the message on the screen
    g_msg_x =(screen_width - g_msg_width) // 2
    g_msg_y  =(screen_height - g_msg_height) // 2
    screen.blit(g_msg, [g_msg_x,g_msg_y])

'''
This function updates the user score and displays it on the screen
'''
def your_score(score):
    value = font_style.render("Your Score: " + str(score), True, white)
    #Draw the score surface on the top-left corner of the screen
    screen.blit(value, [0, 0])

'''
This function is used to draw the green snake onto te users screen
'''
def snake(snake_size, snake_list):
    #Loop through the snake list (co-ordinate postion of each block)
    for i in snake_list:
        #Draw a green rectangle at the position of each snake block
        game.draw.rect(screen, green,[i[0],i[1], snake_size, snake_size])

'''
This function randomly generates the apples co-ordinates
'''
def spwan_apple_coordinates():
    applex = round(random.randrange(0, screen_width - snake_size)/10.0)*10.0
    appley = round(random.randrange(0, screen_height - snake_size)/10.0)*10.0
    return applex, appley 

'''
This function spwans the red apple based on its co-ordinates onto the screen
'''
def spwan_apple(applex,appley):
    screen.fill(black)
    game.draw.rect(screen,red,[applex, appley,snake_size,snake_size])

'''
This is a function to hanlde user input and control snakes direction
'''
def user_change_direction(x1_change, y1_change, length_of_snake, direction, event):
    if event.type == game.KEYDOWN:
        if event.key == game.K_LEFT:
            if length_of_snake > 1 and direction != "right":
                x1_change = -snake_size
                y1_change = 0
                direction = "left"
            elif length_of_snake > 1 and direction == "right":
                pass
            else:
                x1_change = -snake_size
                y1_change = 0
        elif event.key == game.K_RIGHT:
            if length_of_snake > 1 and direction != "left":
                x1_change = snake_size
                y1_change = 0
                direction = "right"
            elif length_of_snake > 1 and direction == "left":
                pass
            else:
                x1_change = snake_size
                y1_change = 0
        elif event.key == game.K_UP:
            if length_of_snake > 1 and direction != "down":
                x1_change = 0
                y1_change = -snake_size
                direction = "up"
            elif length_of_snake > 1 and direction == "down":
                pass
            else:
                x1_change = 0
                y1_change = -snake_size
        elif event.key == game.K_DOWN:
            if length_of_snake > 1 and direction != "up":
                x1_change = 0
                y1_change = snake_size
                direction = "down"
            elif length_of_snake > 1 and direction == "up":
                pass
            else:
                x1_change = 0
                y1_change = snake_size
    return x1_change, y1_change,direction

'''
This checks to see if the snake has collided with itself in which case it is game over
'''
def detect_collision_with_snake(x1,y1, snake_head, snake_list, game_over):
    for i in snake_list[:-1]:
        if i == snake_head:
            game_over = True

        #Check if head of snake has hit any part of its own body    
        if x1 == i[0] and y1 == i[1]:
            game_over = True
    return game_over

'''
This function updates the coordinates of the head of the snake

Basically it ads the new postion of the head of the snake making the length of the list increase past the length of the snake.
Then we remove the first index in the list because thats just the tail block which is now wrong because the head of the snake moved.
It helps simulate the snke moving.
'''
def update_snake_postion(x1,y1,x1_change,y1_change, length_of_snake, snake_list):
    x1 += x1_change
    y1 += y1_change
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > length_of_snake:
        del snake_list[0]
    return  x1, y1, snake_list,snake_head

'''
This function is used to check if the snake has colided with the border of the screen in which case it is game over
'''
def collison_with_border(x1,y1, game_over):
    if (x1 > screen_width) or (x1 < 0) or (y1 > screen_height) or (y1 < 0):
        game_over = True  
    return game_over

'''
This is the function that controls all of our game's logic including updating the snakes postion, checking collisions, and constanly updating the screen
'''
def game_loop(snake_speed,difficulty):
    #Setting coniditional statements as need
    game_over = False
    game_closed = False

    #Setting initial x and y co-oridnates
    x1 = screen_width/2
    y1 = screen_height/2
    x1_change = 0
    y1_change = 0

    #Preparing first apple co-ordinates
    applex, appley = spwan_apple_coordinates()

    #Preparing variables that will be used in loop
    length_of_snake = 1
    snake_list = []
    speed_increased_count = 0
    direction = ""

    while not game_closed:

        #After some collision occurs the game is over soo we displau that and re-enter main mennu
        while game_over == True:
            message("Game Over!",red)
            game.display.update()
            time.sleep(2)
            main_menu()

        #Checking if exit button in top right corner is pressed and what directional keys the user is pressing
        for event in game.event.get():
            if event.type == game.QUIT:
                    game_closed = True
            x1_change, y1_change, direction = user_change_direction(x1_change, y1_change, length_of_snake, direction, event)

        #Check collisions with border after user move   
        game_over = collison_with_border(x1,y1,game_over)   

        #Spwan apple
        spwan_apple(applex,appley)
        
        #Calculate snakes updated postion on screen
        x1, y1, snake_list, snake_head = update_snake_postion(x1, y1,x1_change, y1_change,length_of_snake, snake_list)
        
        #If the snake is as long as the screen the user wins then is returned to main menu
        screen_pixels = screen_width * screen_height
        if len(snake_list) == screen_pixels:
            game_closed = True
            message("You Win!", green)
            game.display.update()
            time.sleep(2)
            main_menu()
        
        #Check if snake has collided with itself
        game_over = detect_collision_with_snake(x1,y1,snake_head,snake_list, game_over)

        #Draw snake and update score
        snake(snake_size, snake_list)
        your_score(length_of_snake-1)
        game.display.update()

        #If apple is eaten by snake spwan a new one and increase snake size
        if x1 == applex and y1 == appley:
            applex, appley = spwan_apple_coordinates()
            length_of_snake += 1
            speed_increased_count+=1
        #If in increasing difficulty after ever 5 apples eaten user speed increases
        if (length_of_snake -1) != 0 and (length_of_snake-1) % 5 == 0 and speed_increased_count == 5 and difficulty == "i":
            snake_speed+=3 
            speed_increased_count=0
        clock.tick(snake_speed)

    game.quit()
    quit()

'''
This function just quickly displays onto the screen the controls to play the game
'''
def how_to_play():
    #Prepare message to render
    msg = font_style.render("Use arrow keys control the snake!", True, red)

    #Calulcate message size and coordinates to center the message Then display it
    msg_width, msg_height = msg.get_size()
    msg_x = (screen_width - msg_width) // 2
    msg_y = (screen_height - msg_height) // 2
    screen.fill(black)
    screen.blit(msg, [msg_x, msg_y])
    game.display.update()
    time.sleep(2)

'''
This function generates the difficulty selection screen then starts the game accordingly
'''
def difficulty_selector_screen():
    while True:
        #Preparing the Select difficulty message and its location on the screen
        screen.fill(black)
        title = font_style.render("Select Difficulty", True, white)
        title_width, title_height = title.get_size()
        title_x = (screen_width - title_width) // 2
        screen.blit(title, (title_x, screen_height / 2 - 100))

        #Preparing where each button will be drawn on the screenn
        easy_button = game.draw.rect(screen, green, [screen_width / 2 - 100, screen_height / 2 -40, 200, 50])
        medium_button = game.draw.rect(screen, orange, [screen_width / 2 - 100, screen_height / 2 + 20, 200, 50])
        hard_button = game.draw.rect(screen, red, [screen_width / 2 - 100, screen_height / 2 + 80, 200, 50])
        increasing_button = game.draw.rect(screen, white, [screen_width / 2 - 100, screen_height / 2 + 140, 200, 50])

        #Preparing the text for each button
        easy_text = font_style.render("Easy", True, white)
        medium_text = font_style.render("Medium", True, white)
        hard_text = font_style.render("Hard", True, white)
        increasing_text = font_style.render("Increasing", True, black)

        #Based on each buttons location centering the buttons text
        text_width, text_height =easy_text.get_size()
        screen.blit(easy_text, (easy_button.x + (easy_button.width - text_width) //2, easy_button.y  + (easy_button.height - text_height)//2))
        text_width, text_height =medium_text.get_size()
        screen.blit(medium_text, (medium_button.x + (medium_button.width - text_width) //2, medium_button.y  + (medium_button.height - text_height)//2))
        text_width, text_height =hard_text.get_size()
        screen.blit(hard_text, (hard_button.x + (hard_button.width - text_width) //2, hard_button.y  + (hard_button.height - text_height)//2))
        text_width, text_height =increasing_text.get_size()
        screen.blit(increasing_text, (increasing_button.x + (increasing_button.width - text_width) //2, increasing_button.y  + (increasing_button.height - text_height)//2))

        #Updating display to show buttons
        game.display.update()

        #Checking if any buttons have been pressed
        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                quit()
            if event.type == game.MOUSEBUTTONDOWN:
                x, y = game.mouse.get_pos()
                if x > easy_button.x and x < easy_button.x + easy_button.width and y > easy_button.y and y < easy_button.y + easy_button.height:
                    snake_speed = 10
                    difficulty = "e" 
                    how_to_play()
                    game_loop(snake_speed,difficulty)
                if x > medium_button.x and x < medium_button.x + medium_button.width and y > medium_button.y and y < medium_button.y + medium_button.height:
                    snake_speed = 25
                    difficulty = "m"
                    how_to_play() 
                    game_loop(snake_speed,difficulty)
                if x > hard_button.x and x < hard_button.x + hard_button.width and y > hard_button.y and y < hard_button.y + hard_button.height:
                    snake_speed = 40
                    difficulty = "h"
                    how_to_play()
                    game_loop(snake_speed,difficulty)
                if x > increasing_button.x and x < increasing_button.x + increasing_button.width and y > increasing_button.y and y < increasing_button.y + increasing_button.height:
                    snake_speed = 10
                    difficulty = "i"
                    how_to_play() 
                    game_loop(snake_speed,difficulty)

'''
This function just generates the main menu of the game then goes into the diffculty selector screen
'''
def main_menu():
    while True:
        #Preparing Snak eGame message and where to display it
        screen.fill(black)
        title = font_style.render("Snake Game", True, white)
        title_width, title_height = title.get_size()
        title_x = (screen_width - title_width) // 2
        screen.blit(title, (title_x, screen_height / 2 - 100))

        #Preparing where to display buttons on the screen
        start_button = game.draw.rect(screen, green, [screen_width / 2 - 100, screen_height / 2, 200, 50])
        quit_button = game.draw.rect(screen, red, [screen_width / 2 - 100, screen_height / 2 + 60, 200, 50])
        
        #Preparing the text for each button
        start_text = font_style.render("Start", True, white)
        quit_text = font_style.render("Quit", True, white)

        #Calculating where to display text so it is centered within its button
        text_width, text_height =start_text.get_size()
        screen.blit(start_text, (start_button.x + (start_button.width - text_width) //2, start_button.y  + (start_button.height - text_height)//2))
        text_width, text_height =quit_text.get_size()
        screen.blit(quit_text,(quit_button.x + (quit_button.width - text_width) // 2, quit_button.y + (quit_button.height - text_height) // 2))
        
        #Updating Game display to show buttons
        game.display.update()

        #Checking if any buttns have been pressed
        for event in game.event.get():
            if event.type == game.QUIT:
                game.quit()
                quit()
            if event.type == game.MOUSEBUTTONDOWN:
                x, y = game.mouse.get_pos()
                if x > start_button.x and x < start_button.x + start_button.width and y > start_button.y and y < start_button.y + start_button.height:
                    difficulty_selector_screen()
                if x > quit_button.x and x < quit_button.x + quit_button.width and y > quit_button.y and y < quit_button.y + quit_button.height:
                    game.quit()
                    quit()
main_menu()
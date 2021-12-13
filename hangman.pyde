# ICS3U1-3A
# Darren Chung & Ammar Mahmood
# Final Project - Hangman
# Date of Submission: 2021-06-21
# Last Edit: 2021-06-21

from variables import *
import random

def load_wordFile(wordfile):
    global word_dictionary
    
    word_file = open(wordfile)
    word_dictionary = {}
    text = word_file.readlines()
    gdkey = -1
    
    for line in text:
        line = line.strip()
        row = ""
        for c in line:
            row = row + c
        temprow = row.split( ",")

        gdkey = gdkey + 1
        word_dictionary[ gdkey ] = ( temprow[0],temprow[ 1:4 ], int( temprow[4] ))
    
    word_file.close()

def load_scores():
    global player_history, score_history
    score_file = open("scores.txt", "r")
    player_history = []
    score_history = []
    
    for line in score_file:
        split_line = line.split(",")
        player_history.append(split_line[0])
        score_history.append( int( split_line[1] ) )

    score_file.close()
    return player_history, score_history 
    
def setup():
    global word_dictionary, backChosen
    global screenHeight, screenWidth, game_over, objX, objY, objWidth, objHeight, objYIncr, player_name, player_score, clue_counter, max_clues
    global hangman_info, lava_info, num_mistakes, num_correct, max_mistakes, win_count, mode, charWidth, wait_sec, clueButton, menuWidth, menuHeight
    global play_button, help_button, easy_button, medium_button, hard_button, buttonWidth, buttonHeight, alphabet, clue_button,lava, blank_bg,resetGame,help_screen 
    global display_list, startTextX, textX, textY, box_clicked, numButtons, button_boundaries, activeSquares, menu_bar, game_over, end_screen, start_screen, lava, startChosen
    global clue_counter, clueX, clueY, ClueYstart, clueHeight, player, playerX, playerY, playerHeight, playerWidth, clue_board, removeBoundary, breakPoint
    global startChosen, helpChosen, scoresChosen, resetGame ,settingChosen, menu_barWidth, menu_barHeight, menu_barX , menu_barY, menuItemWidth, numMenuItems, guess_word, guess_wordWidth, enter_nameIMG
    global whichKey, nameLimit, nameCount, nameIn,controlKeys, guess_word, clues, score, score_history, player_history, scoresChosen, prev_mode, score_menubar, new_game_clicked, player_info, lava1
    
    mode = "start screen"
    prev_mode = mode
    
    load_wordFile("words.txt")
    
    #load images
    menu_bar = loadImage("game screen hangman.png")
    help_screen = loadImage("help screen.png")
    end_screen = loadImage("end screen.png")
    start_screen = loadImage("startscreen hangman.png")
    player = loadImage("player.png")
    clue_board = loadImage("cluesboard.png")
    blank_bg = loadImage("blankwhite.png")
    lava1 = loadImage("lava1.png")
    enter_nameIMG = loadImage("entername.png")
    score_menubar = loadImage("scores menubar.png")
    categories_image = loadImage("categories hangman.png")

    # size of canvas / screen
    size (960,720)
    
    player_history, score_history = load_scores()
    
def scoreboard_function():
    global score_history, current_player, player_info, player_score
    
    #noStroke()
    fill(255)
    rect(850,21,105,30)
    fill(0)
    textSize(20)
    text("Score: %i" % player_info[player_score] , 900, 41)

def new_game_func():
    global player_history, score_history, player_info, nameIn, player_name, player_score  
    
    for i in range( len(score_history) ):
        if score_history[i] == 0:
            score_history.pop(i)
            player_history.pop(i)
            break
            
    nameIn = ""
    player_info[player_name] = nameIn
    player_info[player_score] = 0
    write_scores()
    reset()
        
            
def reset():
    global clue_board, gdkey, guess_word, clues, score, display_list, activeSquares, numButtons
    global guess_wordWidth, startTextX, textX, hangman_info, lava_info, playerY, clue_counter, wait_sec, num_mistakes, num_correct, max_mistakes
    
    textSize(100)
    strokeWeight(100)
    textAlign(CENTER)
    
    image( clue_board, 0, 0, 960, 720)

    gdkey = random.randint( 0, len( word_dictionary ) - 1)
    guess_word, clues, score = word_dictionary[ gdkey ]
    display_list = ["_" for char in range(len(guess_word))  ]
    activeSquares = [ True for i in range(numButtons) ]
    
    guess_wordWidth = 44 * len(guess_word)
    startTextX = 480 - guess_wordWidth - 10 // 2
    textX = startTextX
    
    hangman_info = [600, 360, 80, 80, 5 ]
    lava_info = [600, 360, 80, 80, 5 ]
    playerY = 10
    clue_counter = 0
    wait_sec = -1
    num_mistakes = 0
    num_correct = 0
    max_mistakes = 8
    
    
def draw_buttons():
    global numButtons, button_boundaries, alphabet, objX, objY, objWidth, objHeight, box_clicked, clueButton, menuWidth, menuHeight
    
    strokeWeight(5)
    textAlign(CENTER)
    textSize(50)
    
    for i in range(0, clueButton ):
        fill( 255 )
        rect(button_boundaries[i][0][objX], button_boundaries[i][0][objY], buttonWidth, buttonHeight)
        fill( 0,0,0 )
        text(alphabet[i], button_boundaries[i][0][objX] + buttonWidth // 2, button_boundaries[i][0][objY] + buttonHeight - 15)
    
    fill( 255 )
    rect(button_boundaries[clueButton][0][objX], button_boundaries[clueButton][0][objY], buttonWidth, buttonHeight)
    fill(0)
    textSize( 20 )
    text("Clues", button_boundaries[clueButton][0][objX] + buttonWidth // 2 , button_boundaries[clueButton][0][objY] + buttonHeight - 15 ) 
    
    greyout_button()
    
    
def greyout_button():
    global numButtons, button_boundaries, alphabet, objX, objY, objWidth, objHeight, box_clicked, activeSquares, buttonWidth, buttonHeight, clue_counter, clueButton
    
    for i in range(0, clueButton ):
        if activeSquares[i] == False:
            fill(128,128,128)
            rect(button_boundaries[i][0][objX], button_boundaries[i][0][objY], buttonWidth, buttonHeight)
            fill(0)
            text(alphabet[i], button_boundaries[i][0][objX] + buttonWidth // 2, button_boundaries[i][0][objY] + buttonHeight - 15)
        
    if clue_counter == 3:
        fill(128,128,128)
        rect(button_boundaries[clueButton][0][objX], button_boundaries[clueButton][0][objY], buttonWidth, buttonHeight)
        fill(0)
        text("Clues", button_boundaries[clueButton][0][objX] + buttonWidth // 2, button_boundaries[clueButton][0][objY] + buttonHeight - 15)
        
    
def menu_draw_buttons():
    global numButtons, button_boundaries, alphabet, objX, objY, objWidth, objHeight, box_clicked, clueButton, menuWidth, menuHeight
    
    for i in range(clueButton + 1, numButtons):
        fill( 150 )
        rect(button_boundaries[i][0][objX], button_boundaries[i][0][objY], menuWidth, menuHeight)
        
        
def write_scores(): # writes scores into a file to be saved 
    global player_history, score_history, player_info, player_score

    score_file = open("scores.txt", "w")

    for i in range(len(player_history)):  
        add_line = player_history[i] + "," + str( score_history[i] ) + "\n"
        score_file.write(add_line)
    
    score_file.close()
    
        
def giveme_clue():
    global activeSquares, clue_counter, clueX, clueY, ClueYstart, clueHeight, max_clues, clueButton, box_clicked
       
    if box_clicked == clueButton:
        clue_counter += 1
        
    textSize(15)
    if clue_counter < max_clues :
        activeSquares[clueButton] = True
        
    clueY = ClueYstart 
    
    for i in range (clue_counter) :
        fill(0)
        text(clues[i], clueX, clueY)
        clueY += clueHeight
        
        
def wrong_letter():
    global num_mistakes, playerY
    
    #move hangman down closer to lava
    num_mistakes += 1
    playerY += 25
    
def right_letter( guessed ):
    global guess_word, num_correct, display_list
    
    textSize(50)
    for i in range( len( guess_word ) ):
        if guessed == guess_word[i]:
            display_list[i] = guessed    
            num_correct += 1

    
def enter_name():
    global nameIn, whichKey, nameLimit, alphabet, mode, blank_bg, nameCount, enter_nameIMG, mode, score_history, player_history, player_info, player_score
    
    fill(0)
    textSize(20)
    name_len = len(nameIn)
    image(enter_nameIMG,0,0,960,720)
    text( nameIn, 375, 220 )
    if whichKey != "" and name_len != nameLimit and whichKey != "0":
        nameIn += whichKey
        nameCount += 1

    if whichKey == "0":
        while nameIn in player_history: # making sure new name does not match any previous names
            nameIn += "1"
            
        mode = "setup game"
        player_info[player_name] = nameIn
        player_history.append(player_info[player_name])
        score_history.append(player_info[player_score])
        

def score_screen( sortlist, namelist ):
    global nameIn, score_history, player_history, blank_bg, score_menubar, player_info, player_score
    
    length = len(sortlist) - 1
    for i in range ( length ):
        sorted = True
        for j in range ( length - i ):
            if sortlist[j] < sortlist[j + 1]:
                sortlist[j], sortlist[j + 1] = sortlist[j + 1], sortlist[j]
                namelist[j], namelist[j + 1] = namelist[j + 1], namelist[j]
                sorted = False
        if sorted:
            break
         
    fill(244, 126, 27)
    textSize(60)
    image(blank_bg, 0, 0, 960, 720 )
    image(score_menubar, 0, 0, 960, 720)
    text("NAME", 300, 100 )
    text("SCORE", 600, 100)
    
    fill(0)
    textSize(30)
    score_displayY = 150
    for i in range( length + 1 ):
        text(player_history[i], 300, score_displayY)
        text(score_history[i], 600, score_displayY)
        score_displayY += 50
        


                        
def draw():
    global mode, gdkey, word_dictionary, guess_word, clues, score, whichKey, clue_button, startChosen, backChosen, whichKey
    global num_mistakes, max_mistakes, game_over, box_clicked, play_button, help_button, easy_button, medium_button, hard_button, player_info, player_name, player_score
    global display_list, startTextX, textX, text_width, textY, box_clicked, menu_bar, game_over, charWidth, end_screen, start_screen,blank_bg, lava,resetGame
    global hangman_info, lava_info, num_mistakes, num_correct, mode, gdkey, word_dictionary, guess_word, clues, score, display_list, player, playerY, playerX, playerHeight, playerWidth, guess_wordWidth
    global lava1, wait_sec, nameLimit, nameCount, nameIn, alphabet, enter_name, help_screen, scoresChosen, mode, prev_mode 
    
    if box_clicked == startChosen and mode == "start screen" :    
        mode = "enter name"
        
    if box_clicked == resetGame and mode != "start screen" and mode != "enter name":
        new_game_func()
        mode = "enter name"
        
    if box_clicked == scoresChosen and mode != "help screen" and mode != "scores screen" : 
        prev_mode = mode
        mode = "scores screen"
    
    elif box_clicked == helpChosen and mode != "scores screen" and mode!= "help screen" :
        prev_mode = mode
        mode = "help screen"
        
        
    if box_clicked == backChosen:
        if mode == "enter name":
            mode = "start screen"
            nameIn = ""
        elif mode != "enter name":
            image(blank_bg,0,0,960,720)    
            image( clue_board, 0, 0, 960, 720)
            image(menu_bar, 0, 0, 960, 720 )
            giveme_clue()
            if mode == "scores screen":
                mode = prev_mode
            elif mode == "help screen":
                mode = prev_mode
            
    if mode == "start screen":
        image(start_screen, 0, 0, 960, 720 )
    elif mode == "help screen":
        image(help_screen, 0, 0, 960, 720)
    elif mode == "scores screen":
        score_screen( score_history, player_history )
    elif mode == "enter name":
        enter_name()
    
    if mode == "setup game":
        image(blank_bg,0,0,960,720)    
        image( clue_board, 0, 0, 960, 720)
        image(menu_bar, 0, 0, 960, 720 )
        mode = "start game"
        
    if mode == "start game":
        reset()
        mode = "play"
    
    if mode == "end screen":
        image(end_screen, 0, 0, 960, 720)
        
    if mode == "play":
        draw_buttons()
        
        image( player, playerX, playerY, playerWidth, playerHeight )
        image(lava1, 0,0,960,720)
        scoreboard_function()
        textSize(100)
        strokeWeight(100)
        textAlign(CENTER)
        startTextX = 480 - guess_wordWidth // 2
        textX = startTextX 
        for char in display_list:
            textAlign(CENTER)
            text(char, textX, textY)
            textX += charWidth   
    
        if box_clicked != -1 : 
            if box_clicked == clue_button : 
                giveme_clue()
                
            if box_clicked != clue_button: 
                if alphabet[box_clicked] in guess_word :
                    right_letter( alphabet[box_clicked] )
                elif alphabet[box_clicked] not in guess_word and alphabet[box_clicked] != " " :
                    wrong_letter()
                    print("Mistake", num_mistakes, "of 8" )
          
    
        if num_mistakes == max_mistakes:
            player_dead = True
            mode = "end screen"
            game_over = True
            
        if num_correct == len(guess_word):
            current_millisec = millis()
        
            if wait_sec < 0:
                wait_sec = (current_millisec + 3000) # wait 3 seconds before proceeding
                
            if current_millisec > wait_sec:
                player_info[player_score] += score
                current_player = player_history.index(player_info[player_name])
                score_history[current_player] = player_info[player_score]
        
                write_scores()
                reset()
            

    box_clicked = -1
    whichKey = ""

def keyPressed():
    global whichKey, alphabet, controlKeys
    if key == CODED:
       if keyCode in controlKeys:
        whichKey = keyCode
    elif key in alphabet:
        whichKey = key
    else:
        whichKey = ''
        
def mouseReleased():
    global button_boundaries, box_clicked, removeSquare, activeSquares, numButtons, removeBoundary, breakPoint
        
    for i in range( numButtons ):
        if activeSquares[ i ]:
            validXRange = button_boundaries[i][0][objX] <= mouseX <= button_boundaries[i][1][objX] 
            validYRange = button_boundaries[i][0][objY]  <= mouseY <= button_boundaries[i][1][objY]
            validLocation = validXRange and validYRange
            if validLocation:
                box_clicked = i
                removeBoundary = button_boundaries[ box_clicked ][1][0] > breakPoint
                break
            
    if validLocation and removeBoundary:
        activeSquares[ box_clicked ] = False

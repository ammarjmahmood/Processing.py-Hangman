screenHeight = 719
screenWidth = 959
box_clicked = -1
controlKeys = [ ENTER, CONTROL ]

# clues
clue_counter = 0 
max_clues = 3
ClueYstart = 150
clueX = 880
clueY = ClueYstart
clueHeight = 30

# control variables
game_over = False
new_game_clicked = 0
categorieChosen = ""

# index variables
objX = 0
objY = 1
objWidth = 2
objHeight = 3
objYIncr = 4
player_name = 0
player_score = 1

#player
playerX = 695
playerY = 10
playerWidth = 103
playerHeight = 483

# taking in the name input
whichKey = ''
nameIn = ""
nameLimit = 20
nameCount = 0

# data list and game info variables
hangman_info = [ 600, 360, 80, 80, 5 ]
lava_info = [600, 360, 80, 80, 5 ]
player_info = [nameIn, 0]

num_mistakes = 0
num_correct = 0
max_mistakes = 8
win_count = 6
clue_button = 26

# navigation variables for sizes
menu_barWidth = 180
menu_barHeight = 470
menu_barX = 0
menu_barY = 0
menuItemWidth = menu_barWidth
menuItemHeight = menu_barHeight // 5 
numMenuItems = 5

# game screen area dimensions 
playAreaWidth = screenWidth - menu_barWidth
playAreaHeight = screenHeight 

# which button chosen
startChosen = 27
resetGame = 28
scoresChosen = 29
helpChosen = 30
backChosen = 31

# text display
display_list = [ ] 
textY = 700
charWidth = 60
text_width = 75 # coordinate with text size to match

# time variables
wait_sec = -1

# button information
button_boundaries = []
buttonStartX = 230
buttonStartY = 60
buttonXShow = buttonStartX
buttonYShow = buttonStartY
buttonHeight = 75
buttonWidth = 75
alphaButtons = 27
clueButton = 26

menuXShow = 0
menuYShow = 0
menuHeight = 95
menuWidth = 182
menuButtons = 5

numButtons = alphaButtons + menuButtons
activeSquares = [ True for i in range(numButtons) ]
alphabet = "abcdefghijklmnopqrstuvwxyz      012349"
removeBoundary = False
breakPoint = 201

# making button boundaries
for i in range( alphaButtons ): # 27 buttons (26 alphabet letters + 1 clue button)
    if i != 0  and i % 6 == 0:  # 27 / 6 = 4.5; makes 4 and a half rows
        buttonYShow += buttonHeight # changes Y level, new row
        buttonXShow = buttonStartX
    upperLeft =  [ buttonXShow, buttonYShow ]
    lowerRight = [ buttonXShow + buttonWidth, buttonYShow + buttonHeight ]
    clickBoundary = [ upperLeft, lowerRight ]     
    button_boundaries.append( clickBoundary )
    buttonXShow += buttonWidth

for i in range( menuButtons ): # 5 menu buttons
    upperLeft =  [ menuXShow, menuYShow ]
    lowerRight = [ menuXShow + menuWidth, menuYShow + menuHeight ]
    clickBoundary = [ upperLeft, lowerRight ]     
    button_boundaries.append( clickBoundary )
    menuYShow += menuHeight
    
# navigation bar
num_menu_items = 5

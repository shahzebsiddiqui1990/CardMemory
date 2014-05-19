# implementation of card game - Memory

import simplegui
import random

list1 = []
list2 = []
gamelist = []



# helper function to initialize globals
def new_game():    
    global list1, list2, gamelist,exposedcards, state,numturns 
    state = 0
    numturns = 0
    list1 = range(8)              
    list2 = range(8)
    random.shuffle(list1)
    random.shuffle(list2)
    gamelist = list1+list2
    exposedcards = []
    for i in range(16):
        exposedcards.append("False")
    
    #exposedcards[1] = "True"
     
# define event handlers
def mouseclick(pos):
    global exposedcards, state, card1_idx,card2_idx,numturns
    cardindex = pos[0] // 50
    
             
    if state == 0:
        state = 1        
        exposedcards[cardindex] = "True"
        card1_idx = cardindex
    
    elif state == 1:
        # if card not exposed then set card2_idx to index of card
        if exposedcards[cardindex] == "False":
            exposedcards[cardindex] = "True"
            card2_idx = cardindex
            state = 2
    else:
        # if two cards dont match, then flip both cards facedown
        if gamelist[card1_idx] != gamelist[card2_idx]:
            exposedcards[card1_idx], exposedcards[card2_idx] = "False","False"            
        if exposedcards[cardindex] == "False":
            exposedcards[cardindex] = "True"            
            card1_idx = cardindex
            numturns+=1
        
        state = 1    
        
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    count = 1
    x,y = 0,0
    #canvas.draw_polygon([(25,0),(25+50,0),(25+50,0+100),(25,0+100)],2,'Green')
    for idx in exposedcards:
        if idx == "False":
            canvas.draw_polygon([(x,y),(x+50,y),(x+50,y+100),(x,y+100)],2,'Black','Green')
        x += 50
        count+=1
    
    x = 25
    count = 0
    for num in gamelist:
        if exposedcards[count] != "False":
            canvas.draw_text(str(num),[x,50],24,'Red')
        x+= 50
        count+= 1 
    label.set_text("Turns = " + str(numturns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



# Always remember to review the grading rubric

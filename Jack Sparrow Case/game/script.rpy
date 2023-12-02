# include "database.rpy" to use database SQLITE3
# python:
#     current_player = Player("Player1", 0)

include "week1.rpy"
include "week2.rpy"
include "week3.rpy"
include "week4.rpy"
include "week5.rpy"

# Define score variable
default score = 0
default week = 0
# Function to display the score
label display_score:
    "Score: [score]"
    if score == 0:
        "You answered no questions correctly. Better luck next time!"
    elif score>0 and week!=5:
        "You answered [score] questions correctly. Great job!\nEnd of Week [week]"
    else:
        "You answered [score] questions correctly. Great job!\nEnd of Trial\nThank you for playing!"
        "THE END"
    return
        


label start:
    $ week+=1
    call start_week1
    $ week+=1
    call start_week2
    $ week+=1
    call start_week3
    $ week+=1
    call start_week4
    $ week+=1
    call start_week5
    return











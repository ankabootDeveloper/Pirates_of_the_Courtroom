# common.rpy
# Define score variable
default score = 0

# Function to display the score
label display_score:
    "Score: [score]"
    if score == 0:
        "You answered no questions correctly. Better luck next time!"
    else:
        "You answered [score] questions correctly. Great job!"
    "Thank you for playing. The game has ended."
    return
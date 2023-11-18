# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Johnny")
define chew = Character("Mr. Chew")
define judge = Character("Judge Azcarate")
define amber = Character("Amber Heard")
# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene courtroom_1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #show johnny_1 at top

    # These display lines of dialogue.
    """
    Day 1 Trial. Johnny Depp v. Amber Heard
    \nApril 12, 2022
    \nFairfax County, Virginia
    """

    show johnny_1 at top:
        zoom 1.8
    with dissolve
    j  "I'm Johnny Depp, I heard you're a good lawyer who can help me, are you ready for today?"
    menu startGameQ:
        "Yes sir, Mr. Depp":
            j "Thank You "
        "Not yet":
            j "That's unfortunate, the trial is going to start anyways..."
    hide johnny_1

    show chew_1 at top:
        zoom 1.8
    with dissolve
    chew "I am attorny Mr.Chew, representing my client, Johnny Depp, Your Honor"

    hide chew_1

    show judge_1 at top:
        zoom 0.9
    with dissolve
    judge "Thank you Mr.Chew, now, will the defendent please present themselves?"

    hide judge_1
    show amber_1 at top:
        zoom 1.8
    with dissolve
    amber "I am Amber Heard, here my with my attorny, Mr...."
    hide amber_1

    show judge_1 at top:
        zoom 1.8
    with dissolve
    judge"Good morning, ladies and gentlemen. I hope you like the seat that you're in. I'd like you to stay in that seat for the duration of the trial. Thank you for being on time. Are we ready to commence with opening statements?"
    hide judge_1

    show chew_1 at topleft:
    with dissolve
    chew"Good morning. I'm Ben Chew from Brown Rudnick, representing Johnny Depp. Some of you may recognize Mr. Depp from seeing him portray characters such as Edward Scissorhands or Captain Jack Sparrow from the \"Pirates of the Caribbean\" movies."
    chew"For nearly 30 years, Mr. Depp built a reputation as one of the most talented actor in Hollywood, a respected artist whose name was associated with success at the box office."
    




    # This ends the game.

    return

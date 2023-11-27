# The script of the game goes in this file.


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Johnny")
define chew = Character("Mr. Chew")
define judge = Character("Judge Azcarate")
define amber = Character("Amber Heard")
define vasquez = Character("Camille Vasquez")
define rottenborn = Character("Mr.Rottenborn")
define meyers = Character("Ms. Meyers")

default score = 0
# The game starts here.
label start:
    
    # Call the function to get the player's name
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
    Week 3, Day 9, Depp v. Heard
    \nApril 25, 2022
    \nFairfax County, Virginia
    """

    show rottenborn_1 at top:
        zoom 1.8
    with dissolve
    rottenborn "Good morning, everyone. hope you all had a nice weekend. Mr. Depp, as we've talked about this a little bit, you've testified that abuse can come in many forms, correct?"
    hide rottenborn_1

    show johnny_1 at top:
        zoom 1.8
    with dissolve
    j "Yes, indeed."
    hide johnny_1

    show rottenborn_1 at top:
        zoom 1.8
    with dissolve
    rottenborn "Emotional? Verbal? Even psychological abuse?"
    hide rottenborn_1

    show johnny_1 at top:
        zoom 1.8
    with dissolve
    j "Indeed, some of those sort of flew into the other..."
    hide johnny_1

    show rottenborn_1 at top:
        zoom 1.8
    with dissolve
    rottenborn "Now, Ms. Heard wasn't the only one who had a problem with you...\n She wasn't the only one who had a problem with your drinking and abuse of alcohol. Correct?"
    hide rottenborn_1

    show meyers_1 at right:
        zoom 1.8
    with Dissolve(0.2)

    meyers "Objection! "
    label objectionAction:
        $ correct_choice = False
    while not correct_choice:
        menu objection1:
            "Relevance...":
                show judge_1 at topleft
                play sound "audio/gavelsmack.mp3" volume 0.9
                judge "Overruled, does not apply"
                hide judge_1
            "Compound":
                show judge_1 at topleft
                play sound "audio/gavelsmack.mp3" volume 0.9
                $ score += 1
                judge "Sustained, please keep questions singular and direct, please"
                $ correct_choice = True
                hide judge_1
            "Speculation":
                show judge_1 at topleft
                play sound "audio/gavelsmack.mp3" volume 0.9
                judge "Overruled, I don't see how that applies."
                hide judge_1
    hide meyers_1

    show rottenborn_1 at top:
        zoom 1.8
    with dissolve
    rottenborn "My apologies, Your Honor...\n Ms. Heard wasn't the only one who had a problem with your drinking, correct?"
    hide rottenborn_1

    show johnny_1 at top:
        zoom 1.8
    with dissolve
    j "If anyone had a problem with my drinking at any time in my life, it was me. The only person that I've ever abused in my life is myself."
    hide johnny_1

    call display_score
    return
    # This ends the game.

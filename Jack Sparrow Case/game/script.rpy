# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define j = Character("Johnny")
define chew = Character("Mr. Chew")
define judge = Character("Judge Azcarate")
define amber = Character("Amber Heard")
define vasquez = Character("Camille Vasquez")
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
    chew"Today, his name is associated with a lie, a false statement uttered by his former wife, the defendent, Amber Heard, who falsely casted Mr. Depp as a villain, a man who would violently abuse a woman."
    chew"He's suing Mrs. Heard for defamation. Mrs. Heard falsely accused Mr.Depp of abuse in a December 2018 Washington Post op-ed. This trial is about clearing Mr. Depp's name, Heard's allegations are false, and we'll prove it!"
    chew"Her words in the op-ed, particularly three statements, caused significant harm: \"I spoke up against sexual violence and faced our culture's wrath.\""
    chew"\"Two years ago,  I became a public figure reprsenting domestic abuse.\" \nThe evidence shows the timing of the op-ed wasn't coincidental---"
    chew"... it was strategically released on the eve of her movie release. Mrs. Heard's false accusations affected Depp's career and reputation."
    chew"Ms. Heard did not use Mr. Depp's name in the op-ed, but everyone knew...Hollywood knew."
    chew"Two years before the op-ed, on May 27, 2016, Ms. Heard accused Mr. Depp of abuse after he requested a divorce. The evidence will reveal her actions were prompted by his decision to end the relationship. Six days after the divorce request, she filed for a restraining order with a mysterious mark on her face."
    chew"And to tell you more about that, I am going to turn it over to my colleague, Camille Vasquez. Thank you for your attention."

    hide chew_1
    show judge_1 at top:
        zoom 1.8
    with dissolve
    judge"Thank you. Attorney Vasquez, please commence."
    hide judge_1
    show vasquez_1 at topleft:
    with dissolve
    vasquez"Thank you, Your Honor"

    #jump start_week2
    ## week 3 here
    #jump start_week4
    jump start_week5

    # This ends the game.

    return

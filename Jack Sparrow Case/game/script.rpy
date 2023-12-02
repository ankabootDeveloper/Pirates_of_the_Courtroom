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


    default button_pressed = False
    
    screen my_screen():
        textbutton "Press me to show text in french" action [SetVariable('button_pressed', True), Return()] 

    call screen my_screen

    if button_pressed:
        # French Version
            
        show johnny_1 at top:
            zoom 1.8
        with dissolve
        j "Oui en effet."
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

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"In fact, you tried to hide your drinking from your daughter, Lily-Rose, didn't you?"
        hide rottenborn_1

        show meyers_1 at right:
                zoom 1.8
        with Dissolve(0.2)

        meyers "Objection! "
        label objectionAction2:
            $ correct_choice = False
        while not correct_choice:
            menu objection2:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Sustained, please keep questions relevant to the case"
                    $ correct_choice = True
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single question"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, I don't see how that applies."
                    hide judge_1
        hide meyers_1

        show johnny_1 at top:
            zoom 1.8
        j "that is irrelevant and very rude to presume of my daughter's life..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Very well then, let's continue. Can you please pull up exhibit 1092"
        hide rottenborn_1

        show exhibit1092 at top:
        """
        Exhibit 1092
        Male, Depp, laying on chair on resort
        """
        hide exhibit1092

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Mr. Depp, is this a picture of you passed out in the chair during daylight hours?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "I wouldn't say passed out...that's very specific. I would say sleeping is more correct..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Alright then, how about this: This is a picture of you in a chair, correct?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "That is correct..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Thank you. Your Honor, permission to admit Exhibit 1092 into evidence?"
        hide rottenborn_1

        show meyers_1 at right:
                zoom 1.8
        with Dissolve(0.2)

        meyers "Objection! "
        label objectionAction3:
            $ correct_choice = False
        while not correct_choice:
            menu objection3:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Sustained, how is this picture relevant, Mr. Rottenburn?"
                    $ correct_choice = True
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single question direct to me"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, I don't see how that applies."
                    hide judge_1
                "Cumulative":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single item. Not applicable"
                    hide judge_1
        hide meyers_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"W-What? Your Honor, this is unfair. I'm trying to move this along and I am stopped every time with an objection..."
        hide rottenborn_1

        show judge_1 at top:
            zoom 1.8
        judge"Well, do you want to lay a foundation? Otherwise let's continue..."
        hide judge_1
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Fine. Please pull up evidence 587B please."
        hide rottenborn_1

        show evidence_audio at top:
        
        """{size=-10}
        Exhibit 587B Audio:\n
        Amber: If you can keep clean and sober, then it will fix all of our problems...\n
        Johnny: I'm never getting clean and sober!\n
        Amber: I know...\n
        End Recording{/size}
        """
        hide evidence_audio

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Mr. Depp, in that clip, you told Ms. Heard: \"I'm never getting clean and sober.\"Correct?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "To me...it does sound like that...or also it could be \"I have never been clean and sober.\""
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Sure...Let's continue. I will show you a stack of articles about you. What can you tell me about these?"
        hide rottenborn_1
        
        screen dragImages:
            draggroup:
                drag:
                    xpos 0.25
                    ypos 0.25
                    draggable True
                    drag_raise True
                    child "images/article1.png"
                drag:
                    xpos 0.5
                    ypos 0.25
                    draggable True
                    drag_raise True
                    child"images/article2.png"
                drag:
                    xpos 0.75
                    ypos 0.25
                    draggable True
                    drag_raise True
                    child "images/article3.png"
                drag:
                    xpos 0.25
                    ypos 0.5
                    draggable True
                    drag_raise True
                    child "images/article4.png"
        show screen dragImages


        

        show johnny_1 at top:
            zoom 1.8
        j " \"Apparently Drunk\"...\"reportedly\"...These are all publicity stunts. Composed by your client, Ms. Heard."
        hide johnny_1
        hide screen dragImages
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Mr. Depp, please just respond to the questions that I'm asking."
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "What is the question then, Mr. Rottenborn?"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"The article published by Vanity Fair on May 10th 2017 titled \"Johnny Depp's Financial Woes Might Sink the Next \"Pirates of the Caribbean\" Movie\". Did I read that right?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "You did, but I don't know how my financial matters will affect the movie...but if you say so ..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"The next article published on June 21st 2018 by Rolling Stones titled \"The Troubel with Johnny Depp, multimillion-dollar lawsuits, haze of booze and hash, a marriage gone very wrong and a lifestyle he can't afford\". Did I read that right?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j"You did. You should read that article, it's wonderful (Chuckles)"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Noted. Let's continue. In 2016, the statement that then two years ago Ms. Heard became a public figure representing domestic abuse, that is true, isn't it?"
        hide rottenborn_1
        show meyers_1 at right:
                zoom 1.8
        meyers "Objection! "
        label objectionAction4:
            $ correct_choice = False
        while not correct_choice:
            menu objection4:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it ties in with the case?"
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single question"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, I don't see how that applies."
                    hide judge_1
                "Cumulative":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single item. Not applicable"
                    hide judge_1
                "Legal Conclusion":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Sustained, it infers a legal conclusion"
                    $ correct_choice = True
                    hide judge_1
        hide meyers_1
        
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Sorry, let me rephrase. And in 2016, for the first time publicly, Ms. Heard accused youof domestic abuse, correct?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j"That's correct, yes"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Very well. No further questions, Your Honor."
        hide rottenborn_1
        """
        This session's cross examination end.
        \n Direct examination begins. 
        \n Ms. Meyers begins her counsel.
        """
    else:
        #English Version
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
        label objectionAction5:
            $ correct_choice = False
        while not correct_choice:
            menu objection5:
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

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"In fact, you tried to hide your drinking from your daughter, Lily-Rose, didn't you?"
        hide rottenborn_1

        show meyers_1 at right:
                zoom 1.8
        with Dissolve(0.2)

        meyers "Objection! "
        label objectionAction6:
            $ correct_choice = False
        while not correct_choice:
            menu objection6:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Sustained, please keep questions relevant to the case"
                    $ correct_choice = True
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single question"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, I don't see how that applies."
                    hide judge_1
        hide meyers_1

        show johnny_1 at top:
            zoom 1.8
        j "that is irrelevant and very rude to presume of my daughter's life..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Very well then, let's continue. Can you please pull up exhibit 1092"
        hide rottenborn_1

        show exhibit1092 at top:
        """
        Exhibit 1092
        Male, Depp, laying on chair on resort
        """
        hide exhibit1092

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Mr. Depp, is this a picture of you passed out in the chair during daylight hours?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "I wouldn't say passed out...that's very specific. I would say sleeping is more correct..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Alright then, how about this: This is a picture of you in a chair, correct?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "That is correct..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Thank you. Your Honor, permission to admit Exhibit 1092 into evidence?"
        hide rottenborn_1

        show meyers_1 at right:
                zoom 1.8
        with Dissolve(0.2)

        meyers "Objection! "
        label objectionAction7:
            $ correct_choice = False
        while not correct_choice:
            menu objection7:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Sustained, how is this picture relevant, Mr. Rottenburn?"
                    $ correct_choice = True
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single question direct to me"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, I don't see how that applies."
                    hide judge_1
                "Cumulative":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single item. Not applicable"
                    hide judge_1
        hide meyers_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"W-What? Your Honor, this is unfair. I'm trying to move this along and I am stopped every time with an objection..."
        hide rottenborn_1

        show judge_1 at top:
            zoom 1.8
        judge"Well, do you want to lay a foundation? Otherwise let's continue..."
        hide judge_1
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Fine. Please pull up evidence 587B please."
        hide rottenborn_1

        show evidence_audio at top:
        
        """{size=-10}
        Exhibit 587B Audio:\n
        Amber: If you can keep clean and sober, then it will fix all of our problems...\n
        Johnny: I'm never getting clean and sober!\n
        Amber: I know...\n
        End Recording{/size}
        """
        hide evidence_audio

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Mr. Depp, in that clip, you told Ms. Heard: \"I'm never getting clean and sober.\"Correct?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "To me...it does sound like that...or also it could be \"I have never been clean and sober.\""
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Sure...Let's continue. I will show you a stack of articles about you. What can you tell me about these?"
        hide rottenborn_1
        
        screen dragImages:
            draggroup:
                drag:
                    xpos 0.25
                    ypos 0.25
                    draggable True
                    drag_raise True
                    child "images/article1.png"
                drag:
                    xpos 0.5
                    ypos 0.25
                    draggable True
                    drag_raise True
                    child"images/article2.png"
                drag:
                    xpos 0.75
                    ypos 0.25
                    draggable True
                    drag_raise True
                    child "images/article3.png"
                drag:
                    xpos 0.25
                    ypos 0.5
                    draggable True
                    drag_raise True
                    child "images/article4.png"
        show screen dragImages


        

        show johnny_1 at top:
            zoom 1.8
        j " \"Apparently Drunk\"...\"reportedly\"...These are all publicity stunts. Composed by your client, Ms. Heard."
        hide johnny_1
        hide screen dragImages
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Mr. Depp, please just respond to the questions that I'm asking."
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "What is the question then, Mr. Rottenborn?"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"The article published by Vanity Fair on May 10th 2017 titled \"Johnny Depp's Financial Woes Might Sink the Next \"Pirates of the Caribbean\" Movie\". Did I read that right?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "You did, but I don't know how my financial matters will affect the movie...but if you say so ..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"The next article published on June 21st 2018 by Rolling Stones titled \"The Troubel with Johnny Depp, multimillion-dollar lawsuits, haze of booze and hash, a marriage gone very wrong and a lifestyle he can't afford\". Did I read that right?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j"You did. You should read that article, it's wonderful (Chuckles)"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Noted. Let's continue. In 2016, the statement that then two years ago Ms. Heard became a public figure representing domestic abuse, that is true, isn't it?"
        hide rottenborn_1
        show meyers_1 at right:
                zoom 1.8
        meyers "Objection! "
        label objectionAction8:
            $ correct_choice = False
        while not correct_choice:
            menu objection8:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it ties in with the case?"
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single question"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, I don't see how that applies."
                    hide judge_1
                "Cumulative":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Overruled, it was a single item. Not applicable"
                    hide judge_1
                "Legal Conclusion":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Sustained, it infers a legal conclusion"
                    $ correct_choice = True
                    hide judge_1
        hide meyers_1
        
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Sorry, let me rephrase. And in 2016, for the first time publicly, Ms. Heard accused youof domestic abuse, correct?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j"That's correct, yes"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Very well. No further questions, Your Honor."
        hide rottenborn_1
        """
        This session's cross examination end.
        \n Direct examination begins. 
        \n Ms. Meyers begins her counsel.
        """




    call display_score
    return
    # This ends the game.
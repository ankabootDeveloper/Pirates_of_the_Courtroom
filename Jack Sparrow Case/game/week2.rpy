#Week2

# Define characters
define judge = Character("Judge Azcarate", color="#c8ffc8")
define depp = Character("Mr. Depp", color="#ffc8c8")
define meyers = Character("Ms. Meyers", color="#ffc8ff")

label start_week2:
    scene black  # Set background color to black
    
    # Display character images
    show judge happy
    hide depp calm
    hide meyers happy
    
    # Dialogue
    judge "Good morning everyone. You can have your seats, and Mr. Depp, this is a reminder that you are still under oath. Thank you. You can proceed."
    hide judge
    show depp calm
    depp "Thank you, Your Honor."
    
    hide depp
    show meyers happy
    meyers "Good morning, Your Honor, ladies and gentlemen. Yesterday, you already told us a brief history about your relationship with Ms. Heard. When did you notice a change in behavior from Ms. Heard?"
    hide meyers
    show depp calm
    menu:
        "After a few months of our relationship.":
            $ score += 1
            depp "Yes, that's correct. It took some time for her behavior to change."
        "Right from the beginning.":
            depp "No, it took a few months for her behavior to change."
    
    jump continue_script

label continue_script:
    hide depp 
    show meyers happy
    meyers "So, why did you stay, given you were exposed to this kind of behavior from Ms. Heard?"
    hide meyers
    show depp calm
    menu:
        "I was afraid for her safety.":
            $ score += 1
            depp "Yes, that's correct. I lived in constant fear because of her suicidal talk."
        "I enjoyed the arguments.":
            depp "No, it was not about enjoying arguments. It was about my concern for her safety."
    
    jump continue_script_2

label continue_script_2:
    hide depp
    show meyers happy
    meyers "Mr. Depp, do you recall at the beginning of her statement when Ms. Heard stated that you supposedly struck her when she inquired about your tattoo?"
    hide meyers
    show depp calm
    menu:
        "Yes, I recall that incident.":
            depp "No, I don't recall any such incident. It never happened."
        "No, I don't recall that incident.":
            $ score += 1
            depp "That's correct. It never happened."
    
    jump continue_script_3

label continue_script_3:
    hide depp
    show meyers happy
    
    meyers "Are there times when you have experienced any form of abuse from Ms. Heard?"
    hide meyers
    show depp calm
    menu:
        "Yes, there were instances of abuse.":
            $ score += 1
            depp "Yes, that's correct. There were instances of abuse, especially during confrontations."
        "No, there was no abuse.":
            depp "No, that's incorrect. There were instances of abuse."
    
    jump continue_script_4

label continue_script_4:
    hide depp
    show meyers happy
    
    meyers "There was a time when I considered a post-nup agreement. I tried to reason with her, but this escalated and suddenly turned to chaos. She would abuse me, and when I try to lock myself in a room, she would bang the door while screaming obscene words and wanting physical altercations. It was all about confrontations after confrontations."
    
    meyers "I do not have anything else for the day, Your Honor."
    
    # Display the score and end the game
    call display_score
    return


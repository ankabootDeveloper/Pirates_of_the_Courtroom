# Define characters
define judge = Character("Judge Azcarate", color="#c8ffc8")
define meyers = Character("Ms. Meyers", color="#ffc8ff")
define mcgivern = Character("Mr. McGivern", color="#c8c8ff")

# Start of the game for week 4
label start_week4:
    scene black  # Set background color to black
    
    # Display character images
    show judge happy
    hide meyers
    hide mcgivern
    
    # Dialogue
    judge "Good morning, ladies and gentlemen. Alright, you can have your seat. Alright, your next witness."
    hide judge
    show meyers happy
    meyers "Your Honor, we call Travis McGivern."
    hide meyers
    show judge happy
    judge "All right. Mr. McGivern, do you swear or affirm to tell the truth under penalty of law?"
    hide judge
    show mcgivern happy
    mcgivern "Yes, I do."
    hide mcgivern
    show judge happy
    judge "Thank you. Thank you, ma'am. Go on."
    hide judge
    show meyers happy
    meyers "Good morning, Mr. McGivern. Could you please state your full names for the record and explain to us how you know Mr. Depp?"
    hide meyers
    show mcgivern happy
    mcgivern "My full name is Travis Edward McGirven, and I have worked for Mr. Depp as his security for over nine years."
    hide mcgivern
    show meyers happy
    meyers "How can you describe the relationship between Mr. Depp and Ms. Heard?"
    hide meyers
    show mcgivern happy
    mcgivern "Sometimes, they were loving and happy, other times they would argue. However, things started being tense. There were also some incidents where they would fight. Ms. Heard, in different circumstances, I could hear her insulting Mr. Depp, and I would try to get Mr. Depp away from these situations where Ms. Heard would turn violent."
    hide mcgivern
    show meyers happy
    meyers "In your interactions with Ms. Heard and Mr. Depp, have you ever encountered any situation where either of the parties physically abused the other?"
    hide meyers
    show mcgivern happy
    menu:
        "Yes, I have witnessed physical abuse.":
            mcgivern "Yes, that's correct. There were instances of physical abuse, such as the incident where Ms. Heard threw a punch at Mr. Depp."
            $ score += 1
        "No, I have not witnessed physical abuse.":
            mcgivern "No, I have never seen Ms. Heard with any form of injuries. While there were arguments, I did not witness physical abuse."
    hide mcgivern
    show meyers happy
    meyers "Your Honor, that’s all."

    meyers "Your Honor, considering the witness's testimony, I believe it is crucial for us to proceed with the next line of questioning. It could provide valuable insights into the nature of the relationship and the events in question. What is the court's stance on this?"
    hide meyers
    show judge happy
    menu:
        "Allow the attorney to proceed.":
            judge "Very well, you may proceed with the next line of questioning."
            $ score += 1
        "Sustain the objection. Disallow further questioning.":
            judge "Objection sustained. Move on to the next phase of the trial."
    
    # Display the score and end the game


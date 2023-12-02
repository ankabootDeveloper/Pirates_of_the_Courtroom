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

# The game starts here.
label start_week3:

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
        rottenborn "Émotionnel? Verbal? Même des abus psychologiques ?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        with dissolve
        j "En effet, certains d’entre eux se sont en quelque sorte envolés vers d’autres…"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        with dissolve
        rottenborn "Maintenant, Mme Heard n'était pas la seule à avoir un problème avec vous...\n Elle n'était pas la seule à avoir un problème avec votre consommation d'alcool et votre abus d'alcool. Correct?"
        hide rottenborn_1

        show meyers_1 at right:
            zoom 1.8
        with Dissolve(0.2)

        meyers "Objection! "
        label objectionAction:
            $ correct_choice = False
        while not correct_choice:
            menu objection1:
                "Pertinence...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, ne s'applique pas"
                    hide judge_1
                "Composé":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Soutenu, veuillez garder les questions singulières et directes, s'il vous plaît"
                    $ correct_choice = True
                    hide judge_1
                "Spéculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, je ne vois pas comment cela s'applique."
                    hide judge_1
        hide meyers_1

        show rottenborn_1 at top:
            zoom 1.8
        with dissolve
        rottenborn "Mes excuses, Votre Honneur...\n Mme Heard n'était pas la seule à avoir un problème avec votre consommation d'alcool, n'est-ce pas?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        with dissolve
        j "Si quelqu’un a eu un problème avec ma consommation d’alcool à un moment de ma vie, c’est bien moi. La seule personne que j'ai abusée dans ma vie, c'est moi-même."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"En fait, vous avez essayé de cacher votre consommation d'alcool à votre fille, Lily-Rose, n'est-ce pas ?"
        hide rottenborn_1

        show meyers_1 at right:
                zoom 1.8
        with Dissolve(0.2)

        meyers "Objection! "
        label objectionAction2:
            $ correct_choice = False
        while not correct_choice:
            menu objection2:
                "Pertinence...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Soutenu, veuillez garder les questions pertinentes au cas."
                    $ correct_choice = True
                    hide judge_1
                "Composé":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, c'était une seule question"
                    hide judge_1
                "Spéculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, je ne vois pas comment cela s'applique."
                    hide judge_1
        hide meyers_1

        show johnny_1 at top:
            zoom 1.8
        j "c'est hors de propos et très impoli de présumer de la vie de ma fille..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Très bien alors, continuons. Pouvez-vous s'il vous plaît afficher la pièce à conviction 1092"
        hide rottenborn_1

        show exhibit1092 at top:
        """
        Pièce 1092
        Homme, Depp, allongé sur une chaise dans un complexe hôtelier
        """
        hide exhibit1092

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"M. Depp, est-ce une photo de vous évanoui sur une chaise pendant la journée ?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "Je ne dirais pas évanoui... c'est très précis. Je dirais que dormir est plus correct..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Très bien, que diriez-vous de ceci: c'est une photo de vous sur une chaise, n'est-ce pas?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "C'est exact..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Merci. Votre Honneur, permission d'admettre la pièce à conviction 1092 comme preuve ?"
        hide rottenborn_1

        show meyers_1 at right:
                zoom 1.8
        with Dissolve(0.2)

        meyers " Objection!"
        label objectionAction3:
            $ correct_choice = False
        while not correct_choice:
            menu objection3:
                "Pertinence...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Soutenu, en quoi cette image est-elle pertinente, M. Rottenburn ?"
                    $ correct_choice = True
                    hide judge_1
                "Composé":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, c'était une seule question qui m'était adressée directement"
                    hide judge_1
                "Spéculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, je ne vois pas comment cela s'applique."
                    hide judge_1
                "Cumulatif":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, il s’agissait d’un seul élément. N'est pas applicable"
                    hide judge_1
        hide meyers_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"W-Quoi ? Votre Honneur, c'est injuste. J'essaie de faire avancer les choses et je suis arrêté à chaque fois avec une objection..."
        hide rottenborn_1

        show judge_1 at top:
            zoom 1.8
        judge"Eh bien, voulez-vous jeter les bases ? Sinon, continuons..."
        hide judge_1
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Bien. Veuillez récupérer la preuve 587B, s'il vous plaît."
        hide rottenborn_1

        show evidence_audio at top:
        
        """{size=-10}
        Pièce 587B Audio :\n
        Amber : Si vous parvenez à rester propre et sobre, cela résoudra tous nos problèmes...\n
        Johnny : Je ne suis jamais clean et sobre !\n
        Ambre : Je sais...\n
        Terminer l'enregistrement{/size}
        """
        hide evidence_audio

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"M. Depp, dans ce clip, vous avez dit à Mme Heard : Je ne suis jamais clean et sobre.,C'est exact?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "Pour moi... ça ressemble à ça... ou ça pourrait aussi être \"Je n'ai jamais été propre et sobre.\""
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Bien sûr... Continuons. Je vais vous montrer une pile d'articles sur vous. Que pouvez-vous me dire à ce sujet ?"
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
        j " \"apparemment ivre\"...\"aurait\"...Ce sont tous des coups publicitaires. Composé par votre cliente, Mme Heard."
        hide johnny_1
        hide screen dragImages
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"M. Depp, s'il vous plaît, répondez simplement aux questions que je pose."
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "Quelle est alors la question, M. Rottenborn ?"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"L'article publié par Vanity Fair le 10 mai 2017 intitulé « Les malheurs financiers de Johnny Depp pourraient faire couler le prochain film « Pirates des Caraïbes ». Ai-je bien lu ?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j "Vous l'avez fait, mais je ne sais pas comment mes problèmes financiers affecteront le film... mais si vous le dites..."
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Le prochain article publié le 21 juin 2018 par les Rolling Stones s'intitule \"Le Troubel avec Johnny Depp, des procès à plusieurs millions de dollars, une brume d'alcool et de hasch, un mariage qui a très mal tourné et un style de vie qu'il ne peut pas se permettre\". Ai-je bien lu ?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j"Tu l'as fait. Tu devrais lire cet article, c'est merveilleux (rires)"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Noté. Nous allons continuer. En 2016, la déclaration selon laquelle Mme Heard est devenue il y a deux ans une personnalité publique représentant la violence domestique est vraie, n'est-ce pas ?"
        hide rottenborn_1
        show meyers_1 at right:
                zoom 1.8
        meyers "Objection!"
        label objectionAction4:
            $ correct_choice = False
        while not correct_choice:
            menu objection4:
                "Relevance...":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, cela a un lien avec l'affaire ?"
                    hide judge_1
                "Compound":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, c'était une seule question"
                    hide judge_1
                "Speculation":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, je ne vois pas comment cela s'applique."
                    hide judge_1
                "Cumulative":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    judge "Annulé, il s’agissait d’un seul élément. N'est pas applicable"
                    hide judge_1
                "Legal Conclusion":
                    show judge_1 at topleft
                    play sound "audio/gavelsmack.mp3" volume 0.9
                    $ score += 1
                    judge "Soutenu, il en déduit une conclusion juridique"
                    $ correct_choice = True
                    hide judge_1
        hide meyers_1
        
        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Désolé, laissez-moi reformuler. Et en 2016, pour la première fois publiquement, Mme Heard vous a accusé de violence conjugale, n'est-ce pas?"
        hide rottenborn_1

        show johnny_1 at top:
            zoom 1.8
        j"C'est exact, oui"
        hide johnny_1

        show rottenborn_1 at top:
            zoom 1.8
        rottenborn"Très bien. Pas d'autres questions, Votre Honneur."
        hide rottenborn_1
        """
        Fin du contre-interrogatoire de cette session.
        \n  L'examen direct commence.
        \n Mme Meyers commence son conseil.
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

#Week 5
# Define characters
init python:
    def beepy_voice(event, interact=True, **kwargs):
        if not interact:
            return

        if event == "show_done":
            renpy.sound.play("audio/text.mp3", loop = True, channel="sound")

        elif event == "slow_done":
            renpy.sound.stop("sound")  # Correctly refer to the 'sound' channel

define bredehoft = Character("Ms. Bredehoft", callback = beepy_voice)
define depp = Character("Johnny", callback = beepy_voice)
define chew = Character("Mr. Chew", callback = beepy_voice)
define judge = Character("Judge Azcarate", callback = beepy_voice)
define heard = Character("Amber Heard", callback = beepy_voice)
define vasquez = Character("Camille Vasquez", callback = beepy_voice)
define woman = Character("Woman", callback = beepy_voice)

# Placeholder images for characters and shows

image t_chew = "t_chew.jpg"
image t_bredehoft = "t_bredehoft.jpg"
image t_choice = "t_choice.png"
image t_depp = "t_depp.jpg"
image t_heard = "t_heard.jpg"
image t_heardBruise = "t_heardBruise.jpg"
image t_heardCar = "t_heardCar.jpg"
image t_heardConcerned = "t_heardConcerned.jpg"
image t_heardDivorce = "t_heardDivorce.jpg"
image t_heardDivorceSurprise = "t_heardDivorceSurprise.jpg"
image t_heardMetGala = "t_heardMetGala.jpg"
image t_heardshocked = "t_heardshocked.png"
image t_judge = "t_judge.jpg"
image t_magic = "t_magic.jpg"
image t_mirror = "t_mirror.jpg"
image t_roomFloor = "t_roomFloor.jpg"
image t_sheriff = "t_sheriff.jpg"
image t_vasquezNoSmile = "t_vasquezNoSmile.jpg"
image t_phone = "t_phone.jpg"
image t_knifeGift = "t_knifeGift.jpg"
image t_time = "t_time.jpg"
image t_tightrope = "t_tightrope.jpg"

label start_week5:
    play music "audio/UndercoverVampirePoliceman.mp3" loop fadein 2.0
    #stop music fadeout 2.0
    show courtroom_1
    """
    Day 17 Trial. Johnny Depp v. Amber Heard
    \n     May 16, 2022
    \nFairfax County, Virginia
    """
    hide courtroom_1
    show t_judge
    judge "Good morning, ladies and gentlemen, thank you for being so punctual this morning. I appreciate it for the early start."
    judge "Just a reminder, Ms. Heard you're still under oath, okay? All right, next question."
    hide judge
    
    show t_bredehoft
    bredehoft "Thank you, Your Honor. Amber, when did the first act of physical violence by Mr. Depp occur?"
    hide t_bredehoft
    
    show t_vasquezNoSmile
    vasquez "Objection, asked and answered."
    hide t_vasquezNoSmile
    
    show t_judge
    judge "Overruled, go ahead."
    hide t_judge
    
    show t_heard
    heard "It would have been early 2012."
    hide t_heard
    
    show t_bredehoft
    bredehoft "And how did you determine this?"
    hide t_bredehoft
    
    show t_heard
    heard "I reviewed my therapist..."
    hide t_heard
    
    show t_vasquezNoSmile
    vasquez "Objection, hearsay."
    hide t_vasquezNoSmile
    
    show t_bredehoft
    bredehoft "She hasn't even answered it, Your Honor."
    hide t_bredehoft
    
    show t_judge
    judge "All right, I'll allow the answer."
    hide t_judge
    
    show t_heard
    heard "By reviewing my therapist's notes."
    hide t_heard
    
    show t_vasquezNoSmile
    vasquez "Objection, hearsay."
    hide t_vasquezNoSmile
    
    show t_judge
    judge "I'll sustain the objection."
    hide t_judge
    
    show t_bredehoft
    bredehoft "Okay. When did you earlier believe the first act of physical violence occurred?"
    hide t_bredehoft
    
    show t_heard
    heard "Well, I had always believed up until recently that it was...it had started later, that the violence started around early 2013 and early 2012."
    hide t_heard
    
    show t_bredehoft
    bredehoft "Now, you testified earlier that the first act of physical violence by Mr. Depp related to the Winona-Wino tattoo, do you recall that testimony?"
    hide t_bredehoft
    
    show t_heard
    heard "I do."
    hide t_heard
    
    show t_bredehoft
    bredehoft "Okay, does that change your testimony realizing that this is earlier? Was this, in fact, still the first act?"
    hide t_bredehoft
    
    show t_vasquezNoSmile
    vasquez "Objection, leading."
    hide t_vasquezNoSmile
    
    show t_judge
    judge "Sustained."
    hide t_judge
    
    show t_bredehoft
    bredehoft "How do you remember the first act of violence?"
    hide t_bredehoft
    
    show t_heard
    heard " Well, you never forget it. That's how I remember it. It changes your life forever. You never forget the first time someone hits you like that. I just had the date wrong."
    hide t_heard
    
    show t_bredehoft
    bredehoft " Okay. And how is it that you think you got the date wrong?"
    hide t_bredehoft
    
    show t_vasquezNoSmile
    vasquez "Objection, calls for speculation."
    hide t_vasquezNoSmile
    
    show t_judge
    judge "Overruled."
    hide t_judge
    
    show t_heard
    heard "I'm embarrassed to say, I think I would have liked to believe that the period of time in which I had to fall in love with Johnny, in which we fell in love and he was sober and he wasn't violent to me lasted for a lot longer than it did."
    heard "I think I would have liked to have believed that. I wasn't hit so early in the relationship and still stayed."
    hide t_heard
    
    show t_heard
    judge "He was also sober for a period in 2012, which was a peaceful time for us in which we fell in love. So, I had kind of allowed myself, I guess, to forget the beginning of that period, before he got sober, was really violent and chaotic as well. I am embarrassed to say that."
    hide t_heard
    
    show t_bredehoft
    judge " Okay. I'm going to take you to the tape recordings. Why did you and Mr. Depp start taping each other?"
    hide t_bredehoft
    
    show t_heard
    heard "Well, at first, it was...not at first, it was meant to be a way to get to the heart of some of our communication issues, and in order to do...to discover in a therapeutic fashion kind of what was some of our issues in our communication were."
    hide t_heard
    show t_bredehoft
    bredehoft "So, what did Mr. Depp say in your discussions about the use of the term threatening to divorce or threatening to leave each other?"
    hide t_bredehoft
    show t_heard
    heard "Well, Johnny would always say, 'The only way out of this was death.' But in fights, in particularly heated ones, we had found...you know, we were using divorce in the fight, in some of our heated fights."
    heard "We tried not to, but that kind of deteriorated after the December incident that I got beat up pretty badly. And after that point, it was used a lot more often"
    hide t_heard
    show t_bredehoft
    bredehoft "Okay. Now, March 26, 2015, this is after the first Australia trip and after the staircase incident. I'm going to ask, Michelle, can you bring up Depp Exhibit 371A?"
    hide t_bredehoft
    show t_judge
    judge "Plaintiff's 371A then. Any objection?"
    hide t_judge
    show t_vasquezNoSmile
    vasquez "No objection."
    hide t_vasquezNoSmile
    show t_judge
    judge "Okay, 371A in evidence. Thank you."
    hide t_judge
    show t_tightrope
    
    # AUDIO RECORDINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
    heard "I see somebody who's changing into different versions of a person that I recognize for a brief moment, and then he slips away, then he disappears. Then I get different versions of him. I get the insecure or scared version of him that lashes out in a different medium every time."
    heard "So if it's Adderall or Junkie Johnny, then he's abusive and he's a tyrant and he's mean, he's reactionary and he's (inaudible), and anything I do and say is cause for violence or anger."
    heard "If I speak bluntly from the heart, I'm yelling at him. If I argue back with him, then I'm abusive. If I don't say anything, then I'm dismissive or absent or somewhere else. If I engage with him, I'm part of the problem, I'm the one that was mean. "
    heard "If I don't engage with him, then I'm part of the problem. No matter what I do I'm fucked."
    heard "Because if I look at him in the wrong way, it's a problem. If I say the wrong thing no matter what it is, I'm the problem. I'm the problem no matter what. That's the guy who's on a bunch of fucking speed."
    hide t_tightrope
    # AUDIO RECORDINGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG
    show t_bredehoft
    bredehoft "What did you mean when you were saying that to Mr. Depp?"
    hide t_bredehoft
    show t_heard
    heard "That no matter my perception was, no matter what I did, no matter what I did to de-escalate, walk away from him, to confront him, to try to..."
    heard "nothing I did made a difference, nothing I did changed his rage at me, nothing I did changed the violence towards me, nothing I did calmed him down, and I was constantly doing a juggling act of what kind of version of Johnny I was dealing with."
    hide t_heard
    show t_heard
    heard "There were different versions of him and they were drastically different from one another, and even more so than them being different from one another, they didn't even sometimes remember what the other version did or said."
    hide t_heard
    show t_heard
    heard "They acted almost like independent versions of his person, depending on what combination of drugs and alcohol he was on. That's what I was trying to express to him. It's just the futility of me responding successfully and the futility of trying to constantly negotiate with him and the substances he was on at the time."
    hide t_heard
    show t_time
    "May 18, 2022, Continued."
    hide t_time
    show t_judge
    judge "Thank you. All right, be seated. Ms. Vasquez, you may begin your Cross-examination. Next question."
    hide t_judge
    show t_vasquezNoSmile
    vasquez "Good afternoon, Ms. Heard"
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "Mr. Depp hasn't looked at you once this entire trial, has he?"
    hide t_vasquezNoSmile
    show t_depp
    hide t_depp
    show t_heard
    heard "Not that I've noticed, no."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You've looked at him, though, many times, haven't you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, I have."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You know exactly why Mr. Depp won't look back at you, don't you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I do."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "He promised you he would never...you would never see his eyes again. Isn't that true?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I don't recall if he said that."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "One of the last times you ever saw Mr. Depp was when you met him in San Francisco in July of 2016, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That was the second to last time I saw him, yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And this was after you had publicly accused him of domestic violence?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I got my restraining order before that, yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's please play Plaintiff's Exhibit 1229. For the record, it's at 11:01 through 12:09. I'm going to ask that it be admitted into evidence."
    hide t_vasquezNoSmile
    show t_judge
    judge "Any objection to 1229?"
    hide t_judge
    show t_bredehoft
    bredehoft "No objection."
    hide t_bredehoft
    show t_judge
    judge "Okay, 1229 entered in its entirety. Go ahead and play your section."
    hide t_judge
    # AUDIO RECOOOOOOOOOOOOOOOOOOORDING
    show t_phone
    heard "Is this how you want it to end? I don't understand, is this what you want?"
    depp "No. Oh no, a hug will save it all. All this, everything you just did to me."
    heard "Please, babe. I don't know. I just wanted to touch you. Seriously, it's..."
    depp "Really, after all the shit you just said?"
    heard "Yes, I just wanted to give you a hug, I just.."
    depp "After all the shit you fucking accused me of, you wanna touch me?"
    heard "Yes, yes, please, please hug me"
    depp "You're fucking nuts"
    heard "Please, I just wanted to hug you and say bye. I didn't want it to end bad."
    depp "Oh, there is no chance of that. We did that last night, it was fine. That was good enough."
    heard "I don't know what else to say."
    depp "No, 'cause I'm nothing to you, and I will always be nothing to you."
    heard "Please, please, calm. Calm down, baby, please."
    depp "What? You're not my shrink."
    heard "Please. Please, put your hand on my heart. Please just feel my heart, please."
    depp "No."
    heard "Please, I need to know if we'll ever see each other again, please."
    depp "No, we'll never see each other again. We will never...don't take my fucking glasses off. You don't like fucking looking at not my fucking eyes? You will not see my eyes again."
    hide t_phone
    # AUDIO RECOOOOOOOOOOOOOOOOOOORDING
    show t_vasquezNoSmile
    vasquez "This is from when you and Mr. Depp met in San Francisco in July of 2016, right? After you had publicly accused him of domestic abuse?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, and got my TRO."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And he tells you, 'You will not see my eyes again.' And he has kept that promise, hasn't he?"
    hide t_vasquezNoSmile
    show t_heard
    heard "As far as I know, he cannot look at me."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "He won't look at you, right, Ms. Heard."
    hide t_vasquezNoSmile
    show t_heard
    heard "He can't."
    hide t_heard
    show t_choice
    menu:
        "(Evidence) Show the court the recording of Ms. Heard mocking Mr. Depp's claims of being abused":
            $ score += 1
        "(Evidence) Mr. Depp's text messages indicating his 2016 travel plans":
            chew "Remember, we need to focus on the core of our argument. The text messages about travel plans, while interesting, don't directly challenge the narrative we're contesting."
    hide t_choice
    show t_vasquezNoSmile
    vasquez "Let's please play Plaintiff's Exhibit 357A, which is already in evidence, Your Honor. And for the record, it's 21:22 through 21:40."
    hide t_vasquezNoSmile
    # AUDIO RECOOOOOOOOOOOOOOOOOOORDING
    show t_phone
    heard "And see what the jury and judge thinks. Tell the world, Johnny. Tell them, Johnny Depp, 'I, Johnny Depp, a man, I'm a victim too of female domestic violence and, you know, it's a fair fight,' and see how many people believe or side with you."
    hide t_phone
    # AUDIO RECOOOOOOOOOOOOOOOOOOORDING
    show t_vasquezNoSmile
    vasquez "That's your voice on that recording, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, it is."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you said to Mr. Depp, 'You can please tell people that it was a fair fight and see what the jury and the judge think. Tell the world, Johnny, tell them, 'Johnny Depp, I, Johnny Depp, a man, a victim too of domestic violence.' That's what you said, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I was saying it to the man who beat me up, yes. I thought it was preposterous."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And the man you beat up numerous times, right, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I could never hurt Johnny."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You didn't think he would tell the world he was a victim of domestic violence, did you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I found it hard to believe that he could or that he would do that considering the relationship he and I had. I thought it would be crazy for him to do so knowing what I know we lived through."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Or, as you said to him in that recording, who was going to believe that Johnny Depp, a man, is a victim of domestic violence, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "With all due respect, I wasn't saying it because he's a man, I was saying it because he was a man who beat me up for five years."
    hide t_heard
    show t_choice
    menu:
        "Keep pushing":
            $ score += 1
        "Ease up the pressure":
            chew "We've got her feet to the fire! We have to take advantage of this opportunity. Keep pushing!"
    hide t_choice
    show t_vasquezNoSmile
    vasquez "Mr. Depp is your victim, isn't he?"
    hide t_vasquezNoSmile
    show t_heard
    heard "No, ma'am."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And once he left you, you continue to abuse him publicly by calling him an abuser, didn't you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "He is an abuser and you can look either of us up online and figure out who's being abused."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's look at some of that. Mr. Depp wears rings on every finger, doesn't he, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's my experience, yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Every one of his fingers is adorned, your words, 'Big, chunky rings.' Isn't that right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's my experience of him."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you've never known him not to wear these rings?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's my experience is he normally wore rings, yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So, Mr. Depp was wearing these big chunky rings on every finger in every incident of abuse you've described to this jury, right?"
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "heard you testified to an incident in March of 2013 where Mr. Depp hit you in the face multiple times. And you testified, 'You don't know how many times he hit you in the face.'"
    hide t_vasquezNoSmile
    show t_heard
    heard "I can't say for certain it was in every single incident, though in general, my experience with Mr. Depp is that he wears rings almost all the time."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you testified, 'You don't know how many times he hit you in the face.' So, Mr. Depp hit you in the face multiple times while he was wearing rings on this occasion, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Which occasion in March are you referencing?"
    hide t_heard
    show t_vasquezNoSmile
    vasquez "The testimony that you gave on day 15 of this trial, March of 2013, you weren't specific as to the day."
    hide t_vasquezNoSmile
    show t_heard
    heard "There were several incidents."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "The one where he hit you several times in the face. March of 2013."
    hide t_vasquezNoSmile
    show t_heard
    heard "Right. What are you asking me? I'm sorry."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "He was wearing rings on that occasion?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I pretty much always knew him to wear rings."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay, let's please pull up Defendant's Exhibit 170A, which is already in evidence, Your Honor."
    hide t_vasquezNoSmile
    show t_heardBruise
    vasquez "You testified this is a picture you took after that incident, right?"
    hide t_heardBruise
    show t_heard
    heard "Yes, that was one where he grabbed me."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And hit you in the face so many times that you don't remember. And there's no injuries to your face in this picture, are there?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Not that this picture shows."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And there's no medical records reflecting that you sought treatment after this alleged incident either."
    hide t_vasquezNoSmile
    show t_heard
    heard "I did not need to go to the doctor at the time."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Despite hitting you several times that you lost count with rings on his fingers?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct, I did not seek medical attention, other than my therapist."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You testified to another incident in March of 2013 where Mr. Depp hit you while he was wearing a lot of rings, and you testified you felt like your lip went through your teeth and it got a little blood on the wall?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, I remember that."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You didn't produce any photographs after that alleged incident, did you, Ms. Heard"
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "You didn't show any pictures to this jury after describing that alleged incident that your teeth...your lip went into your teeth. You don't remember that, right? You didn't show any pictures to this jury after describing that incident, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I don't believe I've seen that picture admitted."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "That picture doesn't exist. The only picture that you've produced and shown to this jury is the one that was just put up on the screen, where you said he hit you multiple times in the face and you appear to have what is a bruise on your arm."
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "You testified about an incident in Russia on or about June 26th, 2013. Do you remember that?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I do."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You testified that Mr. Depp, 'whacked you in the face.'"
    hide t_vasquezNoSmile
    show t_heard
    heard "I did."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And then according to your testimony, when you came out of the bathroom, Jerry Judge, Mr. Depp's security guard who has passed away, pointed out that your nose was bleeding. And you said you hadn't known that your nose is bleeding until Jerry Judge pointed it out to you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, that's correct. I was unaware until he brought it up to me. I didn't see it when I was in the bathroom but I wasn't looking."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So, it's your testimony that you went into the bathroom and didn't look in the mirror, which I assume was in the bathroom, to notice that your nose is bleeding?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's not why I went into the bathroom. I went into the bathroom crying, I don't even know if I paid attention to the mirror. I certainly didn't enough to notice any blood."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you didn't take any pictures of your bloody nose either, but pictures were taken of you in Russia, though. Isn't that correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, that's correct. We had a press...or a dinner."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's please pull up Plaintiff's Exhibit 1248."
    hide t_vasquezNoSmile
    show t_heardCar:
        zoom 0.9
    vasquez "Ms. Heard, this is a picture of you in Russia after the incident, correct?"
    hide t_heardCar
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you have no visible injuries to your face, do you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "None that you can see."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Even though Mr. Depp whacked you in the face so hard that your nose bled, while wearing chunky big rings, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You also testify that Mr. Depp, again, whacked you in the face after the Met Gala in May of 2014. You testify that you thought he hit you so hard he broke your nose."
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You said your nose was, 'Swollen, discolored, red.' You testified you took a picture of your face after this, but you didn't show that picture to the jury, did you?"
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "You understand you're under an obligation to produce all photographs after any alleged incidents of violence, right, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I produced everything."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You also understand that you're under an obligation to produce all medical records reflecting any injuries you allegedly sustained from Mr. Depp, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you haven't produced any pictures or any medical records reflecting a broken nose after the Met Gala in May of 2014, have you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I have given everything to my lawyers, everything, I've turned over literally everything that I have."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You also attended an event a day after the Met Gala in May of 2014. And there were pictures taken of you at this event, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's pull please pull up Plaintiff's Exhibit 1252."
    hide t_vasquezNoSmile
    show t_heardMetGala:
        zoom 0.9
    vasquez "This is a picture of you, Ms. Heard At that event? The night after the Met Gala? The night after Mr. Depp allegedly broke your nose?"
    hide t_heardMetGala
    show t_heard
    heard "Yes, it is. I'm not sure if it was broken for the record, but you should see what it looked like underneath the makeup."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "I think this...if Your Honor is fine, this is a good stopping point."
    hide t_vasquezNoSmile
    show t_judge
    judge "Okay, that's fine. All right, ladies and gentlemen, we'll stop here for the evening. Remember, tonight, do not do any outside research, do not discuss the case with anybody. I know these days are a little longer and I appreciate your patience and you're taking care of everything here." 
    judge "Please take care of yourself tonight, okay? And we'll see you in the morning at 9AM"
    hide t_judge
    show courtroom_1 
    "Day 18 Trial: 'Johnny Depp v. Amber Heard' \n
    May 17, 2022 \n
    Fairfax County, Virginia"
    hide courtroom_1
    show t_judge
    judge "Please be seated."
    hide t_judge
    show t_judge
    judge "Please be seated. Ms. Vasquez, next question."
    hide t_judge
    show t_vasquezNoSmile
    vasquez "Thank you, Your Honor, and good morning, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "Good morning."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Your relationship with Mr. Depp began in October of 2011, and you have testified multiple times under oath that your first year with Mr. Depp was 'the best of times,' correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes, that is correct."
    hide t_heard
    show t_magic:
        zoom 0.9
    vasquez "You also testified that Mr. Depp, as far as you could tell, was sober that first year. You called that time in your life 'magical.'"
    hide t_magic
    show t_heard
    heard "That is what I used to believe."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "But now, you've told this jury that Mr. Depp was being violent with you throughout 2012, the very same time period, haven't you, Ms. Heard?"
    hide t_vasquezNoSmile
    show t_heard
    heard "No. He was hitting me in 2012, but he took a break in the middle of the year when he was sober."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You told them that he was hitting you in 2012 though. Is that right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "He was hitting me in 2012. He just took a break in the middle."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Contradicting what you have said previously, you now claim that Mr. Depp was in and out of sobriety during this time, and that 'cycles of violence' followed from Mr. Depp's alcohol consumption..."
    hide t_vasquezNoSmile
    show t_choice
    menu:
        "(Evidence) Knife gifted to Mr. Depp from Ms. Heard during these 'cycles of violence'":
            $ score += 1
        "(Evidence) 2012 photo of Mr. Depp and Ms. Heard smiling together":
            chew "I don't know if that photo will prove anything, Ms. Vasquez. Show the jury the knife!"
    hide t_choice
    show t_knifeGift
    vasquez "So, it was during these 'cycles of violence' that you decided to gift Mr. Depp a knife? Master Deputy Sheriff Palusa, please show the jury."
    hide t_knifeGift
    show t_sheriff:
        zoom 0.7
    vasquez "This is the knife that you gave the man that you claim would get drunk and violent with you, is that right, Ms. Heard?"
    hide t_sheriff
    show t_heardConcerned: 
        zoom 0.9
    heard "..."
    hide t_heardConcerned 
    show t_heardConcerned
    heard "At the time, I did not believe that he was going to stab me with it, that is for sure."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "But you gave it to him while he was abusing you? Allegedly."
    hide t_vasquezNoSmile
    show t_heard
    heard "I gave it to him that year."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Now, Ms. Heard I'm going to need to talk to you about what happened in Australia in March of 2015. You've testified that at some point during the incident you described, you witnessed Mr. Depp bashing the phone against a wall, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You testified that the phone was breaking into pieces?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I was watching it disappear."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And according to your testimony, this was a wall-mounted phone in the bar area?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's take a look at defendant's exhibit 1820. I believe this has already been admitted into evidence. If we could have it published. Thank you. You saw this photo during your direct examination, right?"
    hide t_vasquezNoSmile
    show t_roomFloor
    vasquez "You saw this photo during your direct examination, right?"
    hide t_roomFloor
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you testified that the wall-mounted phone that you saw Mr. Depp smash is on the wall on the left?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "But it's not depicted in this photo, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Whoever took this photo was standing right in front of where that mounted phone was."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "That's convenient. The pieces of the phone Mr. Depp smashed aren't in this picture either, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "You don't see it because it's...whoever took this photo is standing in front of that."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Mr. King took this photo. Mr. King testified under oath in this trial, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And he testified that there was no wall-mounted phone smashed to smithereens that he had to replace, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I didn't hear him testify to that. No."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "He did. The counsel listed it.  According to you, this is when Mr. Depp lost the tip of his finger, right? When he was smashing the phone?"
    hide t_vasquezNoSmile
    show t_heard
    heard "It is my best guess. I didn't notice his finger come off. Obviously, I was watching him smash the phone and watching the pieces break while he was doing it."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. So you testified in this courtroom that after Mr. Depp smashed the phone, he held you down on the countertop by the neck. Do you remember that?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I'm not quite sure of the exact sequence of things, but yes, both of those things happened."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. We'll get to the sequence. And this is when Mr. Depp supposedly assaulted you with a bottle, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "On the countertop, he assaulted me."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So Mr. Depp was able to get you on the counter, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "He held me down by my neck."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And he grabbed a bottle according to you by holding you down by the neck, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "As I have always said, I don't remember exactly what happened first, or I don't remember the sequence, I just remember being aware that I was being assaulted by a bottle while I was on the countertop."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So he penetrates you with this bottle? But you don't know how he got the bottle, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. And he did that right after he lost the tip of his right middle finger? We'll get to the sequence. And while he was on 8 to 10 MDMA pills, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Again, I don't remember the exact sequence of those events."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "We'll get to the sequence. And while he was on 8 to 10 MDMA pills, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's talk about the sequence. This is the sequence of events you testified to in this courtroom, that he smashed the phone to smithereens and then assaulted you, lost a tip of his finger, and then assaulted you with a bottle. Yes? That's the sequence of events that you testified to in this courtroom."
    hide t_vasquezNoSmile
    show t_heard
    heard "To be clear, you're putting it in order when you say words like then. I have never claimed that I can remember the exact sequence of these things. This was a multi-day assault that took place over three horrible days.  It was the worst thing that ever happened to me."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. Let's focus on the testimony that you gave about the injuries. Mr. Depp, as you testified yesterday, wears rings on every finger, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Sometimes. I mean, often. And certainly, in the later part of our relationship, that was more normal than not, but if he's filming or something like that, of course, he's not gonna have his own jewelry on."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. And he was wearing rings on every finger in Australia, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Not all the time. Not literally every single ring every single day. But he often wore his rings."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Not often, Ms. Heard Your words are, 'I've never known Johnny not to wear rings on every finger.'"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is what I testified to."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. And you testified that you bled as a result of this sexual assault? That your forearms were cut, along with your feet, and that you had a bruise across your jaw?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And there is not a single medical record reflecting treatment for any of those injuries. Is there, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I did not seek treatment for my injuries."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And when you were in Australia, Ms. Hard you didn't take any pictures of the injuries you claimed to have sustained. Right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I did not take any pictures. No"
    hide t_heard
    show t_vasquezNoSmile
    vasquez "But you did take two pictures of the bathroom mirrors. Let's please pull up defendant's exhibit 374, which is already in evidence."
    hide t_vasquezNoSmile
    show t_mirror
    vasquez "You took this picture, right, Ms. Heard"
    hide t_mirror
    show t_heard
    heard "Yes. That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And this black paint on the mirror is from Mr. Depp?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "He wrote on the mirror in black paint after his finger was cut off, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes. I only know that because there was blood as well as paint."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And you took this picture after you had allegedly been assaulted by Mr. Depp? Yes?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Yet you didn't capture yourself in the mirror, did you? Is that because you didn't have any visible injuries on you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "It's because I was taking a picture of the writing"
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Let's talk about the writing on this mirror. So the writing in black paint is for Mr. Depp, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "It's all from Mr. Depp."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And it's your testimony under oath that you did not write the red text that says 'call Carly Simon, she said it better, babe?'"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Because if you did write that, it means that your husband was walking around the house bleeding from his amputated finger and you're writing snarky messages to him on a mirror. Right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I don't know what your question to me is. I'm sorry."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. So you would agree, Ms. Heard, that the black text on the mirror says 'she loves naked photos of herself, so modern, so hot'?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I had not read that yet. I mean, before. But yeah, that's what it says."
    hide t_heard  
    show t_choice
    menu:
        "Leave it":
            chew "Press her on this Ms. Vasquez!"
        "How could she not have read that? She took a picture of it.":
            $ score += 1
    hide t_choice
    show t_vasquezNoSmile
    vasquez "But you were taking pictures of the text, but you had not read that before?"
    hide t_vasquezNoSmile
    show t_heard
    heard "It didn't make sense to me at the time when I read it in person."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. Again, Mr. Depp wrote that?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I don't know who else would've."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So, Ms. Heard, just to be clear, it's your testimony that Mr. Depp also wrote the message in red about Carly Simon saying it better, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You know Carly Simon singing the song, 'You're So Vain,' right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I was told that."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So it's your testimony that Mr. Depp was writing messages to himself in the mirror back and forth?"
    hide t_vasquezNoSmile
    show t_heard
    heard "The best I can describe it is it looked like a crazy conversation. It was on the walls, it was on lampshades..."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "It's your testimony the crazy conversation was with himself?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's what it looked like."
    hide t_heard
    show t_mirror
    vasquez "And you would agree with me that in this photograph, the red text has been smudged with black paint, right?"
    hide t_mirror
    show t_heard
    heard "That's what it looked like."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So Mr. Depp must have not liked his own message to himself?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I'm not sure."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. Let's please pull up plaintiff's exhibit 343, which is already in evidence, and play the portion from 157:21 through 158:54. It's a recording, Your Honor."
    hide t_vasquezNoSmile
    # AUDIO RECOOOOOOOOOOOOOOOOOOORDING
    show t_phone
    depp "It's not to get you mad. It's not to get...it's just to get out of a bad situation while it's happening before it gets worse. In Australia, when we had the big fight where I lost the tip of my finger, at least five bathrooms and two bedrooms I went to..."
    heard "To avoid talking to me?"
    depp "To escape. To escape the fight"
    heard "You don't escape the fight, you escape the solution. You escape the solution."
    depp "No."
    heard "You escape figuring it out. We cannot work it out if you run away to the bathroom every time."
    depp "Listen to me. Listen to me. A boxer can't go 12 rounds without a fucking minute break."
    heard "I'm not giving you a minute break, you do it at minute three at the beginning of an argument"
    depp "No. There are rounds, man. And when it gets too fucking hairy, the ref splits 'em apart or whatever. But all I'm saying is, you can't have a solution if the argument just keeps mounting, and mounting, and mounting, and mounting."
    depp "I fucking go into the bathroom and sit on the floor, bam, bam, bam, here you come. I come out, fight, fight, fight, crazy, escalated. I split again, I go to another fucking bathroom or a bedroom or something. Knock, knock, knock, bang, bang, bang. You kept coming to get me."
    hide t_phone
    # AUDIO RECOOOOOOOOOOOOOOOOOOORDING
    show t_vasquezNoSmile
    vasquez "This is what really happened in Australia, isn't it, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I did knock on a bathroom door on the first night."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Not a bathroom door, five bathroom doors, and two bedrooms. Isn't that right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Johnny is not an accurate historian of what happened during that..."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "heard that's not my question. Five bathroom doors, two bedrooms. That's what you knocked on. That's what actually happened in Australia. Isn't it, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I remember it. I knocked on one bathroom door. I came on the first night after he decided to take the bag of MDMA and I went."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "The recording we just listened to, that's exactly what happened in Australia. Mr. Depp lost the tip of his finger after you threw a bottle at him. Isn't that right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is incorrect."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Okay. You're the one who assaulted someone with a bottle in Australia. Isn't that right, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I didn't assault Johnny in Australia. I didn't assault Johnny ever. I couldn't."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And then after he was injured, he had to hide from you, right?  In five bathrooms, two bedrooms. And you would pursue him. Because he was avoiding talking to you. Right? You weren't scared of him at all, were you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I have a mixed relationship with Johnny, one in which I'm scared and one in which I love him very much"
    hide t_heard
    show t_vasquezNoSmile
    vasquez "I'm not talking about your mixed relationship. That night in Australia after you cut off his finger with a bottle, you weren't scared of him at all, were you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "This is a man who tried to kill me. Of course, it's scary. He's also my husband."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "March 8th is the day that you were allegedly sexually assaulted by Mr. Depp in Australia, correct?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And Mr. Depp's finger had just been cut off, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You sent a text message to your therapist that night, 'I feel so lost. I can't talk. I don't know if I'll ever be able to change.' Did I read that correctly?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That is correct."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You weren't able to change, were you, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I very much wanted to leave the relationship I was in, but I didn't have the power. I didn't feel I had the power to leave. I knew I was in a very toxic relationship with Johnny, and I knew I needed to change that. I knew it was, at this point, horrible for me. And I talked to my therapist often about that."
    hide t_heard
    show t_time:
        zoom 0.9
    "May 19, 2022, Continued."
    hide t_time
    show t_vasquezNoSmile
    vasquez "If we could please pull up plaintiff's exhibit 1280, which is a clip from your divorce deposition."
    hide t_vasquezNoSmile
    show t_heardDivorce:
        zoom 0.9
    woman "heard did you send a text message to Jerry Judge on May 24th, 2016, telling Jerry Judge 'I'm desperately trying to reach Johnny. It's extremely important. Please tell him?'"
    heard "I remember sending the text message that is in front of me right now to Jerry."
    heard "And I would like...I remember sending this because I wanted to tell Johnny or have him told by Jerry or someone who knew him or was close to him. Basically, I didn't want him to find out online that I had or was about to file, or I had already filed for divorce."
    heard "I wanted him to know verbally. So I was trying to reach him through a third party to tell him."
    heard "When I say reach, I'm specifically saying I would like him to know information coming from me or coming from Jerry from me so that he finds out about the divorce filing or my intention to do so from some other source other than TMZ, which was alerted."
    hide t_heardDivorce
    show t_heardDivorceSurprise:
        zoom 0.9
    heard "!!!"
    hide t_heardDivorceSurprise
    show t_vasquezNoSmile
    vasquez "You slipped up there, didn't you, Ms. Heard You let it slip out that TMZ had been alerted to your filing of the domestic violence restraining order, didn't you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I disagree. That's not what I'm talking about."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "TMZ is the same outlet that you released the video of Mr. Depp attacking the kitchen cabinets the day before this deposition was taken, wasn't it?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I didn't do that. I don't know how to do that."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "TMZ owns the copyright to that video now, doesn't it?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I have no idea what TMZ owns"
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Did they pay you for that?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I never got paid for it because I had nothing to do with that."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So TMZ was just lucky in getting the inside scoop to your divorce from Mr. Depp, huh?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I have no idea. It is not...that's not my area of expertise. I wouldn't even know how to do that. And also, what does that get me? If I wanted to leak things about Johnny, I could have done that in a much more successful way, in a bigger way. For years."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Not when you were extorting him for $7 million."
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "Tasya van Ree is your ex-wife, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "That's right. She's my ex-partner."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "She's the one that you told this jury Mr. Depp was jealous of, right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yeah. Well, that was a 2013 fight, around March. Yes."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You committed domestic violence against Ms. van Ree during your relationship, didn't you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "No, I did not."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "You assaulted her at a Seattle airport in 2009, didn't you?"
    hide t_vasquezNoSmile
    show t_heard
    heard "No, I did not."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And people saw that."
    hide t_vasquezNoSmile
    show t_heard
    heard "That's not true."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "And it was covered in the press. Isn't that true?"
    hide t_vasquezNoSmile
    show t_heard
    heard "It was planted in the press by Johnny's team two days after I got the TRO. Not coincidentally."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "Can you please pull up plaintiff's exhibit 1279?"
    hide t_vasquezNoSmile
    show t_vasquezNoSmile
    vasquez "If we could please have that article displayed for the witness? This is an article from two years ago, correct, Ms. Heard"
    hide t_vasquezNoSmile
    show t_heard
    heard "I don't know when this article was published."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "May of 2020. The title reads, 'Amber Heard allegedly grabbed, struck her ex-girlfriend at the airport,' doesn't it?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes. And that's not true."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "'Amber Heard allegedly struck her ex-girlfriend, Tasya van Ree, at the airport in 2009.' Did I read that right?"
    hide t_vasquezNoSmile
    show t_heard
    heard "Yes. This is another example of the smear campaign."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "So Mr. Depp is not the only domestic partner you've assaulted, is he, Ms. Heard?"
    hide t_vasquezNoSmile
    show t_heard
    heard "I've never assaulted Mr. Depp or anyone else that I've been romantically linked to ever."
    hide t_heard
    show t_vasquezNoSmile
    vasquez "No further questions, Your Honor."
    hide t_vasquezNoSmile
    show t_judge
    judge "Alright, this is a good place to stop. Thank you everyone, and stay safe out there."
    hide t_judge
    show t_time:
        zoom 0.9
    "To be continued..."
    call display_score
    

    label end:
        return 
    # THE END
    
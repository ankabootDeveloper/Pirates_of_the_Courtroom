#Week 1
#Week 1 Characters
define j = Character("Judge Azcarate",color="#c8ffc8")# Judge Azcarate (Judge)
define bc = Character("Mr. Chew",color="#1aabea")# Ben Chew (Mr.)
define cv = Character("Ms. Vasquez",color="#1aabea")# Camille Vasquez (Ms.)
define sm = Character("Mr. Moniz",color="#1aabea")# Sam Moniz (Mr.)
define br = Character("Mr. Rottenborn",color="#cd432e")# Ben Rottenborn (Ms.)
define eb = Character("Ms. Bredehoft",color="#cd432e")# Elaine Bredehoft (Ms.)
define cd = Character("Ms. Dembrowski",color="#c8ffc8")# Christi Dembrowski (Ms.)
define rl = Character("Ms. Lecaroz",color="#1aabea")# Rebecca Lecaroz (Ms.)
define ib= Character("Mr. Barauch",color="#c8ffc8")# Isaac Barauch (Mr.)
define kj = Character("Ms. James",color="#c8ffc8")# Katherine James (Ms.)
define la = Character("Dr. Anderson",color="#c8ffc8")# Laurel Anderson (Dr.)
define gd = Character("Ms. Deuters",color="#c8ffc8")# Gina Deuters (Ms.)
define ak = Character("Dr. Kipper",color="#c8ffc8")# David Alan Kipper (Dr.)

label start_week1:
    scene courtroom full:
        zoom 0.73

    """
    Day 1 Trial. Johnny Depp v. Amber Heard
    \nApril 12, 2022
    \nFairfax County, Virginia
    """
    scene depp:
        zoom 0.73  
    ""
    scene heard:
        zoom 0.73
    ""
    scene judge:
        zoom 0.73 
    j "Good morning, ladies and gentleman."
    j "I hope you like the seat that you're in. I'd like you to stay in that seat for the duration."
    j "I'd appreciate it. Thank you, and thank you for being punctual today."
    j "Are we ready with opening statements?"
    scene chew:
        zoom 0.73 
    bc "Yes, Your Honor."
    scene judge:
        zoom 0.73 
    j "All right. Go ahead, sir."
    scene judge:
        zoom 0.73
    scene chew:
        zoom 0.73 
    bc "Good morning. I'm Ben Chew from Brown Rudnick, representing Johnny Depp"
    scene pirate:
        zoom 0.73 
    bc "Some of you may recognize Mr. Depp from seeing him portray characters such as Edward Scissorhands or Captain Jack Sparrow from the \"Pirates of the Caribbean\"movies."
    bc "For nearly 30 years, Mr. Depp built a reputation as one of the most talented actors in Hollywood, a respected artist whose name was associated with success at the box office."
    scene chew:
        zoom 0.73 
    bc "Today, his name is associated with a lie, a statement uttered by his former wife, the defendant, Amber Heard, that cast Mr. Depp as a villain, a man who would violently abuse a woman. He's suing Amber Heard for defamation."
    bc "Heard falsely accused Depp of abuse in a December 2018 Washington Post op-ed. This is about clearing Depp's name. Heard's allegations are false, and we'll prove it."
    scene newspaper:
        zoom 0.73 
    bc "Her words in the op-ed, particularly three statements, caused significant harm:"
    bc "\"I spoke up against sexual violence and faced our culture's wrath.\""
    bc "\"Two years ago, I became a public figure representing domestic abuse.\""
    bc "\"I had the rare vantage point of seeing, in real time, how institutions protect men accused of abuse.\""
    bc "The evidence will show the timing of the op-ed wasn't coincidental. It was strategically released on the eve of her movie release. Heard's false accusations affected Depp's career and reputation."
    scene heard bruise:
        zoom 0.73 
    bc "Ms. Heard didn't use Depp's name in the op-ed, but everyone in Hollywood knew. Two years before the op-ed, on May 27, 2016, Heard accused Depp of abuse after he requested a divorce. The evidence will reveal her actions were prompted by his decision to end the relationship."
    bc "Six days after the divorce request, she filed for a restraining order with a mysterious mark on her face."
    scene  chew:
        zoom 0.73 
    bc "No one had ever, in five decades, accused Johnny Depp of being violent. No one had ever accused Mr. Depp of being violent with a woman. He had been in other long-term relationships. He even has children."
    bc "Ultimately, this trial is about clearing Mr. Depp's name of a terrible and false allegation. "
    bc "We ask you, in the next several weeks, to please, please, carefully consider the evidence, assess the reliability and credibility of that evidence, and to make your own determination about what actually happened between Mr. Depp and Ms. Heard."
    bc "To tell you more about that, I am going to turn it over to my colleague, Camille Vasquez. Thank you all for your attention."
    scene judge:
        zoom 0.73 
    j "Ms. Vasquez."
    scene vasquez:
        zoom 0.73 
    cv "Good morning, everyone. Over this trial, you'll learn about Johnny Depp, the man, not just the actor. His friends, family, and colleagues will attest that he's a kind soul who never raised a hand to a woman."
    cv "Growing up in an abusive environment, he learned to cope by leaving, a pattern he continued in his relationship with Amber Heard."
    scene cat fight:
        zoom 0.73 
    cv "Amber pursued Johnny, and they had a tumultuous relationship. She berated and sometimes became physically violent. Johnny tried to escape the conflicts, but leaving only fueled her anger. Witnesses, including security personnel, will testify to these scenes."
    cv "Medical professionals saw no signs of injuries Amber later claimed."
    scene grave:
        zoom 0.73 
    cv "In 2016, Johnny decided to end the relationship after his mother's death. On May 21, 2016, gathering his belongings, Amber created a false domestic abuse scene."
    cv "But why would she lie?"
    cv "The evidence will reveal that she fabricated more incidents when faced with the seriousness of her claims."
    scene vasquez:
        zoom 0.73
    cv "You'll hear about Amber's changing narrative, from a quiet victim to a public figure in the MeToo movement. The evidence will show that her allegations are false, inconsistent with injuries, and based on manipulated photos. Not a single photograph captures Johnny being violent."
    cv "This trial is about what Amber said in her op-ed, portraying herself as a survivor and Johnny as an abuser. The evidence will expose her lies and reveal her motive: to raise her profile and career."
    cv "At the end of this trial, we will ask you to render a verdict for Mr. Depp. We will ask you to tell the world that he is not the abuser she described and that she is not the victim she portrayed."
    cv "We will ask you to tell Ms. Heard that what she did was wrong."
    cv "Thank you very much."
    scene courtroom full:
        zoom 0.73
    j "Let's take a 15-minute break. Remember, no discussions or outside research."
    scene time skip:
        zoom 0.75
    "Flashback to Febuary 25, 2022\nJohnny Depp's Lawyers Discuss an Important Issue"
    scene lawyer meeting:
        zoom 0.73
    bc "Good morning, everyone. I think it's essential to discuss whether we should have cameras in the courtroom during this trial. Camille, what are your thoughts on this matter?"
    scene paparazzi:
        zoom 0.73
    cv "Well, Mr. Chew, having cameras in the courtroom could be advantageous for Mr. Depp's case. It allows the public to see the evidence firsthand, fostering transparency and potentially garnering public support. Moreover, it puts the power of public opinion in our favor, which could influence the jury."
    scene protest:
        zoom 0.73
    sm "On the flip side, though, there's the risk of sensationalism and misinterpretation. We've seen how media can sometimes twist stories. We need to weigh the benefits of public support against the potential pitfalls of sensationalized coverage."
    scene cross paths:
        zoom 0.73
    cv "Absolutely, Mr. Moniz. Utilizing cameras strategically, focusing on the truth and countering false narratives, could be a powerful strategy. It's a chance to present the real Johnny Depp, a man who, as we'll demonstrate, has never raised a hand to a woman."
    show brain:
        zoom 0.73
    cv "What shall be the final decision?"
    menu:
        "Request cameras in the courtroom": # gain points
            jump day1_pt2
            $ score +=1

        "Reject cameras in the courtroom":
            jump wrong1

    label wrong1:
        scene gamble:
            zoom 0.73
        bc "It is too risky, we need to have those cameras out of the courtroom. It could backfire."
        cv "Public perception matters, especially in high-profile cases. If we can sway the public opinion, it may indirectly influence the jury, making them more receptive to the evidence presented."
        scene lawyer meeting:
            zoom 0.73
        bc "Ms. Vasquez, you sure do have a point. Forget what I said."

    label day1_pt2:
        scene court cameras:
            zoom 0.73
        bc "We are going to have those cameras in the courtroom."
        bc "Johnny Depp is a superstar and the public opinion shall be in his favor."
        scene time skip:
            zoom 0.75
        "Back to Day 1\nApril 13, 2022"
        scene courtroom full:
            zoom 0.73
        "Break is over..."
        scene judge:
            zoom 0.73
        j "All right. Opening statements. Mr. Rottenborn."
        scene rottenborn:
            zoom 0.73
        br "Good morning. I'm Ben Rottenborn, representing Amber Heard. In a few minutes, Elaine will address the allegations. We'll focus on the evidence, not distractions or conspiracy theories."
        br "The central question is whether Amber's words in a 2018 op-ed were protected free speech. The article is about proposed legislation, not Johnny Depp. It doesn't mention him or detail abuse."
        br "We'll examine the context. The article is Amber's advocacy for change in laws protecting abuse victims. Depp's team wants you to forget this context."
        scene newspaper:
            zoom 0.73
        br "Now, let's look at the individual statements."
        br "\"Two years ago, I became a public figure representing domestic abuse.\"This is true. Amber obtained a restraining order after suffering abuse."
        br "\"I had the rare vantage point of seeing how institutions protect men accused of abuse. Also true. Depp was protected despite her accusations.\""
        br "The third statement's headline isn't defamatory, and it speaks to her real experiences. She faced wrath for speaking out against abuse."
        br "Depp didn't sue The Washington Post, focusing solely on Amber in Virginia to ruin her life. He chose this path, and we won't let false statements go unresponded."
        scene drugs:
            zoom 0.73
        br "Regarding damages, Depp's career and reputation suffered due to his choices and addictions, not the op-ed. Witnesses in his case are financially tied to him."
        scene rottenborn:
            zoom 0.73
        br "Depp's poor choices led to this courtroom. He blames others instead of taking responsibility. Op-ed damages are baseless, as evidence shows issues with Disney predate it."
        br "It's time for Depp to take responsibility. Your unique position empowers you to stand for the First Amendment, truth, and Amber's right to speak."
        br "Thank you."
        scene judge:
            zoom 0.73
        j "Thank you, Mr. Rottenborn. Ms. Bredehoft."
        scene bredehoft:
            zoom 0.73
        eb "Good morning, everyone. Thank you for being here. We'll be relying on evidence, not hyperbole."
        eb "Ms. Heard's photos are legitimate and authenticated; an IT expert will confirm. She produced devices, all identical. We'll present a video from 2016 and significant audio tapes."
        eb "Amber, a 35 year old girl from Austin, TX. She faced abuse and poverty in her past. She worked multiple jobs, struggled in Hollywood until she was noticed by an agent."
        scene love drugs:
            zoom 0.73
        eb "She met Depp in 2009 during the filming of \"The Rum Diary.\"Their relationship started after respective breakups. Depp's rage, fueled by drugs and alcohol, led to verbal, emotional, physical, and sexual abuse."
        scene phone locked:
            zoom 0.73
        eb "Amber tried to fix things, attending therapy and Al-Anon meetings. Depp's handlers often took care of him after incidents."
        eb "In 2011, Amber revealed abuse to her therapist. Her 2015 trip to Australia and an incident in December 2015 were violent."
        eb "Depp used drugs. Photos and texts document the abuse. Despite challenges, Amber initially chose to stay, trying to protect Depp's image."
        scene bloody australia:
            zoom 0.73
        eb "In the three days in Australia, some pretty horrendous things happened to her. He rips off her nightgown. He has her jammed up against a bar. He has hurled bottles and bottles at her. He has dragged her across the floor on the broken bottles and the liquor."
        eb "He has punched her. He has kicked her. He tells her he's going to f****g kill her."
        scene money:
            zoom 0.73
        eb "Amber experienced a series of abusive incidents by Johnny Depp, including physical assaults and a sexual assault. The culmination of these events led to a domestic violence restraining order."
        eb"The divorce was challenging, with Amber refusing a financial settlement and opting to donate the money to charity."
        scene bredehoft:
            zoom 0.73
        eb "Johnny's retaliation involved defamatory statements, damaging Amber's emotional well-being and reputation, affecting her career opportunities. The counterclaim against Depp's lawyer, Adam Waldman, focuses on false statements accusing Amber of orchestrating a hoax."
        eb "The evidence will demonstrate the emotional and reputational harm inflicted on Amber."
        eb "Enough is enough."
        eb "We're also going to ask you to hold him responsible and try to fully and fairly compensate Amber for what he has done to her."
        eb "Thank you very much."
        scene judge:
            zoom 0.73
        j "Thank you, Ms. Bredehoft. We will break for lunch early!."
        scene courtroom empty:
            zoom 0.73
        "Break..."
        scene courtroom full:
            zoom 0.73
        "Break is over..."
        scene judge:
            zoom 0.73
        j "All right. Your first witness."
        scene chew:
            zoom 0.73
        bc "Good afternoon, Ms. Dembrowski. Would you please state your full name for the record?"
        scene dembrowski:
            zoom 0.73
        cd "Elisa Christine Dembrowski."
        scene chew:
            zoom 0.73
        bc "Ms. Dembrowski, what relationship, if any, do you have with Johnny Depp?"
        scene dembrowski:
            zoom 0.73
        cd "I am his sister."
        scene chew:
            zoom 0.73
        bc "Christi, how was your life growing up and the events leading to your mother's death."
        scene dembrowski:
            zoom 0.73
        cd "Well, it was a challenging upbringing, especially after our father left. The day he left, I remember it vividly."
        scene depp:
            zoom 0.73
        ""
        scene chew:
            zoom 0.73
        bc "And your father left your family because of a significant argument, correct?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, he mentioned it was the last argument he felt they could ever have. It was intense, and he decided it was time to leave."
        scene approach:
            zoom 0.73
        br "Objection, hearsay."
        scene judge:
            zoom 0.73
        j "Sustained. Please proceed, Mr. Chew."
        scene chew:
            zoom 0.73
        bc "Moving forward, Christi, did your mother recover after taking the pills?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, she did, but she continued to struggle with her mental health."
        scene chew:
            zoom 0.73
        bc "Now, let's touch upon Johnny's departure from your mother's house. Can you tell us about that?"
        scene dembrowski:
            zoom 0.73
        cd "…"
        scene approach:
            zoom 0.73
        br "Objection, foundation."
        scene judge:
            zoom 0.73
        j "Sustained. Please lay the foundation, Mr. Chew."
        scene chew:
            zoom 0.73
        bc "Were you in communication with Johnny at that time?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, he came to live with me for a part of that time."
        scene chew:
            zoom 0.73
        bc "So, what did Johnny do after leaving your mother's house?"
        scene dembrowski:
            zoom 0.73
        cd "He lived in different places, including with me and another family."
        scene chew:
            zoom 0.73
        bc "Did you and Johnny continue to communicate with your mother after leaving the home?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, we did."
        scene chew:
            zoom 0.73
        bc "Christi, why did you and Johnny continue to communicate with your mother?"
        scene dembrowski:
            zoom 0.73
        cd "Simply because she was our mom, and we loved her. Despite the challenges, we understood she did her best with the tools she had from her past."
        scene chew:
            zoom 0.73
        bc "And when you say \"we\", you're referring to Johnny and yourself?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, Johnny and I."
        scene chew:
            zoom 0.73
        bc "Did you ever work for your Mr. Depp?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, I took on the role of Johnny's personal manager. I handled various aspects, including travel arrangements and hotel bookings."
        scene chew:
            zoom 0.73
        bc "Can you elaborate on Johnny's connection with Jerry Judge during this time?"
        scene dembrowski:
            zoom 0.73
        cd "Jerry Judge was Johnny's longtime security personnel. They had a professional relationship, and Jerry played a crucial role in ensuring Johnny's safety."
        scene chew:
            zoom 0.73
        bc "What were the interactions like between Johnny and his former wife, Vanessa Paradise?"
        scene dembrowski:
            zoom 0.73
        cd "It was a lovely marriage. There were no signs of abuse during their relationship. It was amicable, and they co-parented their children."
        scene chew:
            zoom 0.73
        bc "Now, let's talk about the early stages of Amber Heard and Johnny's relationship. What role did you play?"
        scene dembrowski:
            zoom 0.73
        cd "I arranged their travel and hotel bookings. Johnny requested an extra room, not because of any anticipated altercations, but as a pattern from their childhood. They often argued, and Johnny needed a space to get away."
        scene chew:
            zoom 0.73
        bc "Did you witness any altercations between Johnny and Amber?"
        scene dembrowski:
            zoom 0.73
        cd "No, I never saw or heard any altercation between them."
        scene brain:
            zoom 0.73
        bc "(Internal Thoughts)\nIt is time to ask the heavy hitters."
        "Should I ask about Amber having any bruises?\nI may risk getting an objection.\nIf the question makes it through, I should be able to somewhat incite the idea that Amber was never bruised up by Johnny."
        menu:
            "Ask about Amber Heard's bruises": # gain points
                $ score +=1
                jump day1_pt3

            "Best to be quiet":
                jump wrong2

    label wrong2:
        bc "Nah, I am not going to ask."
        bc "Actually, what do I have to lose? Sometimes I guy needs to think with with his gut."

    label day1_pt3:
        scene chew:
            zoom 0.73
        bc "What about marks on Amber? Did you notice any?"
        scene heard:
            zoom 0.73
        ""
        scene dembrowski:
            zoom 0.73
        cd "No, I did not see any marks on Amber."
        scene chew:
            zoom 0.73
        bc "Can you describe Johnny and Amber's wedding and what happened afterward?"
        scene dembrowski:
            zoom 0.73
        cd "The wedding was beautiful, but the relationship faced challenges. Amber told us about her fight with Johnny in Australia during a dinner in 2016."
        scene chew:
            zoom 0.73
        bc "How did the family cope with the passing away of your mother less than a year after?"
        scene dembrowski:
            zoom 0.73
        cd "It was a difficult period. The premiere of \"Alice in Wonderland\"and a music tour were scheduled right after her death, adding to the family's shock."
        scene chew:
            zoom 0.73
        bc "Did Amber's op-ed contribute to Johnny's career challenges?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, it was dangerous for his career. The false allegations affected his reputation."
        scene chew:
            zoom 0.73
        bc "Thank you, Your Honor. That's all I have right now."
        scene judge:
            zoom 0.73
        j "All right. Cross examination"
        scene examine:
            zoom 0.73
        ""
        scene rottenborn:
            zoom 0.73
        br "Good afternoon, Ms. Dembrowski."
        scene dembrowski:
            zoom 0.73
        cd "Good afternoon."
        scene rottenborn:
            zoom 0.73
        br "You do realize that your income is directly tied to your brother's career, right?"
        scene dembrowski:
            zoom 0.73
        cd "Well, historically, it hasn't always been solely tied to Johnny's earnings."
        scene rottenborn:
            zoom 0.73
        br "But for the most part, the success of Infinitum Nihil is linked to your brother's projects, correct?"
        scene dembrowski:
            zoom 0.73
        cd "I wouldn't simplify it that way. We've had deals with other entities and companies."
        scene rottenborn:
            zoom 0.73
        br "However, it's fair to say that the better your brother does in his career, the more successful Infinitum Nihil becomes?"
        scene dembrowski:
            zoom 0.73
        cd "It's not as straightforward as that, no."
        scene rottenborn:
            zoom 0.73
        br "You mentioned that you're an employee of Infinitum Nihil. Do you work for any of Johnny's other companies?"
        scene dembrowski:
            zoom 0.73
        cd "No, I'm solely employed by Infinitum Nihil."
        scene rottenborn:
            zoom 0.73
        br "Your paycheck comes from Infinitum Nihil, correct?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, that's correct."
        scene rottenborn:
            zoom 0.73
        br "So, you do have a financial interest in how well Infinitum Nihil performs financially?"
        scene dembrowski:
            zoom 0.73
        cd "I receive a salary, but I wouldn't consider that a financial interest in the way you're implying."
        scene rottenborn:
            zoom 0.73
        br "You wouldn't consider a salary a financial interest?"
        scene dembrowski:
            zoom 0.73
        cd "I consider it a salary, but if you're asking if I get a share of the profits, then no."
        scene rottenborn:
            zoom 0.73
        br "You mentioned earlier that you've always felt protective of your younger brother. Is that accurate?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, that's correct."
        scene rottenborn:
            zoom 0.73
        br "You testified about Mr. Depp's reactions to your mother's anger during your childhood. Was he addicted to drugs or alcohol back then?"
        scene dembrowski:
            zoom 0.73
        cd "No, he was not."
        scene cocaine:
            zoom 0.73
        br "Did you observe Johnny using cocaine during his marriage with Amber?"
        scene dembrowski:
            zoom 0.73
        cd "No, I never saw him using cocaine."
        scene rottenborn:
            zoom 0.73
        br "Regarding the texts with Amber Heard regarding Johnny's substance abuse. Do you have any awareness of the context of those texts?"
        scene dembrowski:
            zoom 0.73
        cd "No, I do not."
        scene rottenborn:
            zoom 0.73
        br "Despite not witnessing Johnny doing cocaine, you tried to intervene with Amber regarding his substance abuse?"
        scene alcohol abuse:
            zoom 0.73
        cd "Yes, I was concerned, but my awareness was limited to his drinking habits."
        scene rottenborn:
            zoom 0.73
        br "You also mentioned some regrets about the messages you sent. Could you elaborate on that?"
        scene dembrowski:
            zoom 0.73
        cd "Well, I regret sending those messages because, at the time, I wasn't fully aware of the extent of Johnny's substance abuse."
        scene rottenborn:
            zoom 0.73
        br "Did you believe Amber Heard's claims of the severity of Johnny's actions?"
        scene dembrowski:
            zoom 0.73
        cd "I didn't fully believe her claims. My perspective was limited and Amber tends to exaggerate."
        scene rottenborn:
            zoom 0.73
        br "You had another text conversation with Amber about how she should handle Johnny in relation to his addiction. Can you share more about that?"
        scene bullseye:
            zoom 0.73
        cd "Yes, I advised her on how to approach the situation, as I felt she was being too confrontational. I wanted to find a more constructive way to address Johnny's struggles with addiction."
        scene judge:
            zoom 0.73
        j "Mr. Rottenborn, how much more do you have probably?"
        scene rottenborn:
            zoom 0.73
        br "About an hour."
        scene judge:
            zoom 0.73
        j "About an hour, okay. All right."
        j "Ladies and gentlemen, since it's 5:00, we're going to go ahead and release you for the day."
        scene time skip:
            zoom 0.75
        ""

    label day2:
        scene courtroom full:
            zoom 0.73
        """
        Day 2 Trial. Johnny Depp v. Amber Heard
        \nApril 13, 2022
        \nFairfax County, Virginia
        """
        scene depp:
            zoom 0.73  
        ""
        scene heard:
            zoom 0.73 
        ""
        scene judge:
            zoom 0.73 
        j "Good morning, ladies and gentleman. Let's continue, shall we?"
        scene rottenborn:
            zoom 0.73
        br "On August 18, 2024, you exchanged emails with Dr. David Kipper regarding the treatment of your brother. Could you shed some light on the nature of that communication?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, I communicated with Dr. Kipper about Johnny's treatment, particularly concerning his struggles with drug abuse, specifically pain pills. The doctor did keep me informed about Johnny's progress and treatment."
        scene rottenborn:
            zoom 0.73
        br "Did Johnny ever disclose to you that Amber had issues with anger?"
        scene dembrowski:
            zoom 0.73
        cd "Yes, Johnny did mention to me that Amber had difficulties with anger."
        scene rottenborn:
            zoom 0.73
        br "You mentioned earlier that you made an effort to talk to Amber whenever you felt the need. Can you elaborate on those conversations?"
        scene dembrowski:
            zoom 0.73
        cd "I reached out to Amber through text messages, expressing my willingness to talk. These conversations mainly revolved around Johnny's drug addiction."
        scene rottenborn:
            zoom 0.73
        br "In these exchanges with Amber, what were your primary concerns?"
        scene dembrowski:
            zoom 0.73
        cd "My primary concern was Johnny's well-being. I was worried about his life and not just how his actions might affect others."
        scene rottenborn:
            zoom 0.73
        br "Let's address Exhibit 210, which includes texts with Amber."
        br "Were you asked about Johnny's finger injury during the filming of \"Pirates of the Caribbean\", and was there any discussion about covering it up?"
        scene finger bleed:
            zoom 0.73
        cd "Yes, I was asked about Johnny's finger injury, and there were discussions about how to handle it, including the possibility of covering it up."
        scene rottenborn:
            zoom 0.73
        br "Why would you want to cover it up?"
        scene dembrowski:
            zoom 0.73
        cd "We certainly didn't want any press to know about it. So that's, you know, to keep it from that."
        scene rottenborn:
            zoom 0.73
        br "That's all Your Honor."
        scene judge:
            zoom 0.73
        j "All right, your next witness."
        scene lecaroz:
            zoom 0.73
        rl "Good morning, Your Honor. We the plaintiff call Isaac Baruch."
        rl "Good morning Isaac."
        scene barauch:
            zoom 0.73
        ib "Good morning."
        scene lecaroz:
            zoom 0.73
        rl "How do you know Mr. Depp?"
        scene barauch:
            zoom 0.73
        ib "We met as teenagers in Florida."
        scene lecaroz:
            zoom 0.73
        rl "Can you share more about that?"
        scene party: 
            zoom 0.75
        ib "Yeah, we met at parties and nightclubs. We later reconnected when I moved to California in September 1985."
        scene lecaroz:
            zoom 0.73
        rl "When you moved to California. Where you aware of Johnny's pursuit of acting during that time?"
        scene barauch:
            zoom 0.73
        ib "Yes, I knew he was interested in acting."
        scene lecaroz:
            zoom 0.73
        rl "How often did you see Johnny after reconnecting in California?"
        scene band instruments:
            zoom 0.73
        ib "Only a few times, mainly through mutual relationships. Johnny joined my buddy's band and I at the time moved to California to pursue music while also working retail."
        scene lecaroz:
            zoom 0.73
        rl "What were you doing for Mr. Depp when you started working for him in 1993?"
        scene nightclub:
            zoom 0.73
        ib "Well, he owned a place called the Viper Room, which is a music venue, nightclub, bar, and bands play. And it was already open for six months. I worked there from 1993 to 1998."
        scene lecaroz:
            zoom 0.73
        rl "After 1998, you mentioned Johnny's involvement in your art career. Can you tell us more about that transition?"
        scene barauch:
            zoom 0.73
        ib "I moved back to LA, worked at an art gallery, and joined the Viper Room for another year in 2000. Johnny took an interest in my pursuit of an art career."
        scene lecaroz:
            zoom 0.73
        rl "Here I present Exhibit 116: a floor plan of the the Eastern Columbia building. Can you discuss the time you moved in to this building?"
        scene penthouse:
            zoom 0.73
        ib "Certainly. I moved into Penthouse 2 in March 2013, and shortly after, Johnny and Amber moved into Penthouse 3. Rocky Pennington, a friend of Amber's, and Heard's sister also moved in."
        scene lecaroz:
            zoom 0.73
        rl "You mentioned earning $100,000 from your art show. How did this relate to your relationships with Johnny and the others?"
        scene barauch:
            zoom 0.73
        ib "Johnny provided financial support for my art career, around $100,000, over four years. I used some of it to pay for an MRI and therapy."
        scene lecaroz:
            zoom 0.73
        rl "You mentioned falling in love with Amber. Can you share your observations of Johnny and Amber's relationship?"
        scene barauch:
            zoom 0.73
        ib "They loved each other, treated each other with respect. I never witnessed violence but did see them argue." 
        ib "Once, Johnny screamed on the phone, \"Who is he?\"and Amber responded, \"Calm down, baby.\""
        ib "It was a non-stop argument with no end. I had to intervene by taking the phone from Johnny and telling Amber to stop."
        ib "Johnny was drunk though."
        scene lecaroz:
            zoom 0.73
        rl "Your Honor, I'm about to switch gears a little bit. It might be a good time for a mid-morning break."
        scene judge:
            zoom 0.73
        j "Alright Great! We are going to take a break."
        scene barauch:
            zoom 0.73
        ib "I gotta stay here the whole time?"
        scene judge:
            zoom 0.73
        j "Yes sir."
        scene courtroom empty:
            zoom 0.73
        "Break..."
        scene brain:
            zoom 0.73
        rl "(Internal Thoughts)\nI am running out of time here. I got to start asking the questions that will put a hole in Amber Heard's defense. How should I go about this?"
        menu:
            "Ask about Amber Heard's bruises": # gain points
                $ score +=1
                jump day2_pt1

            "Ask about Amber Heard's behavior":
                jump wrong3

    label wrong3:
        scene hallway:
            zoom 0.73
        bc "Hey Rebecca. Make sure you focus on getting information about the bruises."
        rl "Really I thought that would be too direct."
        bc "Worst thing that can happen is an objection."

    label day2_pt1:
        scene courtroom full:
            zoom 0.73
        "Day 2 resumes ..."
        scene judge:
            zoom 0.73
        j "Your next question, Ms. Lecaroz."
        scene lecaroz:
            zoom 0.73
        rl "Have you ever witnessed any instances of violence between Johnny get physically violent with Amber?"
        scene barauch:
            zoom 0.73
        ib "No, I did not see Johnny hit her. Throughout my whole time living at the penthouse."
        scene lecaroz:
            zoom 0.73
        rl "Leading up to the days before the divorce. Did you see any bruising, sweling, or redness on Amber's face."
        scene heard bruise:
            zoom 0.73
        ""
        scene barauch:
            zoom 0.73
        ib "No cuts, no bruises, no swelling, no redness, no ..."
        ib "It's Amber."
        scene heard:
            zoom 0.73
        ib "It's Amber's face. Just how it is now."
        scene lecaroz:
            zoom 0.73
        rl "How did you learn about the divorce?"
        scene barauch:
            zoom 0.73
        ib "I was shocked about it because I learned about it on the internet. Despite seeing Amber in the hallways all week."
        scene lecaroz:
            zoom 0.73
        rl "How did you learn about the divorce?"
        scene barauch:
            zoom 0.73
        ib "Yes, she did offer food, but I refused, and that marked the end of our relationship."
        scene lecaroz:
            zoom 0.73
        rl "You mentioned a video showing Amber and Whitney waiting for an elevator. Could you elaborate on that?"
        scene barauch:
            zoom 0.73
        ib "Yes, in the video, Amber and Whitney were waiting for an elevator, and they were playing around; fake punch Amber like they claimed Johnny did. They were laughing during this interaction."
        scene lecaroz:
            zoom 0.73
        rl "That's all I have, Your Honor."
        scene judge:
            zoom 0.73
        j "Thank you  Ms. Lecaroz. Cross-examination."
        scene examine:
            zoom 0.73
        ""
        scene bredehoft:
            zoom 0.73
        eb "Let's us start off the makeup. Have you seen Ms. Heard putting on makeup."
        scene barauch:
            zoom 0.73
        ib "Yes, plenty of times in the years I lived in the penthouse."
        scene bredehoft:
            zoom 0.73
        eb "So when you're saying that you didn't notice any makeup, would it be fair to say that you yourself are not familiar with what type of makeup Amber Heard uses on a daily basis?"
        scene barauch:
            zoom 0.73
        ib "I don't know what she uses on a daily basis."
        scene bredehoft:
            zoom 0.73
        eb "That is my point ..."
        scene barauch:
            zoom 0.73
        ib "Well I don't what she uses but I can tell when she uses it."
        scene bredehoft:
            zoom 0.73
        eb "Did Amber ever tell you she was not wearing makeup?"
        scene barauch:
            zoom 0.73
        ib "As many times as she's told me, \"I am wearing makeup,\" which is I can't remember. So I don't know. Yeah, no. There's not onetime I remember that, her saying that."
        scene bredehoft:
            zoom 0.73
        eb "Regarding your arrangements on Depp's property. You live rent free in the penthouses for a number of years and now you've been rent-free ever since in Sweetzer."
        scene barauch:
            zoom 0.73
        ib "Yeah that is what you call a good friend."
        scene bredehoft:
            zoom 0.73
        eb "Yeah, okay. And I think you testified already, you were pretty angry with Ms. Heard at the time, right?"
        scene barauch:
            zoom 0.73
        ib "About the phony pictures that were taken and put in tabloids, and about the fake narrative, and about...and the way she's trying to get a fraudulent DV claim to extort and blackmail a man. Yeah, that kind of got me."
        scene bredehoft:
            zoom 0.73
        eb "Are you still angry with Ms. Heard?"
        scene barauch:
            zoom 0.73
        ib "Am I angry anymore? I'm not. You know, what I am is tired and I want this all to end. Her to go heal. Him to go heal. You know, so many people have been affected by this malicious lie that she started and she created."
        ib "It's gone out the door and around the world. And so I'd only... I can't even paint anymore."
        ib "I've stopped painting for the last who knows how many years. And that's affected by stuff. I'm not angry at anybody. I want the best for her, for her to take her responsibility, heal, and move on, move on."
        ib "For Johnny. Johnny, you know, his family has been completely wrecked by all of this stuff and it's not fair. It's not right what she did and what happened for so many people to get affected from this. It's insane how this happened."
        scene bredehoft:
            zoom 0.73
        eb "Okay."
        eb "Thank you, Your Honor."
        scene judge:
            zoom 0.73
        j "Ladies and gentlemen, we'll go ahead and take our afternoon lunch. We'll give you till 2:30 to take care of lunch. Again, no outside information and please don't discuss this case."
        scene time skip:
            zoom 0.75
        "After lunch, the judge was shown video evidence that verified Amber Heard and Johnny Depp were staying at Eastern Columbia Building for specific days."
        scene judge:
            zoom 0.73
        j "All right. Ladies and gentlemen, since it's 5:00, we're going to go ahead and release you for the day."
        scene time skip:
            zoom 0.75

    label day3:
        scene courtroom full:
            zoom 0.73
        """
        Day 3 Trial. Johnny Depp v. Amber Heard
        \nApril 14, 2022
        \nFairfax County, Virginia
        """
        scene depp:
            zoom 0.73  
        ""
        scene heard:
            zoom 0.73 
        ""
        scene judge:
            zoom 0.73 
        j "Good morning. Your first witness."
        scene rottenborn:
            zoom 0.73
        br "Good morning, Your Honor. Our first witness is Kate James by video."
        scene james camera:
            zoom 0.73
        br "Good morning, Ms. James. Can you please state your full name?"
        scene james:
            zoom 0.73
        kj "My name is Katherine Olwin James."
        scene zoom meeting:
            zoom 0.73
        br "When did you first start working as a Amber Heard's personal assistant?"
        scene james:
            zoom 0.73
        kj "In 2012."
        scene zoom meeting:
            zoom 0.73
        br "What were your job duties?"
        scene james:
            zoom 0.73
        kj "I mean if you are ready for a really, really long time of me explaining all of the details, that's fine. It's everything you could possibly do to run someone's life."
        kj "Okay? ..."
        kj "So it is grocery shopping. It is taking care of admin. It is running errands. It is getting the car fixed. It is getting the dog's groomed. It is picking up flowers."
        kj "Every day, it's something different. It's a myriad of things that go across the board daily."
        scene zoom meeting:
            zoom 0.73
        br "You were paid for that work, correct?"
        scene james:
            zoom 0.73
        kj "Very poorly."
        scene courtroom full:
            zoom 0.73
        "(People in the courtroom laugh)"
        scene judge:
            zoom 0.73
        j "Order. Order."
        scene zoom meeting:
            zoom 0.73
        br "What were you paid? Was it $1,500 a week to start?"
        scene james:
            zoom 0.73
        kj "Are you kidding? I wish. My God. No, it was not. She paid me $25 an hour to start off with. She finally agreed after screaming abuse at me that she would pay me $50,000 a year once I went to full-time."
        kj "This was after me working for well over 10 years as a personal assistant."
        scene zoom meeting:
            zoom 0.73
        br "You never believed Ms. Heard that Mr. Depp had mistreated her? Is that correct?"
        scene james:
            zoom 0.73
        kj "At the time or after? I never believed...in what context are you talking about, during my employment or afterward?"
        scene zoom meeting:
            zoom 0.73
        br "During your employment."
        scene james:
            zoom 0.73
        kj "No, never. And there was never any damage to the apartment that I witnessed. There was never any aftermath of anything ever, that I ever saw."
        scene zoom meeting:
            zoom 0.73
        br "Did you resent misheard for that, for terminating your employment?"
        scene james:
            zoom 0.73
        kj "It would have been nice to be given some notice so I had some time to look around. So I was a little upset for the lack of notice. But apart from that, no, I was not upset."
        scene vasquez:
            zoom 0.73
        "Plaintiff Direct Examination"
        scene zoom meeting:
            zoom 0.73
        cv "I believe you previously testified to this so sorry for asking you again but while you worked for Ms. Heard, did you ever see any types of injuries on her? Any cuts, bruises, swelling, redness, black eyes."
        scene james:
            zoom 0.73
        kj "No never."
        scene zoom meeting:
            zoom 0.73
        cv "What was your impression of Mr. Depp?"
        scene james:
            zoom 0.73
        kj "He's such a gentleman. He's like a total Southern gentleman."
        scene zoom meeting:
            zoom 0.73
        cv "Did you ever witness Mr. Depp be rude to anyone?"
        scene james:
            zoom 0.73
        kj "No, never."
        scene zoom meeting:
            zoom 0.73
        cv "You mentioned bringing your son to work. Did Mr. Depp ever interact with your son?"
        scene band instruments:
            zoom 0.73
        kj "Yes, countless times and he would even teach him how to play guitar. He gave my son a little pick as well, a guitar pick, which he cherishes to this day as well."
        scene zoom meeting:
            zoom 0.73
        cv "You mentioned being unfairly compensated. Did you receive any verbal abuse for requesting more money."
        scene james:
            zoom 0.73
        kj "I do remember on one occasion when we were moving from part-time to full-time, and then the salary negotiations became a real bone of contention."
        kj "I specifically remember standing in her office where she leapt up out of her chair, put her face approximately 4 inches from my face, and she was spitting in my face, and telling me how dare I ask for the salary I was asking for, which was in fact approximately half of my regular annual salary."
        kj "I was offering her that as a favor. And she felt that gave her the right to spit in my face. And there was a witness in the apartment at that time, by the way."
        scene zoom meeting:
            zoom 0.73
        cv "I don't have any further questions. Thank you for your time today."
        scene james:
            zoom 0.73
        kj "You're welcome."
        scene judge:
            zoom 0.73
        j "Thank you. All right, ladies and gents, let's go ahead and take our morning recess for 15 minutes."
        scene courtroom empty:
            zoom 0.73
        "Break ..."
        scene judge:
            zoom 0.73
        j "All right, your next witness."
        scene rottenborn:
            zoom 0.73
        br "Your Honor. Our second witness is Dr. Laurel Anderson by video."
        scene doc camera:
            zoom 0.73
        br "You're a clinical psychologist, is that correct?"
        scene anderson:
            zoom 0.73
        la "Correct. Psychotherapy for individuals and couples\."
        la "It's an evaluation of an individual or a couples' problems. Then, it's a conceptualization of what's actually going on and an effort to make intervention that leads to change."
        scene zoom meeting:
            zoom 0.73
        br "So as I understand it, starting October 1st, 2015, Mr. Depp and Amber would come for couples counseling?"
        scene anderson:
            zoom 0.73
        la "Yes."
        scene zoom meeting:
            zoom 0.73
        br "In working with Amber and Mr. Depp, did Amber ever report to you any physical violence on behalf of Mr. Depp toward Amber?"
        scene anderson:
            zoom 0.73
        la "Yes. I have seen photos of Amber with bruising around her eyes."
        scene zoom meeting:
            zoom 0.73
        br "Did you witness abuse by either?"
        scene anderson:
            zoom 0.73
        la "I did not witness any."
        scene zoom meeting:
            zoom 0.73
        br "Is it your testimony that while Mr. Depp may have said he wasn't violent with any of his other partners, there was violence from Mr. Depp toward Amber, correct?"
        scene anderson:
            zoom 0.73
        la "Yes, you're right. both were victims of abuse in their homes. But I thought he had been well controlled for decades. Then with Ms. Heard, he was triggered. They engaged in what I saw as mutual abuse sometimes."
        la "I know she led on more than one occasion, and started it to keep him with her because abandonment and having him leave was her worst nightmare. I think he may have initiated it on occasions too, that I'm less sure on."
        scene zoom meeting:
            zoom 0.73
        br "How did you come to the understanding that on some occasions Ms. Heard physically abused Mr. Depp?"
        scene anderson:
            zoom 0.73
        la "Ms. Heard reported that."
        scene chew:
            zoom 0.73
        "Plaintiff Direct Examination"
        scene zoom meeting:
            zoom 0.73
        bc "When Ms. Heard told you that Johnny Depp hits her or slaps her, Johnny Depp was not present. Correct?"
        scene anderson:
            zoom 0.73
        la "Correct he was not present."
        scene zoom meeting:
            zoom 0.73
        bc "When you were talking about how the size of it, your fingers were under your eyes. Do you remember seeing the bruises under Amber's eyes?"
        scene anderson:
            zoom 0.73
        la "That's what I recall. They may have been in other places throughout her body. I don't remember. But I do remember her face."
        scene zoom meeting:
            zoom 0.73
        bc "I don't have any further questions. Thank you for your time today."
        scene james:
            zoom 0.73
        la "You're welcome."
        scene judge:
            zoom 0.73
        j "Alright Great! We are going to take our lunch break."
        scene courtroom empty:
            zoom 0.73
        "Break ..."
        scene brain:
            zoom 0.73
        sm "(Internal Thoughts)\nI need a witness to prove that Johnny is not violent." 
        sm "(Internal Thoughts)\nA friend that is a girl." 
        sm "(Internal Thoughts)\nGina is a good candidate."
        sm "(Internal Thoughts)\nShe is known to be a bit cuckoo. Shall I take the gamble?"
        menu:
            "Call Gina Deuters as a witness": #gain points
                $ score +=1
                jump day3_pt2
            
            "Don't call her as a witness":
                jump day3_pt3

    label day3_pt2:
        scene judge:
            zoom 0.73 
        j "Your next witness."
        scene moniz:
            zoom 0.73
        sm "We call Gina Deuters."
        sm "Good afternoon Ms. Deuters."
        scene deuters:
            zoom 0.73
        gd "Hi."
        scene moniz:
            zoom 0.73
        sm "Can you tell us a little bit about what your occupation is?"
        scene deuters:
            zoom 0.73
        gd "Currently I am a freelance creator who kind of conceptualized, and shoots, and edits photographs and clips, largely for social media."
        scene moniz:
            zoom 0.73
        sm "Do you know Johnny Depp?"
        scene deuters:
            zoom 0.73
        gd "I do. He is a good friend of mine that I met in 2005."
        scene moniz:
            zoom 0.73
        sm "Over the course of your friendship with Mr. Depp, have you ever seen Mr. Depp take drugs or drink?"
        scene deuters:
            zoom 0.73
        gd "I've seen him smoke weed and occasionally cocaine. Also, drinking."
        scene moniz:
            zoom 0.73
        sm "Have you ever partaken of any of these substances at the same time?"
        scene deuters:
            zoom 0.73
        gd "Yes."
        scene cocaine:
            zoom 0.73
        sm "How many times would you estimate you've seen Mr. Depp use cocaine?"
        scene deuters:
            zoom 0.73
        gd "Oh, gosh, I mean, it's usually, like, you know, kind of a celebratory event like after a gig or a party or something." 
        gd "Twenty? I don't know, 20 times over the ... Yeah."
        scene alcohol abuse:
            zoom 0.73
        sm "Does he seem to drink to excess in your experience?"
        scene deuters:
            zoom 0.73
        gd "No."
        scene moniz:
            zoom 0.73
        sm "Did you see Mr. Depp and Ms. Heard interact at all on that 2021 Las Vegas trip? Can you describe it for us?"
        scene deuters:
            zoom 0.73
        gd "Yes. They seemed pretty in love. They were tactile and, you know, they seemed happy."
        scene approach:
            zoom 0.73
        br "Your Honor, may we approach?"
        scene rottenborn:
            zoom 0.73
        br "You might want to look at this. ..."
        scene judge:
            zoom 0.73
        j "Okay. Ladies and gentlemen of the jury, we just have to take a few housekeeping matters up. So we're just gonna have you take a recess for a few minutes, okay? So, again, no outside research and don't talk to anybody, okay?"
        scene jury leaves:
            zoom 0.73
        "Jury leaves ..."
        scene judge:
            zoom 0.73
        j "All right. Ms. Deuters, I just had a question for you."
        j "Have you been watching the trial this past week?"
        scene deuters:
            zoom 0.73
        gd "Yes. I've seen a couple of clips of the trial online."
        scene moniz:
            zoom 0.73
        sm "Ms. Deuters, have you been watching...?"
        scene judge:
            zoom 0.73
        j "It doesn't matter. She's been watching clips of witness testimony. All right, you're excused, ma'am."
        scene brain :
            zoom 0.73
        sm "(Internal Thoughts)\nBen and Camille are going to kill me."
        scene judge:
            zoom 0.73
        j "Thank you. I will instruct the jury to have to strike the testimony of Ms. Deuters. We will continue the break for another 15 minutes."
        scene courtroom empty:
            zoom 0.73
        "Break ..."

    label day3_pt3:
        scene judge :
            zoom 0.73
        j "Alright your next witness."
        scene moniz:
            zoom 0.73
        sm "Your Honor, we call Dr. David Kipper by video designation."
        scene doc camera:
            zoom 0.73
        br "Could you please provide your full name?"
        scene kipper:
            zoom 0.73
        ak "David Alan Kipper."
        scene zoom meeting:
            zoom 0.73
        br "You're a doctor, correct?"
        scene kipper:
            zoom 0.73
        ak "Yes."
        scene zoom meeting:
            zoom 0.73
        br "What did you discuss with Mr. Depp at that first meeting?"
        scene love drugs:
            zoom 0.73
        ak "Mr. Depp was seeking treatment for substance abuse and wanted to detoxify from his substance abuse. Alcohol, opiates, benzodiazapines, and stimulants."
        scene drugs:
            zoom 0.73
        br "Drug tests showed Mr. Depp being positive for cocaine and THC, correct?"
        scene kipper:
            zoom 0.73
        ak "Yes, correct."
        scene zoom meeting:
            zoom 0.73
        br "Did you ever see violence between Ms. Heard and Mr. Depp?"
        scene kipper:
            zoom 0.73
        ak "No."
        scene zoom meeting:
            zoom 0.73
        br "Regarding visiting Johnny Depp in Australia in March of 2015, what happened?"
        scene kipper:
            zoom 0.73
        ak "Mr. Depp had wanted to see me. He had just wanted to check in. He wanted my company at that point because of what happened to his finger."
        scene zoom meeting:
            zoom 0.73
        br "What had happened to his finger?"
        scene finger bleed:
            zoom 0.73
        ak "He had had part of his finger taken off as a result of a fight with Amber."
        scene moniz:
            zoom 0.73
        sm "That is it, Your Honor."
        scene judge:
            zoom 0.73
        j "Alright it is 5:00. We will see you guys next week."
        scene court cameras with fade:
            zoom 0.73
        scene time skip:
            zoom 0.75
        "End of Week 1"
        # Display the score and end the game
        call display_score
        return

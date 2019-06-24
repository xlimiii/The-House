import time
from random import randint
import os

spells = ["'avada kedavra' - killing curse", "'expecto patronum' - protect you from the evil", "'Alohomora'- open locked doors"]
animals = ["tiger", "pig", "deer", "goose", "possum", "cow"]
kpn = ["rock", "paper", "scissors"]
#animacja tekstu
def animacja_tekstu(tekst):
    for i in tekst:
        print '\b'+i, 
        time.sleep(0.02)
    print("")

#wstep do pokoju z bajkami i wybor: stolik, karaoke czy parkiet?
def fairy_tales():
    animacja_tekstu("You came to a really strange place... \nWhat a colorful world! It is absolutely incomparable to the earlier room. \nYou see lots of well known faces.\nThere are Anna, Elsa, Winnie the Pooh, Buzz Astral, even Timon and Pumba sitting at the table.\nThey're drinking tea. \nBehind there are  Blossom, Bubbles and Buttercup dancing with Snow White and Peter Pan. \nPinocchio with Little Red Riding Hood are singing karaoke. \nThey're pretty good. They're singing 'Dancing Queen'. \nYou can't believe your own eyes. Honestly, I totally get that. \nBut it looks like a safe place. Those guys still didn't notice that you came in, \nhowever - you have to make a decision. You can't stand there like that. \nWhat are you doing? \nPress A if you decided to walk to the guys at the table. \nPress B if you wanna start performing on karaoke. \nPress C if you're thinking 'Let's dance- 'Dancing Queen' is my favourite piece!")
    choice1 = raw_input()
    choice1 = choice1.lower()
    if choice1 == "a":
        os.system("cls")
        table()
    elif choice1 =="b":
        os.system("cls")
        karaoke()
    elif choice1 =="c":
        os.system("cls")
        dance()
    else:
         animacja_tekstu ("You chose the wrong letter.")
         os.system("cls")
         fairy_tales()
#parkiet-bajki
def dance():
    animacja_tekstu("You start dancing but, to be honest, you suck... \nChoose something else. \nPress A if you decided to walk to the guys at the table. \nPress B if you wanna start performing on karaoke.")
    choicee = raw_input()
    choicee = choicee.lower()
    if choicee == "a":
        os.system("cls")
        table()
    elif choicee =="b":
        os.system("cls")
        karaoke()
    else:
        animacja_tekstu( "You chose the wrong letter.")
        os.system("cls")
        dance()
#stolik-bajki
def table():
    animacja_tekstu("At the table you see two free sits. \nYou can choose if you want sit next to Buzz Astral or Elsa. \nPress name of character: ")
    name = raw_input()
    name = name.lower()
    if (name == "buzz astral" or name == "buzz"):
        os.system("cls")
        buzz()
    elif name == "elsa":
        os.system("cls")
        elsa()
    else:
        animacja_tekstu ("You pressed the wrong expression")
        os.system("cls")
        table()
#buzz-stolik-bajki
def buzz():
    animacja_tekstu("You sit next to Buzz. \nYou start a conversation, introduce yourself and tell what happened to you before. \nHe suggests: Let's play 'Rock, paper, scisssors'! \nIf you win, I will help you get out of here. \nDo you agree? \nA-Yes, at least there is some hope... \nB-No, thanks. I prefer to sit next to Elsa. \nPress A or B: ")
    choice1=raw_input()
    choice1=choice1.lower()
    if choice1=="a":
        os.system("cls")
        rps()
    elif choice1=="b":
        os.system("cls")
        elsa()
    else:
        animacja_tekstu("You pressed the wrong letter")
        os.system("cls")
        buzz()
#kamien, papier, nozyce
def rps():
    animacja_tekstu("Press: rock, paper or scissors?")
    your_choice = raw_input()
    your_choice = your_choice.lower()
    i = randint(0,2)
    buzz_choice = kpn[i]
    animacja_tekstu("Buzz choice: %s" % (buzz_choice))
    time.sleep(3)
    if your_choice == str(buzz_choice):
        animacja_tekstu("It's a tie! Play again!")
        os.system("cls")
        rps()
    elif your_choice == kpn[0] and buzz_choice == kpn [2]:
        os.system("cls")
        animacja_tekstu("You win! \nBuzz keeps the promise and fly away with you: 'to infinity and beyond!'")
    elif your_choice == kpn[1] and buzz_choice == kpn [0]:
        os.system("cls")
        animacja_tekstu("You win! \nBuzz keeps the promise and fly away with you: 'to infinity and beyond!'")
    elif your_choice == kpn[2] and buzz_choice == kpn [1]:
        os.system("cls")
        animacja_tekstu("You win! \nBuzz keeps the promise and fly away with you: 'to infinity and beyond!'")
    else:
        os.system("cls")
        lost_rps()
#przegranie w kamien, papier, nozyce
def lost_rps():
    animacja_tekstu("You lost! \nIt's a game for life and death. \nBut you have your last chance to save. \nWhere do you run? \nL - left \nR - right \nPress L or R: ")
    choice = raw_input()
    choice = choice.lower()
    if choice == "l":
        os.system("cls")
        animacja_tekstu("Winnie the pooh hits you in your head. You wake up in different room.")
        os.system("cls")
        joker()
    elif choice =="r":
        os.system("cls")
        animacja_tekstu("Pumba hits you in your head. You wake up in different room.")
        os.system("cls")
        harry_potter()
    else:
        os.system("cls")
        animacja_tekstu("You pressed the wrong letter")
        os.system("cls")
        lost_rps()
#elza, stolik, bajki
def elsa():
    animacja_tekstu("You sit next to Elsa. \nShe's not in the mood. \nSo she decides to freeze you. \nYou wake up in different room.")
    time.sleep(4)
    os.system("cls")
    joker()
#karaoke-bajki
def karaoke():
    animacja_tekstu("There's no one on waiting list, so you're next. \nWhat song do you want to sing? \nPress a title: ")
    song = raw_input()
    os.system("cls")
    animacja_tekstu("3...")
    animacja_tekstu("2...")
    animacja_tekstu("1...")
    animacja_tekstu("sing!")
    time.sleep(2)
    os.system("cls")
    animacja_tekstu("In my opinion you're rock! But your audience don't think so... \nYou're such a loser, but '%s' is special song here and singing it is just like a profanation. \nThey seem to be really mad. What are you doing?" % (song))
    stay_or_run()
#spiewanie, karaoke-bajki
def stay_or_run():
    animacja_tekstu("Press A if you decide to run away.")
    animacja_tekstu("Press B if you don't care- show must go on!")
    choice1 = raw_input()
    choice1 = choice1.lower()
    os.system("cls")
    if choice1 == "a":
        animacja_tekstu("You see door! Hurry up, they're chasing you and there is madness in theirs eyes!" )
        time.sleep(3)
        os.system("cls")
        joker()
    elif choice1 == "b":
        time.sleep(3)
        os.system("cls")
        stay_and_sing()
    else:
        animacja_tekstu( "You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        stay_or_run()
#wybor karaoke-bajki, przegranie
def stay_and_sing():
    animacja_tekstu("They're screaming. You see madness in theirs eyes. \nThey look nothing like your favourite characters from childhood even though they look the same. \nYou're scared \nDo you want to run away now? \nPress Yes or No: ")
    choice2 = raw_input()
    choice2 = choice2.lower() 
    os.system("cls")
    if choice2 == "yes":
        animacja_tekstu("Sorry, it's too late... \nThey catch you and...\nOh God, what are they doing with you?! \nIt's terrible! \nSorry, Sleeping Beauty and Peter Pan killed you and you're dead.")
    elif choice2 == "no":
        animacja_tekstu("You don't want to stop singing. \nThey catch you and...\nOh God, what are they doing with you?! \nIt's terrible! \nSorry, Sleeping Beauty and Peter Pan killed you and you're dead.")
    else: 
         animacja_tekstu( "You chose the wrong letter.")
         time.sleep(3)
         os.system("cls")
         stay_and_sing()
#hannibal, wstep
def hannibal():
    animacja_tekstu("You hear music. It's Beethoven's 5th Symphony. \nLooking around. \nOn the left side you see lots of books. \nMost of them is about anatomy. \nNext to the books there are refrigerators. \nYou hear that there is someone behind the books. \nOn the right side there is the door. \nYou can go either left or right. \nL-go left \nR-go right \nPress L or R: ")
    direct=raw_input()
    direct=direct.lower()
    os.system("cls")
    if direct == "l":
        left()
    elif direct =="r":
        animacja_tekstu("The door is locked.")
        time.sleep(3)
        os.system("cls")
        hannibal()
    else:
        animacja_tekstu("You chose the wrong letter")
        time.sleep(3)
        os.system("cls")
        hannibal()
#hannibal- rozmowa, pobicie czy szukanie?
def left():
    animacja_tekstu("You see a man sitting at the desk and working. \nA-come to him and start conversation \nB-fall on him from behind, sneak up and hit him on the head \nC-go right to the refrigerators \nPress A, B or C:")
    hannibal_choice = raw_input()
    hannibal_choice = hannibal_choice.lower() 
    os.system("cls")
    if hannibal_choice == "a":
        nice_talk()
    elif hannibal_choice == "b":
        animacja_tekstu("You did that! He's lying on the floor. \n")
        animacja_tekstu ("Now you have to find a key to open the door.")
        time.sleep(4)
        os.system("cls")
        look_for()
    elif hannibal_choice == "c":
        animacja_tekstu("You open a refrigerator. \nThere are human bodies inside! \nBut you find key! \nYou can finally go out of this awful room!")
        time.sleep(3)
        os.system("cls")
        harry_potter()
    else: 
        animacja_tekstu("You chose the wrong letter")
        time.sleep(3)
        os.system("cls")
        left()
#hannibal-rozmowa
def nice_talk():
    animacja_tekstu("You two have a nice conversation. It turnes out that he used to be psychiatrist. \nNow he helps police in catching criminals.")
    animacja_tekstu("He askes you: Are you hungry? \nPress Yes or No: ")
    hungry = raw_input()
    hungry = hungry.lower()
    os.system("cls")
    if hungry == "yes":
        y_hungry()
    elif hungry == "no":
        animacja_tekstu("He insist so much that you have to say 'yes'")
        time.sleep(3)
        os.system("cls")
        y_hungry()
    else:
        animacja_tekstu("You pressed the wrong expression")
        time.sleep(3)
        os.system("cls")
        nice_talk()
#hannibal-obiad
def y_hungry():
    animacja_tekstu("You go through the room and sit at the table. \nYour host layes the table and goes to the kitchen for his 'signature dish'. \nHe ensures you that it is delightful \nYou try it. \nIt tastes weird. \nIt's meat but it has sweet taste. \nYou also notice that guy is a little bit creepy. \nA- ask him what exactly 'signature dish' is \nB- excuse him and secretly go looking around for key to the door \nPress A or B: ")
    aft_dinner = raw_input()
    aft_dinner = aft_dinner.lower()
    os.system("cls")
    if aft_dinner == "a":
        last()
    elif aft_dinner == "b":
        look_for()
    else:
        animacja_tekstu("You typed in the wrong letter.")
        time.sleep(3)
        os.system("cls")
        y_hungry()
#hannibal-ucieczka czy zabicie?
def last():
    animacja_tekstu("He excuses you for a moment and brings you a photoalbum. \nHe asks you: The dinner was a little bit sweet, wasn't it? \nExactly like my ex-girlfriend: Jude! \nHe starts lauhging. \nIt's insane! \nHe tries to catch you. \nAre you trying to run away? \nA- Yes \nB- Actually no, I just ate human and I don't wanna live anymore... \nPress A or B: ")
    last_choice = raw_input()
    last_choice = last_choice.lower()
    os.system("cls")
    if last_choice == "a":
        animacja_tekstu("You see the door which you didn't notice before. Run! Yes, you did that!")
        time.sleep(4)
        os.system("cls")
        fairy_tales()
    elif last_choice == "b":
        animacja_tekstu("He catches you and ... \nyou know what is he going to do with your body...")
        time.sleep(3)
        os.system("cls")
    else: 
        animacja_tekstu("You chose the wrong letter")
        time.sleep(3)
        os.system("cls")
        last()
#hannibal- szukanie klucza
def look_for():
    animacja_tekstu("Where do you want to search? \nA-Through the books \nB-Through the refrigerators \nPress A or B: ")
    where = raw_input()
    where = where.lower()
    os.system("cls")
    if where == "a":
        animacja_tekstu("Key is not here")
        time.sleep(2)
        os.system("cls")
        look_for()
    elif where == "b":
        animacja_tekstu("You open a refrigerator. \nThere are human bodies inside! \nBut you find key! \nYou can finally go out of this awful room!")
        time.sleep(4)
        os.system("cls")
        harry_potter()
    else:
        animacja_tekstu("You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        look_for()   

#harry potter
def harry_potter():
    animacja_tekstu("It's absolutely dark in here \nYou can't see anything. \nBut you hear a voice... \nIt's woman's laugh. Pretty scary laugh. \nThere is a bag next to you.")
    animacja_tekstu("You have two options: \nA- Follow the voice, \nB- Check what's in the bag \nPress A or B: ")
    choice1 = raw_input()
    choice1 = choice1.lower()
    os.system("cls")
    if choice1 == "a":
        follow_harry()
    elif choice1 == "b":
        check_harry()
    else:
        animacja_tekstu( "You chose the wrong letter.")
        harry_potter()
#harry potter, idz za glosem
def follow_harry():
    animacja_tekstu(("You are closer and closer. \nNow you can recognise words she singing. \nAnd you hear: \n'I killed %s lalalala'") % player_name)
    animacja_tekstu("You are terrified but I assure you- you are still alive. \nOr maybe I should say- You are alive yet...")
    animacja_tekstu("You have to options: \nA- you can still follow the voice, \nB- you can come back and check the bag\nPress A or B:  ")
    choice2 = raw_input()
    choice2 = choice2.lower()
    os.system("cls")
    if choice2 == "a":
        bellatrix()
    elif choice2 == "b":
        check_harry()
    else:
        animacja_tekstu( "You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        follow_harry()
#harry potter, sprawdz torbe
def check_harry():
    animacja_tekstu("In the bag you find the wand and notebook 'The spells'")
    animacja_tekstu("Do you want to read the notebook? \nPress Yes or No: ")
    choice_notebook = raw_input()
    choice_notebook = choice_notebook.lower()
    os.system("cls")
    if choice_notebook == "yes":
        for i in spells:
            print i
        time.sleep(6)
        os.system("cls")
        decision_harry()
    elif choice_notebook == "no":
        decision_harry()
    else: 
         animacja_tekstu( "You chose the wrong letter.")
         time.sleep(3)
         os.system("cls")
         check_harry()       
#harry potter, final
def decision_harry():
    animacja_tekstu("Your eyes adjust to darkness. \nYou notice the door in the distance. \nThe woman is coming. \nShe is Bellatrix Lestrange... \nShe smiles weirdly and she says: \n'Hello, darling!' \nWhat are you doing? \nA- run to the door \nB- use the wand \nC- check the spells in the notebook")
    decision=raw_input()
    decision=decision.lower()
    os.system("cls")
    if decision == "a":
        animacja_tekstu("The door is locked")
        time.sleep(3)
        os.system("cls")
        decision_harry()
    elif decision == "b":
        press_spell()
    elif decision == "c":
        for i in spells:
            print i
        time.sleep(6)
        os.system("cls")
        decision_harry()
    else: 
        animacja_tekstu( "You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        decision_harry()
#harry potter, rzucanie zaklecia
def press_spell():
    animacja_tekstu("Press a spell: ")
    spell1 = raw_input()
    spell1 = spell1.lower()
    os.system("cls")
    if spell1 == "avada kedavra":
        animacja_tekstu("You cast a Killing Curse. \nBut it's not your wand, \nit doesn't work fully properly so the spell returns and... \nhits on you. \nSorry, you're dead.")
    elif spell1 == "expecto patronum":
        x = randint(0, len(animals)-1)
        animacja_tekstu("You did that! You create your patronus! \nIt takes the form of " + animals[x])
        animacja_tekstu("You get on it and fly away from this house!")
        animacja_tekstu("Congratulation! You survived! \nYou win!")
    elif spell1 == "alohomora":
        animacja_tekstu("It works! You open the door and run away to the next room")
        time.sleep(3)
        os.system("cls")
        joker()
    else: 
        animacja_tekstu("You chose the wrong spell")
        time.sleep(3)
        os.system("cls")
        decision_harry()
#harry potter, przegranie
def bellatrix():
    animacja_tekstu("And now you can see in the darkness. \nYou know that woman. \nShe is Bellatrix Lestrange... \nShe smiles and she says: \n'Hello, darling!' \nPress your response: ")
    raw_input()
    os.system("cls")
    animacja_tekstu("'Your words are unnecessery' \nShe pulls out her wand and scream: \n'AVADA KEDAVRA!'")
    animacja_tekstu("It's a killing curse, so... \nSorry, you're dead")

#wspinanie u freddiego
def climbing():
    animacja_tekstu( "You almost reached the vent!")
    animacja_tekstu( "You need to make a choice: grab the left or right pipe.")
    pipe = raw_input("Enter Left or Right: ")
    pipe = pipe.lower()
    os.system("cls")
    if pipe == "left":
        animacja_tekstu( "You made it!")
        animacja_tekstu( "You make it till the end and fall down a hole - into a new room.")
        animacja_tekstu( "")
        time.sleep(4)
        os.system("cls")
        hannibal()
    elif pipe == "right":
        animacja_tekstu( "The pipe breaks!")
        animacja_tekstu( "Freddy finds you and murders you.")
        animacja_tekstu( "You're dead.")
    else:
        animacja_tekstu( "You didn't choose a pipe!")
        animacja_tekstu( "")
        time.sleep(3)
        os.system("cls")
        climbing()

#atak freddiego
def attack():
    animacja_tekstu( "You hear a strange sound from behind.")
    animacja_tekstu( "You look behind you.")
    animacja_tekstu( "Freddie is chasing you! You start running away.")
    animacja_tekstu( "You have no choice but to climb the vent in front of you.")
    animacja_tekstu( "")
    time.sleep(4)
    os.system("cls")
    climbing()

# wybor przedmiotow na stole u jokera
def choice_joker():
    animacja_tekstu( "You can choose:") 
    animacja_tekstu( "A - a deck of cards.")
    animacja_tekstu( "B - a rolling dice.")
    animacja_tekstu( "C - a flower.") 
    animacja_tekstu("")
    your_joker_choice = raw_input("Enter A, B or C: ")
    your_joker_choice = your_joker_choice.upper()
    os.system("cls")
    if your_joker_choice == "A":
        animacja_tekstu( "Joker says: Oh! What a marvelous choice.")
        animacja_tekstu( "Now grab the first card off the deck.")
        animacja_tekstu( "You are stabbed by a blade. You start bleeding.")
        animacja_tekstu( "Joker says: Oops. My bad.")
        animacja_tekstu( "Now you have two more choices.")
        time.sleep(4)
        os.system("cls")
        choice2()
    elif your_joker_choice == "B":
        rolling_dice()
    elif your_joker_choice == "C":
        animacja_tekstu( "Joker says: Oh! Who wouldn't choose such a beautiful flower.")
        animacja_tekstu( "Touch it.")        
        animacja_tekstu( "The flower shoots acid straight at your face!")
        animacja_tekstu( "It stings extremely badly.")
        animacja_tekstu( "Joker says: Oops!")
        animacja_tekstu( "Now you have two more options.")
        time.sleep(4)
        os.system("cls")
        choice3()
    else:
        animacja_tekstu( "You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        choice_joker()

# 2 pozostale wybory gdy pierwszy wybor to A
def choice2():
    animacja_tekstu( "B is the rolling dice, C is the flower.")
    animacja_tekstu( "")
    second_choice = raw_input("Enter B or C: ")
    second_choice = second_choice.upper()
    animacja_tekstu( "")
    os.system("cls")
    if second_choice == "B":
        rolling_dice()
    elif second_choice == "C":
        animacja_tekstu( "Joker says: Oh! Who wouldn't choose such a beautiful flower.") 
        animacja_tekstu( "Touch it.")  
        animacja_tekstu( "The flower shoots acid straight at your face!")  
        animacja_tekstu( "It stings extremely badly.")   
        animacja_tekstu( "Joker says: Oops!")
        animacja_tekstu( "You start slowly dying.")
        animacja_tekstu( "Joker says: Well, you lost the game. Have a nice death.")
    else:
        animacja_tekstu( "You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        choice2()

# 2 pozostale wybory gdy pierwszy wybor to C
def choice3():
    animacja_tekstu( "B is the rolling dice, A is a deck of cards.")
    animacja_tekstu( "")
     
    second_choice2 = raw_input("Enter A or B: ")
    second_choice2 = second_choice2.upper()
    animacja_tekstu( "")
    os.system("cls")
    if second_choice2 == "B":
        rolling_dice()
    elif second_choice2 == "A":
        animacja_tekstu( "Joker says: Oh! What a marvelous choice.")        
        animacja_tekstu( "Now grab the first card off the deck.")     
        animacja_tekstu( "You are stabbed by a blade. You start bleeding.")
        animacja_tekstu( "Joker says: Oops. My bad.")
        animacja_tekstu( "You start slowly dying.")
        animacja_tekstu( "Joker says: Well, you lost the game. Have a nice death.")
    else:
        animacja_tekstu( "You chose the wrong letter.")
        time.sleep(3)
        os.system("cls")
        choice2()

# gra w number guess z jokerem
def rolling_dice():
    animacja_tekstu( "Joker says: Let's play a little game.")    
    animacja_tekstu( "It's called: number guess!")
    animacja_tekstu( "")
    time.sleep(3)
    os.system("cls")

    def get_user_guess():
        guess = int(raw_input("Go ahead! Guess a number: "))
        os.system("cls")
        return guess


    def roll_dice(number_of_sides):
        first_roll = randint(1, number_of_sides)
        second_roll = randint(1, number_of_sides)
        max_val = number_of_sides * 2
        animacja_tekstu( "The maximum possible value is %d." % (max_val))
        guess = get_user_guess()
        if guess > max_val:
            animacja_tekstu( "You guessed a wrong number.")
            time.sleep(3)
            os.system("cls")
        else:
            animacja_tekstu( "Rolling...")
            animacja_tekstu( "The first roll is: %d" % (first_roll))   
            animacja_tekstu( "The second roll is: %d" % (second_roll)) 
            total_roll = first_roll + second_roll
            animacja_tekstu( "The total roll is: %d" % (total_roll))
            animacja_tekstu( "Result...")
            time.sleep(4)
            os.system("cls")
             
            if guess == total_roll:
                animacja_tekstu( "You won.") 
                animacja_tekstu( "Joker says: Wait.. nobody ever wins this game..") 
                time.sleep(3)
                os.system("cls")
                animacja_tekstu( "This is ridiculous!!")   
                animacja_tekstu( "I cannot be defeated...")
                animacja_tekstu( "No, no, no...")        
                time.sleep(3)
                os.system("cls")
                animacja_tekstu( "Joker starts slowly fading away.")
                animacja_tekstu( "So does the room you're in.")
                animacja_tekstu( "Suddenly you're outside of the house, back where you started.")
                animacja_tekstu( "You feel extremely dizzy.") 
                time.sleep(5)
                os.system("cls")
                animacja_tekstu( "Was it just an illusion? Was it just a dream?...")
                animacja_tekstu( "Congratulations! You survived.")
            else:
                animacja_tekstu( "You lost.")
                time.sleep(2)
                os.system("cls")
                losing()
    roll_dice(6)

# przegranie z jokerem
def losing():
    animacja_tekstu( "Joker says: Oh, what a shame you lost!")  
    animacja_tekstu( "I wish I could let you down easy..")
    animacja_tekstu( "But what kind of a game would it be without a punishment?")
    time.sleep(5)
    os.system("cls")
    animacja_tekstu( "He cuts out one of your fingers.")
    animacja_tekstu( "Well, maybe now you'll have the chance to redeem yourself.")
    time.sleep(4)
    os.system("cls")
    animacja_tekstu( "You hear someone walking into the room you're in.")
    animacja_tekstu( "A female voice says: Honey, you're having all of this fun without me?")
    animacja_tekstu( "It's Harley Quinn.")  
    time.sleep(4)
    os.system("cls")
    animacja_tekstu( "Joker says that she came right in the time for the fun part.")
    time.sleep(3)
    os.system("cls")
    animacja_tekstu( "She says: Well but firstly come with me for a second, I need to show you something very important.")
    animacja_tekstu( "Joker whispers in your ear: we'll be back soon and ties your hands to the chair.")  
    animacja_tekstu( "You need to come up with a plan how to untie yourself.")
    time.sleep(6)
    os.system("cls")
    escaping_joker()
    
#ucieczka przed jokerem
def escaping_joker():
    animacja_tekstu( "You have two options:")
    animacja_tekstu( "A - try to swing the chair and look for a sharp object.")
    animacja_tekstu( "B - try to bite off the rope you're tied with.")
    animacja_tekstu("")
    option_escaping_joker = raw_input("Enter A or B: ")
    option_escaping_joker = option_escaping_joker.upper()
    animacja_tekstu("")
    os.system("cls")
    if option_escaping_joker == "A":
        animacja_tekstu( "You start swinging your chair and you finally fall down.")
        animacja_tekstu( "You see something that looks very sharp just a few metres away..")
        time.sleep(4)
        os.system("cls")
        animacja_tekstu( "You climb towards it.")
        animacja_tekstu( "You cut the rope with it.")
        animacja_tekstu( "You're free!")
        animacja_tekstu( "You see a door in front of you - you have no choice but to enter it.")
        time.sleep(4)
        os.system("cls")
        animacja_tekstu( "Suddenly.. the sun hits your eyes.")
        animacja_tekstu( "You're outside!")
        time.sleep(3)
        os.system("cls")
        animacja_tekstu( "Was it just an illusion? Was it just a dream?..")
        animacja_tekstu( "Congratulations! You survived.")

    elif option_escaping_joker == "B":
        animacja_tekstu( "You try to bite it off, but it's extremely hard to do so.")
        animacja_tekstu( "You manage to free your hands.")
        animacja_tekstu( "But at the exact moment Harley and Joker come into the room.")
        time.sleep(5)
        os.system("cls")
        animacja_tekstu( "Joker says: Well well well.. did someone try to escape?")
        animacja_tekstu( "Nice try, but me and Harley made a decision while we were gone.")
        animacja_tekstu( "Harley says: yeah.. we decided to kill you.")
        animacja_tekstu( "No hard feelings though.")
        animacja_tekstu( "We have things to do that are far more interesting.")
        time.sleep(5)
        os.system("cls")
        animacja_tekstu( "You start begging for mercy.. but Joker takes out a bottle of unknow liquid from his pocket.")
        animacja_tekstu( "It's a speciality of mine.")
        animacja_tekstu( "He forces you to drink it.")
        time.sleep(5)
        os.system("cls")
        animacja_tekstu( "You start slowly choking.")
        animacja_tekstu( "They leave the room laughing.")
        animacja_tekstu( "You die.")

    else:
        animacja_tekstu( "You typed in the wrong letter.")
        time.sleep(3)
        os.system("cls")
        escaping_joker()


#pokoj z jokerem
def joker():
    animacja_tekstu( "You're in a very dark room.")
    animacja_tekstu( "There's a smell of burning in the air.")
    animacja_tekstu( "You walk straightforward very carefully.")
    animacja_tekstu( "Suddenly, someone in front of you strikes a match.")
    animacja_tekstu( "It's Joker.. He says: Let's play some games.")
    time.sleep(5)
    os.system("cls")
    animacja_tekstu( "He drags you and ties you to a chair - but your hands are loose.")
    animacja_tekstu( "On the desk in front of you lay 3 objects.")
    animacja_tekstu( "Joker says you need to choose one of them.")
    time.sleep(5)
    os.system("cls")
    choice_joker()

#pokoj z freddy'em
def freddy():
    animacja_tekstu( "It's extremely misty and hot in the room you're in.")
    animacja_tekstu( "You're in a boiling house.")
    animacja_tekstu( "You can either go left or right.")
    animacja_tekstu( "")
    def direction1():
        direction = raw_input("Type in Left or Right: ")
        direction = direction.lower()
        animacja_tekstu( "")
        os.system("cls")
        if direction == "left":
            animacja_tekstu( "You see a vent.")
            animacja_tekstu( "The climb looks very dangerous tho.")
             
            def vent1():
                animacja_tekstu( "You can either climb it or keep on walking.")
                animacja_tekstu("")
                vent = raw_input("Type in Climb or Walk: ")
                vent = vent.lower()
                animacja_tekstu( "")
                os.system("cls")
                if vent == "climb":
                    climbing()
                elif vent == "walk":
                    attack()

                else:
                    animacja_tekstu( "You typed in the wrong expression.")
                    animacja_tekstu( "")
                    time.sleep(3)
                    os.system("cls")
                    vent1()
            vent1()

        elif direction == "right":
            animacja_tekstu( "You find an underground tunnel.")
            def tunnel():
                tunnel1 = raw_input("Type in E to enter it or K to keep on walking: ")
                tunnel1 = tunnel1.upper()
                os.system("cls")
                if tunnel1 == "E":
                    animacja_tekstu( "Corpses are laying on the ground - it smells extremely bad.")
                     
                    def corpse():
                        animacja_tekstu( "You can continue to walk on them or leave the tunnel and continue walking through the boiling house")
                        dead = raw_input("Type in C to continue walking or L to leave: ")
                        dead = dead.upper()
                        os.system("cls")
                        if dead == "C":
                            animacja_tekstu( "Finally after walking for around an hour you find an exit!")
                            animacja_tekstu( "You climb onto a new room.")
                            time.sleep(4)
                            os.system("cls")
                            hannibal()
                            
                        elif dead == "L":
                            attack()
                        else:
                            animacja_tekstu( "You entered a wrong letter.")
                            animacja_tekstu( )
                            time.sleep(3)
                            os.system("cls")
                            corpse()
                    corpse()
                elif tunnel1 == "K":
                    attack()
                else:
                    animacja_tekstu( "You typed in the wrong letter.")
                    animacja_tekstu( "")
                    time.sleep(3)
                    os.system("cls")
                    tunnel()
            tunnel()

        else:
            animacja_tekstu( "You typed in the wrong direction.")
            animacja_tekstu( "")
            time.sleep(3)
            os.system("cls")
            direction1()
    direction1()

#pokoj z pennywise
def pennywise():
    animacja_tekstu( "You hear a child's scream.")
    animacja_tekstu( "A red balloon is floating towards its sound.")
    animacja_tekstu( "")
     
    def follow():
        animacja_tekstu( "If you want to follow the voice enter Follow.")
        scream = raw_input("If you want to go the other way enter Other way: ")
        scream = scream.lower()
        animacja_tekstu( "")
        os.system("cls")
        if scream == "follow":
            animacja_tekstu( "You see Pennywise talking to the child and making it cry.")
            animacja_tekstu( "There are red doors to your right.")
            animacja_tekstu( "You can walk through them unnoticed. ")
             
            animacja_tekstu( "")
            time.sleep(4)
            os.system("cls")
            def crying_child():
                animacja_tekstu( "If you want to help the child enter Help. ")
                crying_kid = raw_input("If you want to leave enter Leave: ")
                crying_kid = crying_kid.lower()
                animacja_tekstu( "")
                os.system("cls")
                if crying_kid == "leave":
                    hannibal()
                elif crying_kid == "help":
                    def helping1():
                        animacja_tekstu( "You have 2 options.")
                        animacja_tekstu( "A - run towards the child, grab it and try to escape through the door.")
                        animacja_tekstu( "B - sneak behind Pennywise and try to choke him.")
                        animacja_tekstu( "")
                         
                        helping = raw_input("Enter A or B: ")
                        helping = helping.upper()
                        animacja_tekstu( "")
                        os.system("cls")
                        if helping == "A":
                            animacja_tekstu( "The kid releases from your grip.")
                            animacja_tekstu( "It's taken by Pennywise. Your only option is running away through the door.")
                            time.sleep(4)
                            os.system("cls")
                            hannibal() 
                        elif helping == "B":
                            animacja_tekstu( "You're caught!")
                            animacja_tekstu( "Pennywise says: Now you'll float too.")                            
                            animacja_tekstu( "You wake up in a different room.")
                            time.sleep(3)
                            os.system("cls")
                            freddy()
                        else:
                            animacja_tekstu( "You chose the wrong option.")
                            animacja_tekstu( "")
                            time.sleep(3)
                            os.system("cls")
                            helping1()
                    helping1()
                else:
                    animacja_tekstu( "You typed in the wrong option.")
                    animacja_tekstu( "")
                    time.sleep(3)
                    os.system("cls")
                    crying_child()
            
            crying_child()
        elif scream == "other way":
            animacja_tekstu( "You can't walk further.")
            animacja_tekstu( "The floor is full of holes and very unstable.")     
            animacja_tekstu( "You have to follow the voice.")
            animacja_tekstu( "")
            time.sleep(5)
            os.system("cls")
            follow()
        else:
            animacja_tekstu( "You typed in the wrong expression. ")
            animacja_tekstu( "")
            time.sleep(3)
            os.system("cls")
            follow()   

    follow()
#start gry
def start():
    animacja_tekstu( "You see a big, scary house.")
    animacja_tekstu( "It's been abandoned for 20 years now, the legend says.") 
    animacja_tekstu( "You can either go in or leave.")
    animacja_tekstu( "")
    enter = raw_input("Type in Enter if you want to come in, Leave if you want to leave: ")
    enter = enter.lower()
    if enter == "leave":
        animacja_tekstu( "Congratulations! You survived. But you might have missed a great adventure...")
    elif enter == "enter":
        os.system("cls")
        animacja_tekstu( "In front of you there are two doors. ")
        animacja_tekstu( "One of them is black and in front of it there is a red balloon hanging.")
        animacja_tekstu( "The other one is blue and it has scratch marks on it.")
        animacja_tekstu( "")
        colour = raw_input("Type in the colour of the door you want to go in: ")
        colour = colour.lower()
        animacja_tekstu( "")
        if colour == "black":
            os.system("cls")
            pennywise()
        elif colour == "blue":
            os.system("cls")
            freddy()
        else:
            os.system("cls")
            animacja_tekstu( "You typed in the wrong colour.")
            os.system("cls")
            start()   
    else:
        os.system("cls")
        animacja_tekstu( "You typed in the wrong expression.")
        os.system("cls")
        start()
#introduce
animacja_tekstu("Tatiana Cieslar, Dominika Limanowka")
animacja_tekstu("Welcome in...")
print "######   ##   ##  ####### "
print "  ##     ##   ##   ##     "
print "  ##     ##   ##   ##    "
print "  ##     #######   ####  "
print "  ##     ##   ##   ##     "
print "  ##     ##   ##   ##      "
print "  ##     ##   ##  #######  "
print ""
print "##   ##   #####   ##   ##   #####   #######"
print "##   ##  ##   ##  ##   ##  ##   ##   ##    "
print "##   ##  ##   ##  ##   ##  ##        ##     "
print "#######  ##   ##  ##   ##   #####    ####  "
print "##   ##  ##   ##  ##   ##       ##   ##      "
print "##   ##  ##   ##  ##   ##  ##   ##   ##      "
print "##   ##   #####    #####    #####   #######  "
print ""
animacja_tekstu("What's your name?")
player_name = raw_input()
os.system("cls")
animacja_tekstu(("Hello, %s. Let's start!") % player_name)
time.sleep(2)
os.system("cls")
start()


#%%

def adventure_game():
    print("you are flying home and notice that a man is fidgeting with his jacket and saw something that looked odd after you just woke up from your nap. You can TELL a flight attendant, ASK him if he is okay, or go back to SLEEP.")
    choice = input("Which choice do you make? ").strip().lower()
    
    if choice == "tell":
        print("You tell a flight attendant as they walk buy about the man and they go and check on the him. You see that she asks him if he’s okay and notice that she seems alarmed now.")
        print("you can get UP and see what is going on for yourself with the man, wait and ASK the flight attendant later, or YELL because you think everyone is in danger.")
        action = input("do you get UP and see what is going on for yourself, or ASK the flight attendant if she is okay").strip().lower()
        
        if action == "ask":
            print("the flight attendant walks down to the man to ask him what is going on, and at that moment you see a flash and a feel a hot sensation. you realize just before that flames engulf you that he set off a bomb...")
        elif action == "up":
            print("you get up and walk towards the man and as you approach him from behind you see that he sees you and that’s when he gets up and shoots you and right before you die you see that he has a bomb on his chest...")
        elif action == "yell":
            print("After yelling the man says we will all go home today and blows up the plane.")
        else:
            print("That is not a valid choice. The man notices you staring at him and pulls out a bomb and...")
    elif choice == "sleep":
        print("you go back to sleep and don’t wake up until after a man shakes you awake and is yelling at you...")
        print("You notice that he has a gun and is asking you to move to the back of the plane.")
        action = input("you can COMPLY or FIGHT.").strip().lower()
        
        if action == "comply":
            print("You comply with his request and later on find out that they are hijacking the plane and all of the sudden you then feel the plane loosing altitude quickly as you realize your going to crash.")
        elif action == "fight":
            print("You try to punch him and then you hear a bang! that’s when you feel your stomach and shirt getting wet, and your shirt is red now. You faint at that moment and never wake up...")
        else:
            print("That is not a valid choice. You waited to long and the man aims the gun at you and shoots, and you feel your life flash before your eyes.")
    elif choice == "ask":
        print("You lean forward and ask him if he’s okay...")
        print("He turns to you and says that he is okay because he will get to go home soon too...")
        action = input("You can ASK him where home is or LEAVE him alone.").strip().lower()
        
        if action == "ask":
            print("He tells you that home is heaven, and we will all be there soon. You go back to your seat confused, until he gets up and yells that heaven is home and blows up a bomb...")
        elif action == "leave":
            print("you go to get up and leave and that’s when he yells at you that wee will all go home.")
        else:
            print("That is not a valid choice. You waited to long and the man says you know too much. He gets up and blows up the plane after yelling I’m coming home.")
    
    else:
        print("That is not a valid choice. You waited to long and the man gets up along with 4 other passenger’s and pulls out a gun and aims it at you while the others pull out guns and bombs, and then detonate the bombs...")

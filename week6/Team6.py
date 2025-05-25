Age_check = int(input("What is the age of the first rider? "))
Height_check = int(input("What is the height of the first rider? "))

if Age_check >= 12 and Age_check < 18:
    gold = input("Does this rider have a golden passport (yes/no)? ")

Rider_2 = input("Is there a second rider (yes/no)? ")

if Rider_2.lower() == "yes":
    Age_check2 = int(input("What is the age of the second rider? "))
    Height_check2 = int(input("What is the height of the second rider? "))

    if Age_check2 >= 12 and Age_check2 < 18:
        gold2 = input("Does this rider have a golden passport (yes/no)? ")

    if Height_check2 < 36 or Height_check2 < 36:
        can_ride = False
    else:
        if Age_check >= 18 or Age_check2 >= 18 or gold.lower() == "yes" or gold2.lower() == "yes":
            can_ride = True
        else:
            if Age_check >= 12 and Height_check >= 52 and Age_check2 >= 12 and Height_check2 >= 52:
                can_ride = True
            elif (Age_check >= 16 and Age_check2 >= 14) or (Age_check >= 14 and Age_check2 >= 16):
                can_ride = True
            else:
                can_ride = False
else:
    if (Age_check >= 18 or gold.lower() == "yes") and Height_check >= 62:
        can_ride = True
    else:
        can_ride = False
if can_ride:
    print("You may get on the ride.Welcome!Please be safe and have fun!")
else:
    print("Sorry,you may not ride at this time.")
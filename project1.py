name=input("Enter your name=")
print("Hello," + name + ", Welcome to my game!")

should_we_play=input("Do you want to play?")
play=should_we_play.lower()=="yes" or should_we_play.lower()=="YES" or should_we_play.lower()=="y" or should_we_play.lower()=="Y"

if play==True:
    print("Great! Let's play!")

    weapon=input("Choose a weapon (sword/axe)")
    
    
    direction=input("Do you want to go 'left' or 'right'?")
    if direction.lower()=="left":
        print("Okay we went left")

    elif direction.lower()=="right":
        print("Okay we went right")
        choice=input("You see a house and a river, which one do you go to? Type 'house' or 'river'")
        if choice=="river" and weapon.lower()=="sword":
            print("You got eaten by an alligator, you lose!")
        else:
            print("You go to the house and find a treasure, you win!")
    else:
        print("Invalid direction, you lose!")

else:
    print("No problem, maybe next time!")

from random import randint

def roll_dice():
    roll = True
    while roll:
        choice=str(input("Enter your choice(y/n): ")).strip().lower()
        if choice.lower() == "y":
            diceA = randint(1,6)
            diceB = randint(1,6)
            print(f"Your dice: {(diceA,diceB)}")
        elif choice.lower() == "n" : 
            roll = False 
            print(f"Thanks for playing")
            break
        else:
            roll = False 
            print(f"Invalid choice!")
            break 

roll_dice()


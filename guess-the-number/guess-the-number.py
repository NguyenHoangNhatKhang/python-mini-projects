def guess_the_number(): 
    import random 
    # number = 0

    def random_number(): 
        return random.randint(1,100)
    def want_to_guess(choices): 
        number = random_number()
        attempts = 10
        while attempts > 0 :
            if choices == "easy":  
                guess = int(input(f"You have {attempts} attempts to get the number"
                                "Make a guess: "))
                if guess > number :
                    attempts -= 1 
                    print("Too high")
                elif guess < number : 
                    attempts -=1
                    print("Too low")
                else: 
                    print(f"You got it - The answer was {number}") 
                    attempts = 0 
                    break
            elif choices == "hard": 
                attempts = 5 
                guess = int(input(f"You have {attempts} attempts to get the number"
                                "Make a guess: "))
                if guess > number :
                    attempts -= 1 
                    print("Too high")
                elif guess < number : 
                    attempts -=1 
                    print("Too low")
                else: 
                    print(f"You got it - The answer was {number}") 
                    attempts = 0
                    break 
                
    is_game_over = False 
    while not is_game_over: 
        choice = input("Welcome to the Number Guessing Game!" 
                    "I'm thinking of a number between 1 and 100"
                    "Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
        print(want_to_guess(choice))

guess_the_number()

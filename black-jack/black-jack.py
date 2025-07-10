cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ascii_art = r"""
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      '------'                           |__/
"""


player_card = []
computer_card = []
player_score = 0
computer_score = 0 
import random 
def ascii():
    print(ascii_art)
def computer():
    return random.choices(cards, k=2)
def player():
    return random.choices(cards,k=2)
def cancel():
    return "-----THANKS FOR PLAYING-----"
def hit_another_card():
    return random.choices(cards,k=1)
play_card = True
while play_card:
    ascii()
    choice = input("Do you want to play a game of BlackJack? Type `y` or `n`: ").lower().strip()
    if choice == "y":
        player_card = []
        computer_card = []
        player_score = 0
        computer_score = 0
        result = ""

        computer_card = computer()
        player_card = player()
        if 11 in computer_card and 10 in computer_card:
            result = f"{computer_card} BLACKJACK YOU LOST"
        elif 11 in player_card and 10 in player_card:
            result = f"{player_card} BLACKJACK YOU WIN"
        player_score = sum(player_card)
        computer_score = sum(computer_card)
        print(f"Computer first card: {computer_card[0]}")
        if player_score > 21 and 11 in player_card:
            player_card[player_card.index(11)] = 1 
        hit_another_card_1 = input(f"Your cards: {player_card} Do you want to pick up an extra card?:").lower().strip()
        while "y" in hit_another_card_1: 
            player_card.append(hit_another_card()[0])
            player_score = sum(player_card)
            print(f"YOUR CARDS {player_card}")
            if player_score > 21:
                print(f"You went over 21! Your score is {player_score} → GAME OVER")
                break
            hit_another_card_1 = input(f"Your cards: {player_card} Do you want to pick up an extra card?:").lower().strip()
        else: 
            print(f"Your cards are {player_card} and Your score is {player_score}")

        while computer_score > 21 and 11 in computer_card:
            computer_card[computer_card.index(11)] = 1 
            computer_score = sum(computer_card)
            print(f"Computer first card: {computer_card[0]}")
            if computer_score > 21 : 
                break 
    

        if player_score <= 21 and player_score > computer_score:
            result = f"{player_score} > {computer_score} YOU ARE THE WINNER"
            
        elif player_score <= 21 and player_score == computer_score: 
            result = f"{player_score} vs {computer_score} are equal. ENDS UP IN DRAW"
            
        elif player_score <= 21 and computer_score <= 21 and computer_score > player_score:
            result = f"{player_score} vs {computer_score} YOU LOST"
            
        else:
            result = f"Something unexpected happened. Your score: {player_score}, Computer: {computer_score}"
            

        print(result)   


            

    else: 
        play_card = False 
        print(cancel())
    
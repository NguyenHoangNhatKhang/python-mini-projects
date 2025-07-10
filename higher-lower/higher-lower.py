from HIGHER import ascii_art, ascii_vs_art
from data import data 
import random 
score = 0
account_a = random.choice(data) 
account_b = random.choice(data)
if account_a == account_b : 
    account_b = random.choice(data)
print(ascii_art)
def check_amswers(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        # if user_guess == "a":
        #     return True 
        # else : 
        #     return False 
        return user_guess == "a"
    else: 
        return user_guess == "b"
def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_ctr = account["country"]
    return f"{account_name}, a {account_descr} from {account_ctr}"

print(f"compare a {format_data(account_a)}")
print(ascii_vs_art)
print(f"compare B {format_data(account_b)}")


guess = input("Who has more followers: ").lower().strip()

a_followers_count = account_a["follower_count"]
b_followers_count = account_b["follower_count"]

is_correct =  check_amswers(guess,a_followers_count,b_followers_count)
if is_correct:
    print(f"You are right current score {score}")
else : 
    print(f"You are wrong final score {score}")
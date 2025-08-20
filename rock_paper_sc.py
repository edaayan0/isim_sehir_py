import random

user_score=0
comp_score=0

for i in range(3):
    user = input("rock paper scissors?: ")
    actions = ["rock", "paper", "scissors"]
    comp = random.choice(actions)
    print(f"\n {user} X {comp}\n")
    if comp == user:
        print("YOU 0-0 COMPUTER")
    elif comp == "rock":
        if user == "paper":
            user_score += 1
            print(f"\nYOU {user_score} - {comp_score} COMPUTER\n")

        else:
            comp_score += 1
            print(f"\nYOU {user_score} - {comp_score} COMPUTER\n")
    elif comp == "paper":
        if user == "scissors":
            user_score += 1
            print(f"\nYOU {user_score} - {comp_score} COMPUTER\n")
        else:
            comp_score += 1
            print(f"\nYOU {user_score} - {comp_score} COMPUTER\n")
    elif comp == "scissors":
        if user == "rock":
            user_score += 1
            print(f"\nYOU {user_score} - {comp_score} COMPUTER\n")
        else:
            comp_score += 1
            print(f"\nYOU {user_score} - {comp_score} COMPUTER\n")



if user_score > comp_score:
    print("\033[32mYOU WON\033[0m")
elif user_score < comp_score:
    print("\033[31mCOMPUTER WON\033[0m")
else:
    print("\033[34mA DRAW\033[0m")







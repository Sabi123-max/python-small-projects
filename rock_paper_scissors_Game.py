import random
def get_choice():
    first = input("Please enter your choic from tock paper scisors: ")
    options = ["paper", "scissors", "rock"]
    second = random.choice(options)
    choice = {"first": first, "second": second}
    return choice

def game_check(first, second):
    if first == second:
        print("it is a tie")
    elif (first == "paper" and second == "rock") or (first == "rock" and second == "scissors") or (first == "scissor" and second == "paper") :
        print("it is a win")
    else:
        print("it is a lose")
choice = get_choice()
print(choice)
result = game_check(choice["first"], choice["second"])
print(result)
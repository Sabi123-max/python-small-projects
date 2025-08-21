guess = input("guess the word you have 3 tries \n try1 ").lower()
tries = 1
if guess == "python":
    print("you guessed the word python")
while guess != "python":
    tries += 1
    guess = input(f"try {tries} ")
    if tries == 3:
        print("Oops the word was python")
        break

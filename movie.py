from itertools import count
import  random
movies = ["godzilla", "dracula", "frozen"]
print(movies[0])
print(movies[-1])
movies[1] = "super"
movies.append("nari")
print(movies)

animals = ["cat", "dog", "fish"]
print(animals)
print(animals[2])
animals[0] = "lion"
animals.append("pig")
animals.append("hen")
print(animals)
for animal in animals:
    print(animal)

for number in range(1,6):
    print(number)
count = 0
while count < 5:
    print("hello")
    count += 1

guess = int(input("Enter a number between 1 and 10: "))
random_number = random.randint(1, 10)
print(random_number)
count = 0
while guess != random_number:
    if guess >= 1 and guess < 5:
        print("Too low!")
    else:
        print("Too high!")

    guess = int(input("Guess again: "))
    count += 1



print("You guessed right!")
print(f"you have guessed {count} times")

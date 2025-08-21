guess = int(input("Enter a number between 1 and 10:\n "))
print(f" the multiplication table of {guess}")
for number in range(1, 11):
    multiplication = number * guess
    print(f" {number} x {guess} = {multiplication}")

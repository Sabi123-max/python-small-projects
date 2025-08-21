for number in range(10, 0, -1):
    print(number)
hey = input("do you wnat to continue? (y/n) ")
count = 1
while(hey != "y"):
    hey = input("do you wnat to continue? (y/n) ")
    count += 1
    if(count == 3):
        print("you have hit the limit of 3 !")
        break
print("great lets go")
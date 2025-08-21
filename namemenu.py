print("welcome to name manager")
print("""1.for adding name
2.for removing name
3.for viewing names
4.quit""")
choice = int(input("enter your choice: "))
names = []
while choice < 5:
    if choice == 1:
        add = input("enter the name to add: ")
        names.append(add)
        choice = int(input("enter your choice: "))
    elif choice == 2:
        rmv = input("enter the name to remove: ")
        names.remove(rmv)
        choice = int(input("enter your choice: "))
    elif choice == 3:
        print(names)
        choice = int(input("enter your choice: "))
    else:
        quit()

if choice > 4:
    print("please enter a number between 1 and 4")
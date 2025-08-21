names = ["Alice", "Bob", "Charlie"]
names.insert(3, "ramesh")
askname = input("please enter your name:")
names.append(askname)
names.sort()
names.remove("Bob")
if askname in names:
    print(f"{askname} already exist")
if askname in names:
    names.remove(askname)
for name in names:
    print("hello", name)
    if name.lower() == "sabik":
        print("welcome back sabik")

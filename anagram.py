ls = {}
words = input("Enter word: ").split()
for word in words:
    key = "".join(sorted(word))
    if key in ls:
        ls[key].append(word)
    else:
        ls[key] = [word]
sorted_group = sorted(ls.values(), key=lambda x: (-len(x),x))

for i,group in enumerate(sorted_group,start=1):
    print(f"{i}: {" ".join(group)}")

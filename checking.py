
dicta = {}
word = input("input: ").split(" ")
print(word)
for i in word:
    if i in dicta:
        dicta[i] += 1
    else:
        dicta[i] = 1

def get_choice(student):
    return -dicta[student],student

for key in sorted(dicta,key=get_choice):
    print(f"{key}:{dicta[key]}")



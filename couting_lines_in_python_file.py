import sys

def main():
    try:
        if len(sys.argv) == 2:
            if ".py" in sys.argv[1]:
                result = fileopen(sys.argv[1])
                print(result)
            else:
                sys.exit("Not a python file")
        elif len(sys.argv) < 2:
            sys.exit("Too few argument")
        else:
            sys.exit("Too many argument")
    except FileNotFoundError:
        sys.exit("File does not exist")

def fileopen(f):
    with open(f,"r") as file:
        i = 0
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith("#"):
                continue
            i = i + 1
        return i

main()

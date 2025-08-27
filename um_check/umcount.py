import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"[\s?,]um$|[\s?,]um[\s?,.]|(?:^um)|^Um|^um\."
    if mathch := re.findall(pattern, s):
        return len(mathch)
    else:
        return 0

...


if __name__ == "__main__":
    main()
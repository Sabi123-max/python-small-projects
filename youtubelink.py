import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    group=[]
    if s[0:7] == "<iframe":
        pattern = r"https?://(?:\w+\.)?youtube(?:\.com|\.edu)/\w+/(\w+)"
        match = re.findall(pattern, s)
        if match:

            result = f"https://youtu.be/{match[0]}"
        else:
            return None

        if match:
             return result
        else:
             return None
    else:
        return None




if __name__ == "__main__":
    main()
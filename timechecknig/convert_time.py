import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    pattern = r"^(1[0-2]|[1-9])(\:([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(\:([0-5][0-9]))? (AM|PM)$"
    match = re.search(pattern, s)
    if not match:
        raise ValueError("ValueError")
    firsthour = match.group(1)
    firstminute = match.group(3)
    firstmerdian = match.group(4)
    secondhour = match.group(5)
    secondminute = match.group(7)
    secondmerdian = match.group(8)



    if "AM" in firstmerdian:
        if firsthour == "12":
            firsthour = "00"
            if firstminute and not secondminute:
                final = f"{firsthour}:{firstminute} to {secondhour}:00"
            elif secondminute and not firstminute:
                final = f"{firsthour}:00 to {secondhour}:{secondminute}"
            elif firstminute and secondminute:
                final = f"{firsthour}:{firstminute} to {secondhour}:{secondminute}"
            else:
                final = f"{firsthour}:00 to {secondhour}:00"
            return final
        secondhour = int(secondhour) + 12
        if int(firsthour) < 10 :
            firsthour = "0" + str(firsthour)
        if int(secondhour) < 10 :
            secondhour = "0" + str(secondhour)
        if firstminute and not secondminute:
            final = f"{firsthour}:{firstminute} to {secondhour}:00"
        elif secondminute and not firstminute:
            final = f"{firsthour}:00 to {secondhour}:{secondminute}"
        elif firstminute and secondminute:
            final = f"{firsthour}:{firstminute} to {secondhour}:{secondminute}"
        else:
            final = f"{firsthour}:00 to {secondhour}:00"
        return final
    elif "PM" in firstmerdian:
        if secondhour == "12":
            secondhour = "00"
            if firstminute and not secondminute:
                final = f"{firsthour}:{firstminute} to {secondhour}:00"
            elif secondminute and not firstminute:
                final = f"{firsthour}:00 to {secondhour}:{secondminute}"
            elif firstminute and secondminute:
                final = f"{firsthour}:{firstminute} to {secondhour}:{secondminute}"
            else:
                final = f"{firsthour}:00 to {secondhour}:00"
            return final
        firsthour = int(firsthour) + 12
        if int(firsthour) < 10 :
            firsthour = "0" + str(firsthour)
        if int(secondhour) < 10 :
            secondhour = "0" + str(secondhour)
        if firstminute and not secondminute:
            final = f"{firsthour}:{firstminute} to {secondhour}:00"
        elif secondminute and not firstminute:
            final = f"{firsthour}:00 to {secondhour}:{secondminute}"
        elif firstminute and secondminute:
            final = f"{firsthour}:{firstminute} to {secondhour}:{secondminute}"
        else:
            final = f"{firsthour}:00 to {secondhour}:00"
        return final
    else:
        return None


if __name__ == "__main__":
    main()
from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    birthdate = input("Date of Birth: ").strip()
    try:
        dob = date.fromisoformat(birthdate)
    except ValueError:
        sys.exit("Invalid")

    print(minutes_in_words(dob))

def minutes_in_words(dob):
    today = date.today()
    diff = today - dob
    minutes = diff.days * 24 * 60
    words = p.number_to_words(minutes, andword="").capitalize()
    return f"{words} minutes"

if __name__ == "__main__":
    main()

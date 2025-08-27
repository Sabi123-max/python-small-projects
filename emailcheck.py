from validator_collection import validators

value = input("input: ")


try:
    email_address = validators.email(value, allow_empty=True)
    print("Valid")

except ValueError:
     print("Invalid")

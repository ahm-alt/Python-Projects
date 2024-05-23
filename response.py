from validator_collection import is_email

def main():
    email = input("What's your email address? ")
    if is_email(email):
        print("Valid")
    else:
        print("Invalid")
main()
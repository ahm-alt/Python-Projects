def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):


    if not s[0:2].isalpha():
        return False

    for i in range(len(s)):
        if s[i] in [" ", ".", ",", "?", "!", ":"]:
            return False

    for i in range(len(s)):
        if s[i].isnumeric():
            if not s[i:len(s)].isnumeric() or s[i] == '0':
                return False
            break
    if 2 <= len(s) <= 6:
        return True
    return False



main()

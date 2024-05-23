import inflect

def main():
    p = inflect.engine()
    lname = []
    while True:
        try:
            name = input("Name: ")
            lname.append(name)
        except EOFError:
            print()
            break
    mylist = p.join(lname)
    print("Adieu, adieu, to " + mylist)
main()
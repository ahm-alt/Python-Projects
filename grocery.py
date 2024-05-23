def main():
    glist = dict()
    while True:
        try:
            item = input("").upper()
            if item not in glist:
                glist[item] = 1

            else:
                glist[item] += 1
        except EOFError:
            print("")
            break
    #del glist["APPLE"]
    while True:
        if not glist:
            break
        temp = "z"
        for i in glist:
            if i < temp:
                temp = i
        print(f"{glist[temp]} {temp}")
        del glist[temp]

main()


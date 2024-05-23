def main():
    while True:
        date = input("Date: ")
        if check(date):
            break

def check(date):
    months = [
        "january",
        "february",
        "march",
        "april",
        "may",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december"
    ]
    try:
        m, d, y = date.split("/")
        day = int(d)
        mon = int(m)
    except ValueError:
        pass
    else:
        if mon <= 12 and day <= 31:
            print(f"{y:>04}-{m:>02}-{d:>02}")
            return True

    try:
        md, y = date.split(", ")
        m, d = md.split(" ")
        m = m.lower()
        day = int(d)
    except ValueError:
        return False

    for i in months:
        if m == i and day <= 31:
            n = months.index(i) + 1
            s = f"{n}"
            print(f"{y:>04}-{s:>02}-{d:>02}")
            return True
    return False
main()
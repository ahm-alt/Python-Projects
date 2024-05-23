from datetime import date, timedelta
import inflect, sys,re


def main():
    dte = input("Date of Birth: ")
    if match := re.search(r"[0-9]{4}-((0[0-9])|1[0-2])-(([0-2][0-9])|30)", dte):
        print(convert(dte).capitalize())
    else:
        sys.exit("Invalid date")

def convert(dte):
    p = inflect.engine()
    d = date.fromisoformat(dte)
    x = d.today() - d
    return f'{p.number_to_words(x.days * 24 * 60, andword="")} minutes'


if __name__ == "__main__":
    main()
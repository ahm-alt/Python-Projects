from sys import exit, argv
import csv
import tabulate

def main():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    if len(argv) > 2:
        exit("Too many command-line arguments")
    if ".csv" not in argv[1]:
        exit("Not a Python file")
    try:
        file = open(argv[1])
    except FileNotFoundError:
        exit("File does not exist")

    print(convert(file))


def convert(file):
    reader = csv.DictReader(file)
    p = argv[1].removesuffix('.csv').capitalize()
    pizza = f"{p} Pizza"
    table = []
    for row in reader:
        table.append([row[pizza], row["Small"], row["Large"]])
    headers = [pizza, "Small", "Large"]
    return tabulate.tabulate(table, headers, tablefmt="grid")
main()
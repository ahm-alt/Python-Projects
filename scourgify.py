from sys import exit, argv
import csv

def main():
    if len(argv) < 3:
        exit("Too few command-line arguments")
    if len(argv) > 3:
        exit("Too many command-line arguments")
    if ".csv" not in argv[1] or ".csv" not in argv[2]:
        exit("Not a csv file")
    try:
        file = open(argv[1])
    except FileNotFoundError:
        exit("Could not read", argv[1])

    reader = csv.DictReader(file)
    dicts = []
    for row in reader:
        last, first = row["name"].split(", ")
        dicts.append({"first":first, "last":last, "house":row["house"]})
    file.close()
    with open(argv[2], "w") as file2:
        writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for ldict in dicts:
            writer.writerow(ldict)
main()
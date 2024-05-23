from sys import exit, argv

def main():
    if len(argv) < 2:
        exit("Too few command-line arguments")
    if len(argv) > 2:
        exit("Too many command-line arguments")
    if ".py" not in argv[1]:
        exit("Not a Python file")
    try:
        file = open(argv[1])
    except FileNotFoundError:
        exit("File does not exist")

    print(count_line(file))

def count_line(file):
    no_line = 0
    for line in file:
        line = line
        # not line.startswith("#") and
        n = "\n"
        if not line.lstrip().startswith("#") and line.strip() != "" :
            no_line += 1

    return no_line
main()
from sys import argv, exit
from random import choice
from pyfiglet import Figlet

def main():
    figlet = Figlet()
    if len(argv) == 3:
        if argv[1] not in ["-f", "--font"] or argv[2] not in figlet.getFonts():
            exit("Invalid usage")
        figlet.setFont(font=argv[2])

    elif len(argv) == 1:
        x = choice(figlet.getFonts())
        figlet.setFont(font=x)
    else:
        exit("Invalid usage")

    text = input("Input: ")
    print(figlet.renderText(text))

main()

from sys import exit
import emoji
def main():
    em = input("Input: ")

    if "_"  in em:
        print("Output: " + emoji.emojize(em))
    else:
        print("Output: " + emoji.emojize(em, language="alias"))

main()
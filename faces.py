def main():
    words = input()
    words = convert(words)
    print(words)

def convert(words):
    #if ":)" in words:
    words = words.replace(":)", "🙂")
    #elif ":(" in words:
    words = words.replace(":(", "🙁")
    return words
main()
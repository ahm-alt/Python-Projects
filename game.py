import random
from sys import exit

def main():
    level = get_postive("Level: ")
    rand = random.randint(1, level)
    guess = get_postive("Guess: ")
    if guess < rand:
        print("Too small!")
    elif guess > rand:
        print("Too large!")
    else:
        print("Just right!")
        exit()


def get_postive(s):
    while True:
        post = input(s)
        try:
            post = int(post)
        except ValueError:
            pass
        else:
            if post > 0:
                return post
main()

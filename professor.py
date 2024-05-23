import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tresult = x + y

        tries = 0
        while True:
            try:
                result = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if result == tresult:
                    score += 1
                    break
            tries += 1
            print("EEE")
            if tries == 3:
                print(f"{x} + {y} = {tresult}")
                break
    print(f"Score: {score}")
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level in [1, 2, 3]:
                return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
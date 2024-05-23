def main():
    x = get_fract()
    print(conv_fract(x))

def get_fract():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            f = float(int(x) / int(y))
            if f > 1:
                return get_fract()
            return f
        except (ValueError, ZeroDivisionError):
            return get_fract()

def conv_fract(x):
    x *= 100
    if x <= 1:
        return "E"
    elif x >= 99:
        return "F"
    else:
        return f"{round(x)}%"

main()



def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 7 <= time <= 8:
        print("breakfast time")
    elif 18 <= time <= 19:
        print("dinner time")
    elif 12 <= time <= 13 :
        print("lunch time")

def convert(time):
    h, m = time.split(":")
    m = float(m) / 60
    time = int(h) + m
    return time


if __name__ == "__main__":
    main()

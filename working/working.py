import re
import sys


def main():
    print(convert(input("Hours: ")))




def convert(s):
    if match := re.search(r"^([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM) to ([0-9]|1[0-2]):?([0-5][0-9])? (AM|PM)$", s):
        h1, m1, p1, h2, m2, p2 = match.groups()
        h = {"h" : [h1, h2], "m" : [m1, m2], "p" : [p1, p2]}
        for i in [0, 1]:
            if not h["m"][i]:
                h["m"][i] = "00"
            if h["h"][i] == "12":
                h["h"][i] = f"{int(h['h'][i]) - 12}"
            if h["p"][i] == "PM":
                h["h"][i] = f"{int(h['h'][i]) + 12}"

        return f"{h['h'][0]:>02}:{h['m'][0]:>02} to {h['h'][1]:>02}:{h['m'][1]:>02}"

    raise ValueError



if __name__ == "__main__":
    main()
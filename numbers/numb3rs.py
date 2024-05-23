import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    sys.exit()


def validate(ip):
    #{3}[0-9][0-5]{0,2}
    #([0-9]|[0-9][0-9]|1[0-9][0-9]|2[0-5][0-5])
    check = re.search(r"^((1?[0-9]{1,2})\.|(2[0-4][0-9])\.|(25[0-5])\.){3}(1?[0-9]{1,2}|2[0-4][0-9]|25[0-5])$", ip)
    if check:
        return True
    return False
if __name__ == "__main__":
    main()
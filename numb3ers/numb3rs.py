import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def check_parts(parts):

    for item in parts:
        ip_adress_part = int(item)
        if ip_adress_part < 0 or ip_adress_part > 255:
            return False

    return True


def validate(ip):
    ip_parts = ip.split(".")

    if len(ip_parts) != 4:
        return False
    elif check_parts(ip_parts) == True:
        return True
    else:
        return False



if __name__ == "__main__":
    main()


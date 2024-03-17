import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    try:
        matches = re.search(r"([0-9]?[0-9]+)?:?([0-5]?[0-9]+)?\s+(AM|PM)+\sto\s([0-9]?[0-9]+)?:?([0-5]?[0-9]+)?\s+(AM|PM)+", s)
        matches = matches.groups()
        matches_list = list(matches)

        matches_list[0] = int(matches_list[0])
        matches_list[3] = int(matches_list[3])

        if matches_list[1] != None:
            matches_list[1] = int(matches_list[1])

        if matches_list[4] != None:
            matches_list[4] = int(matches_list[4])

        if matches_list[0] < 0 or matches_list[0] > 12:
            raise ValueError

        if matches_list[3] < 0 or matches_list[3] > 12:
            raise ValueError

        if matches_list[1] is not None and (matches_list[1] < 0 or matches_list[1] > 59):
            raise ValueError

        if matches_list[4] is not None and (matches_list[4] < 0 or matches_list[4] > 59):
            raise ValueError

        if matches_list[0] == 12 and matches_list[2] == "AM":
            matches_list[0] = 0
        elif matches_list[0] == 12 and matches_list[2] == "PM":
            matches_list[0] = 12
        elif matches_list[2] == "PM":
            matches_list[0] += 12


        if matches_list[3] == 12 and matches_list[5] == "PM":
            matches_list[3] = 12
        elif matches_list[5] == "PM":
            matches_list[3] += 12


        if matches_list[1] != None or matches_list[4] != None:
            return f"{matches_list[0]:02}:{matches_list[1]:02} to {matches_list[3]:02}:{matches_list[4]:02}"
        elif matches_list[1] == None or matches_list[4] == None:
            return f"{matches_list[0]:02}:00 to {matches_list[3]:02}:00"


    except (ValueError, AttributeError):
        raise ValueError

if __name__ == "__main__":
    main()

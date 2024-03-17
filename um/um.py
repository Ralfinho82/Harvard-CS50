import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    match_count = 0

    matches = re.findall(r"\w*", s)
    print(matches)

    for m in matches:
        match m:
            case "um" | "Um" | "UM" | "uM":
                match_count += 1


    return match_count


if __name__ == "__main__":
    main()
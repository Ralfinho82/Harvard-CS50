import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        if ('src="https://www.youtube' or 'src="http://www.youtube' in s) and '<iframe' in s:
            matches = re.search(r"(?:https?://)?(?:www\.)?(?:youtube)?\.com/embed/(\w+)", s)

            matches = "https://youtu.be/" + matches.group(1)
            return matches

        else:
            return None
    except AttributeError:
        return None


if __name__ == "__main__":
    main()


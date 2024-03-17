import sys
from pyfiglet import Figlet
import random


def main():

    figlet = Figlet()
    fonts = figlet.getFonts()


    if len(sys.argv) == 1:
        user_input = input("Input: ")
        figlet.setFont(font = random.choice(fonts))
        print("Output:")
        print(figlet.renderText(user_input))

    elif len(sys.argv) == 3:
        if sys.argv[1] != "-f" and sys.argv[1] != "--font":
            sys.exit("Invalid usage")
        elif sys.argv[2] not in fonts:
            sys.exit("Invalid usage")
        else:
            user_input = input("Input: ")
            figlet.setFont(font = sys.argv[2])
            print("Output:")
            print(figlet.renderText(user_input))

    else:
        sys.exit("Invalid usage")



if __name__ == "__main__":
    main()
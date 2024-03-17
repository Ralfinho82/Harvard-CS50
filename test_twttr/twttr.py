def main():
    user_input = input("Please enter the expression. ")
    print(shorten(user_input))


def shorten(word):
    output = ""
    for c in word:

        match c:
            case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
                output += ""
            case _:
                output += c

    return output


if __name__ == "__main__":
    main()


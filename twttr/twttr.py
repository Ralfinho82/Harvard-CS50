def main():
    user_input = input("Please enter the expression. ")
    convert(user_input)

def convert(user_input):
    output = ""
    for c in user_input:

        match c:
            case "a" | "e" | "i" | "o" | "u" | "A" | "E" | "I" | "O" | "U":
                output += ""
            case _:
                output += c

    print(output)


main ()
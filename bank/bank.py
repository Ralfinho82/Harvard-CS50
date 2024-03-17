def main():
    greeting = str(input("Please input your greeting. ")).lower().strip()

    position_greeting = greeting.find("hello")
    position_greeting_two = greeting.find("h")


    if position_greeting == 0:
        print("$0")
    elif position_greeting_two == 0:
        print("$20")
    else:
        print("$100")


main()
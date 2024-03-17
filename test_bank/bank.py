def main():
    user_input = str(input("Please input your greeting. "))
    print(f"${value(user_input)}")


def value(greeting):

    greeting = greeting.lower().strip()
    position_greeting = greeting.find("hello")
    position_greeting_two = greeting.find("h")

    if position_greeting == 0:
        return 0
    elif position_greeting_two == 0:
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()


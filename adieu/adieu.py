def main():
    adieu("Name: ")

def adieu(prompt):
    names_list = []

    while True:
        try:
            name = input(prompt)
            names_list.append(name)
            print(names_list)
        except (EOFError):
            break

    if len(names_list) == 1:
        print(f"Adieu, adieu, to {names_list[0]}")
    elif len(names_list) == 2:
        print(f"Adieu, adieu, to {names_list[0]} and {names_list[1]}")
    elif len(names_list) > 2:
        print(f"Adieu, adieu, to {', '.join(names_list[:-1])}, and {names_list[-1]}")


if __name__ == "__main__":
    main()
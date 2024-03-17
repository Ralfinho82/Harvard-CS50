def main():
    result = get_fraction("Fraction: ")
    if result is not None:
        if result <= 1:
            print("E")
        elif result >= 99:
            print("F")
        else:
            print(str(result) + "%")

def get_fraction(prompt):
    while True:
        try:
            x, y = input(prompt).split("/")
            x = int(x)
            y = int(y)
            if x > y:
                print("Fraction: ")
            else:
                result = round((x / y) * 100)
                return result
        except (ValueError, ZeroDivisionError):
            pass


main()
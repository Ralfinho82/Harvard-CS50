def main():
    result = convert(input("Fraction: "))
    formatted_result = gauge(result)
    print(formatted_result)


def convert(fraction):
    try:
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        result = x / y
        result = round(result * 100)
        return result

    except (ValueError, ZeroDivisionError):
        pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return str(percentage) + "%"


if __name__ == "__main__":
    main()


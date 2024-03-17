def main():
    expression = input("Please enter the mathematical expression. ")

    x, y, z = expression.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
        print(result)
    elif y == "-":
        result = x - z
        print(result)
    elif y == "*":
        result = x * z
        print(result)
    else:
        result = x / z
        print(result)

main ()
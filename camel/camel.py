def main():
    camel_case = input("Please enter the camelCaseExpression. ")
    convert(camel_case)

def convert(camel_case):
    snake_case = ""
    for c in camel_case:
        # print(c, end="")

        if c.isupper() == True:
            c = c.lower()
            snake_case += "_" + c

        else:
            snake_case += c

    print(snake_case)


main ()
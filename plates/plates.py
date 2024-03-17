def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if s[0:2].isalpha() == False:
        return False

    elif len(s) < 2 or len(s) > 6:
        return False

    elif s[len(s) - 1].isalpha() == True and s[len(s) - 2].isalpha() == False or s[len(s) - 3].isalpha() == False:
        return False

    elif s[2] == "0":
        return False

    elif s.isalnum() == False:
        return False

    else:
        return True


main()
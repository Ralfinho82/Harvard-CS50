import validators

def main():
    print(check(input("What's your email address? ")))


def check(s):
    try:
        result = validators.email(s)
        if result == True:
            return "Valid"
        else:
            return "Invalid"
    except ValidationError:
        return "Invalid"



if __name__ == "__main__":
    main()


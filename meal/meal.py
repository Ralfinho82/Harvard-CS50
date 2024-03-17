def main():
    user_time = input("Please enter the current time. ")
    time = convert(user_time)

    if time >= 7.0 and time <= 8.0:
        print("breakfast time")
    elif time >= 12.0 and time <= 13.0:
        print("lunch time")
    elif time >= 18.0 and time <= 19.0:
        print("dinner time")


def convert(user_time):
    hours, minutes = user_time.split(":")
    minutes = float(minutes) / 60
    decimal_time = float(hours) + minutes
    return(decimal_time)


if __name__ == "__main__":
    main()

def main():
    amount_due = 50

    while amount_due > 0:
        coin_value = int(input("Insert Coin: "))

        if coin_value == 25:
            amount_due -= 25
            if amount_due < 0:
                change = amount_due * -1
                print("Change Owed: " + str(change))
            elif amount_due > 0:
                print("Amount Due: " + str(amount_due))
            else:
                print("Change Owed: " + str(amount_due))

        elif coin_value == 10:
            amount_due -= 10
            if amount_due < 0:
                change = amount_due * -1
                print("Change Owed: " + str(change))
            elif amount_due > 0:
                print("Amount Due: " + str(amount_due))
            else:
                print("Change Owed: " + str(amount_due))

        elif coin_value == 5:
            amount_due -= 5
            if amount_due < 0:
                change = amount_due * -1
                print("Change Owed: " + str(change))
            elif amount_due > 0:
                print("Amount Due: " + str(amount_due))
            else:
                print("Change Owed: " + str(amount_due))

        else:
            print("Amount Due: 50")
            coin_value = int(input("Insert Coin: "))

main()
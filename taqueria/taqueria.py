def main():
    price_list = menu("Item: ")

def menu(prompt):
    price_list = []
    while True:
        try:
            d = {
                "Baja Taco": 4.00,
                "Burrito": 7.50,
                "Bowl": 8.50,
                "Nachos": 11.00,
                "Quesadilla": 8.50,
                "Super Burrito": 8.50,
                "Super Quesadilla": 9.50,
                "Taco": 3.00,
                "Tortilla Salad": 8.00
            }

            item = input(prompt).title()
            if item in d:
                item_price = d.get(item)
                price_list.append(item_price)
                total_price = sum(price_list)
                formatted_total = "{:.2f}".format(total_price)
                print("Total: $" + formatted_total)
            else:
                print(prompt)
        except (KeyError):
            pass
        except (EOFError):
            break

main()
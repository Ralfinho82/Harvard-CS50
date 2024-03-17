def main():
    add_to_grocery_list()

def add_to_grocery_list():
    grocery_list = {}
    while True:
        try:
            item = input().upper()
            if item not in grocery_list:
                grocery_list[item] = 1
            else:
                grocery_list[item] += 1
        except (KeyError):
            pass
        except (EOFError):
            break


    grocery_list_keys = list(grocery_list.keys())
    grocery_list_keys.sort()
    grocery_list_sorted = {i: grocery_list[i] for i in grocery_list_keys}

    for key, value in grocery_list_sorted.items():
        print(f"{value} {key}")


main()


# wenn item im dictionary, dann hochzählen um 1 -> erledigt
# wenn item nicht im dictionary, dann item anlegen -> erledigt
# check ob input errors gecatcht werden müssen -> nein, alles kommt rein
# printoutput muss alphabetisch sortiert werden und die Zahlen müssen an erster Stelle stehen
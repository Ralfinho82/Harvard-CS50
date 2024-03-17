def main():
    fruit = input("Item: ").lower()

# Dictionary anlegen
    d = {
        "apple": "130",
        "avocado": "50",
        "banana": "110",
        "sweet cherries": "100",
        "pear": "100",
        "kiwifruit": "90"
    }
# Prüfen, ob der Key (die Frucht) vorhanden ist und Ausgabe der Kalorien



# If k is a str and d is a dict, you can check whether k is a key in d with code like:

    if fruit in d:
        print("Calories: " + d[fruit])
    else:
        print("")

main()
import sys
from tabulate import tabulate
import csv

def check_filename(filename):
    filename_parts = filename.split(".")
    if filename_parts[-1] == "csv":
        return True
    else:
        return False

def check_length(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    elif not check_filename(arguments[1]):
        sys.exit("Not a CSV file")
    else:
        print(pretty_print(arguments[1]))

def pretty_print(filename):
    try:

        pizzas = []
        if filename == "regular.csv":
            with open(filename) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                    pizzas.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
            print(tabulate(pizzas, headers="keys", tablefmt="grid"))

        elif filename == "sicilian.csv":
            with open(filename) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    print(row)
                    pizzas.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})
            print(tabulate(pizzas, headers="keys", tablefmt="grid"))
        else:
            raise FileNotFoundError

    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    check_length(sys.argv)

if __name__ == "__main__":
    main()
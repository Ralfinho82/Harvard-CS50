import sys
import csv


def check_filename(filename):
    filename_parts = filename.split(".")
    if filename_parts[-1] == "csv":
        return True
    else:
        return False


def check_length(arguments):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    elif not check_filename(arguments[1]):
        sys.exit("Not a CSV file")
    else:
        convert(arguments[1], arguments[2])


def split_name(full_name):
    parts = full_name.split()
    if len(parts) >= 2:
        last = parts[0]
        first = ' '.join(parts[1:])
    else:
        first = full_name
        last = ""
    return first, last


def clean_name(name):
    return name.replace('"', '').replace(',', '')


def convert(before_filename, after_filename):
    try:
        with open(before_filename, newline='') as input_file, open(after_filename, "w", newline='') as output_file:

            reader = csv.reader(input_file)
            writer = csv.writer(output_file)
            next(reader, None)

            writer.writerow(["first", "last", "house"])

            for row in reader:
                name = clean_name(row[0])
                house = row[1]
                first, last = split_name(name)
                writer.writerow([first, last, house])

    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    check_length(sys.argv)


if __name__ == "__main__":
    main()
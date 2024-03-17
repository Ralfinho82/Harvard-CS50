import sys

def check_filename(filename):
    filename_parts = filename.split(".")
    if filename_parts[-1] == "py":
        return True
    else:
        return False

def check_length(arguments):
    if len(arguments) < 2:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 2:
        sys.exit("Too many command-line arguments")
    elif not check_filename(arguments[1]):
        sys.exit("Not a Python file")
    else:
        print(count_lines(arguments[1]))

def count_lines(filename):
    try:
        line_counter = 0
        with open(filename) as file:
            for line in file:
                line = line.lstrip()
                if line and not line.startswith("#"):
                    line_counter += 1
        return line_counter
    except FileNotFoundError:
        sys.exit("File does not exist")

def main():
    check_length(sys.argv)

if __name__ == "__main__":
    main()
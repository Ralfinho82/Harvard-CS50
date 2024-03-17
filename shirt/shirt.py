import sys
from PIL import Image
from PIL import ImageOps


def check_filename(filename):
    filename_parts = filename.split(".")
    if filename_parts[-1] == "jpg".lower() or filename_parts[-1] == "jpeg".lower() or filename_parts[-1] == "png".lower():
        return True
    else:
        return False


def same_extension(file_1, file_2):
    filename_parts_1 = file_1.split(".")
    filename_parts_2 = file_2.split(".")
    if filename_parts_1[-1] == filename_parts_2[-1]:
        return True
    else:
        return False


def check_length(arguments):
    if len(arguments) < 3:
        sys.exit("Too few command-line arguments")
    elif len(arguments) > 3:
        sys.exit("Too many command-line arguments")
    elif not check_filename(arguments[1]):
        sys.exit("Invalid input")
    elif not same_extension(arguments[1], arguments[2]):
        sys.exit("Input and output have different extensions")
    else:
        create_shirt("shirt.png", arguments[1], arguments[2])


def create_shirt(base_file, input, output):
    try:
        image_base = Image.open(base_file)
        image_input = Image.open(input)
        image_fit = ImageOps.fit(image_input, (600, 600), bleed=0.0, centering=(0.5, 0.5))
        image_fit.paste(image_base, (0, 0, 600, 600), image_base)
        image_fit.save(output)
    except FileNotFoundError:
        sys.exit("File does not exist")


def main():
    check_length(sys.argv)


if __name__ == "__main__":
    main()
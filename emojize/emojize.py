import emoji

def main():
    user_input = input("Input: ")
    print(emoji.emojize("Output: " + user_input, language="en"))


main()
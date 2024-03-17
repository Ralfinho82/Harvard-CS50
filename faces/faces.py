def convert(text):
    text_1 = text.replace(":)", "🙂")
    print(text_1.replace(":(", "🙁"))

def main():
    convert(input("Please input something."))
    
main()
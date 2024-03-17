import random as r

def main():
    lvl = level("Level: ")
    game(lvl, "Guess: " )

def level(prompt):

    while True:
        try:
            level = int(input(prompt))
            if level > 0:
                return level
            else:
                continue
        except (ValueError, TypeError):
            pass

def game(n, prompt):

    result = r.randint(1, n)

    while True:
        try:
            guess = int(input(prompt))
            if result > guess:
                print("Too small!")
            elif result < guess:
                print("Too large!")
            else:
                print("Just right!")
                break
        except (ValueError, TypeError):
            pass


if __name__ == "__main__":
    main()
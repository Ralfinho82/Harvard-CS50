import random as r
import sys


def main():
    lvl = get_level()
    # problem(generate_integer(lvl), generate_integer(lvl))
    s = score(lvl)
    print(f"Score: {s}")


def score(lvl):
    problems_looked_at = 1
    score = 0
    while problems_looked_at <= 10:
        x = generate_integer(lvl)
        y = generate_integer(lvl)
        result = problem(x, y)
        if result == True:
            score += 1
            problems_looked_at += 1
        elif result == False:
            problems_looked_at += 1
    return score


def problem(x, y):
    attempts = 0

    while attempts < 3:
        try:
            user_input = int(input(f"{x} + {y} = "))
            solution = x + y
            if user_input == solution:
                return True
            else:
                attempts += 1
                print("EEE")
        except (ValueError, TypeError):
            attempts += 1
            print("EEE")
    print(f"{x} + {y} = {solution}")
    return False


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except:
            pass


def generate_integer(level):
    if level == 1:
        return r.randint(0, 9)
    elif level == 2:
        return r.randint(10, 99)
    elif level == 3:
        return r.randint(100, 999)
    else:
        raise ValueError

'''
def generate_problem(lvl):
    x = generate_integer(lvl)
    y = generate_integer(lvl)
    solution = x + y
    return x, y, solution
'''

if __name__ == "__main__":
    main()
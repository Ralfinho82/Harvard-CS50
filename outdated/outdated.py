def main():
    convert_date("Date: ")

def convert_date(prompt):
    while True:
        try:
            months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

            user_date = input(prompt).strip()

            if "/" in user_date:
                date = user_date.split("/")
                month = int(date[0])
                day = int(date[1])
                year = int(date[2])
                if day > 31:
                    user_date = input(prompt).strip()
                    continue
                if month > 12:
                    user_date = input(prompt).strip()
                    continue

                print(f"{year:04}-{month:02}-{day:02}")
                break

            elif " " in user_date:
                if "," not in user_date:
                    continue
                date = user_date.replace(",", "")
                date = date.split()
                day = int(date[1])
                if day > 31:
                    user_date = input(prompt).strip()
                    continue

                month_index = months.index(date[0])
                print(f"{date[2]}-{month_index + 1:02}-{day:02}", end="")
                break

            else:
                user_date = input(prompt).strip()

        except (ValueError, IndexError):
            pass

        except (EOFError):
            break


main()
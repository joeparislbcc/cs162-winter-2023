#! /usr/bin/env python3

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

while True:
    try:
        user_number = int(input("Please enter a number between 1 and 7: "))
    except ValueError:
        pass  # ignore the problem until it goes away
    else:
        if user_number not in range(1, 8):
            print("Sorry, that is not a number between 1 and 7.")
        else:
            print(week_days[user_number - 1])
            break

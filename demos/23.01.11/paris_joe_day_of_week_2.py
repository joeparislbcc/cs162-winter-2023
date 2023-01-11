#! /usr/bin/env python3

week_days = {
    "1": "Monday",
    "2": "Tuesday",
    "3": "Wednesday",
    "4": "Thursday",
    "5": "Friday",
    "6": "Saturday",
    "7": "Sunday",
}

while True:
    user_number = input("Please enter a number between 1 and 7: ")

    if user_number not in week_days.keys():
        print("Sorry, that is not a number between 1 and 7.")
    else:
        print(week_days[user_number])
        break

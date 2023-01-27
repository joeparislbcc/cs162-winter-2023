#!/usr/bin/env python3
"""Demo building dicts all the way down."""
import csv
import pprint
from typing import TextIO


def open_file() -> TextIO:
    """Return a handle to the input file."""
    while True:
        try:
            file_name = input("Enter a file name to open: ")
        try:
            # It would be better to use a context handler here BUT for the sake
            # of this assignment we are not. The following line will silence
            # Pylint's warning about the issue.
            #
            # pylint: disable=consider-using-with
            data_file = open(file_name, mode="r", encoding="UTF-8")
        except FileNotFoundError:
            print(f"{file_name} not found, please try again.")
        else:
            return data_file


def build_data_dict(in_file) -> dict[str, dict[str, dict[str, dict[str, str]]]]:
    """Build the dictionary containing the car data."""
    csv_reader = csv.DictReader(in_file)

    data: dict[str, dict[str, dict[str, dict[str, str]]]] = {}

    for row in csv_reader:
        # Make,Model,MPG,Cylinders,Displacement,Horsepower,Weight,Acceleration,ModelYear,Origin
        make = row["Make"]
        origin = row["Origin"]
        model = row["Model"]
        mpg = row["MPG"]
        cylinders = row["Cylinders"]
        displacement = row["Displacement"]
        horsepower = row["Horsepower"]
        weight = row["Weight"]
        acceleration = row["Acceleration"]
        model_year = row["ModelYear"]

        if make not in data:
            data[make] = {}

        if origin not in data[make]:
            data[make][origin] = {}

        if model not in data[make][origin]:
            data[make][origin][model] = {
                "mpg": mpg,
                "cylinders": cylinders,
                "displacement": displacement,
                "horsepower": horsepower,
                "weight": weight,
                "acceleration": acceleration,
                "model_year": model_year,
            }

    return data


def main():
    """Make it go."""
    file_handle = open_file()
    data = build_data_dict(file_handle)

    pprinter = pprint.PrettyPrinter(indent=2)
    pprinter.pprint(data)

    file_handle.close()


if __name__ == "__main__":
    main()

import csv
import sys
from datetime import datetime

from matplotlib import pyplot as plt

WELCOME_MESSAGE = """
Welcome to the Sitka Airport Weather Graph Display
Please select one of the following options:
1. Highs - Displays the highest temperature reading by day
2. Lows  - Displays the lowest temperature reading by day
3. Exit  - Quit the program
"""

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates and temperatures from this file.
    dates , highs , lows = [] , [] , []
    for row in reader:
        current_date = datetime.strptime(row[2] , '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
        low = int(row[6])
        lows.append(low)


def show_display(temp):
    fig , ax = plt.subplots()

    match temp:
        case "HIGHS":
            ax.plot(dates , highs , c='red')
            plt.title("Daily High Temperatures - 2018" , fontsize=24)
        case "LOWS":
            ax.plot(dates , lows , c='blue')
            plt.title("Daily Low Temperatures - 2018" , fontsize=24)

    plt.xlabel('' , fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)" , fontsize=16)
    plt.tick_params(axis='both' , which='major' , labelsize=16)
    plt.show()


def main():
    print(WELCOME_MESSAGE)
    while True:
        choice = input(">>").strip().upper()
        match choice:
            case "1" | "HIGHS":
                show_display("HIGHS")
                print("Graph closed...")
                print(WELCOME_MESSAGE)
            case "2" | "LOWS":
                show_display("LOWS")
                print("Graph closed...")
                print(WELCOME_MESSAGE)
            case "3" | "EXIT":
                print("\nThank you! Goodbye.")
                sys.exit()
            case _:
                print(f"Invalid option entered: {choice}. Please select a valid option...")
                print(WELCOME_MESSAGE)


if __name__ == "__main__":
    main()

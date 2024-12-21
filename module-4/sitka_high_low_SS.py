import csv
from datetime import datetime
import sys
from matplotlib import pyplot as plt

# Function to read the weather data from the file
def read_weather_data(filename):
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        # Get dates, high temperatures, and low temperatures from the file.
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            low = int(row[6])
            highs.append(high)
            lows.append(low)

    return dates, highs, lows

# Function to plot high temperatures
def plot_highs(dates, highs):
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red')
    ax.set_title("Daily High Temperatures - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Function to plot low temperatures
def plot_lows(dates, lows):
    fig, ax = plt.subplots()
    ax.plot(dates, lows, c='blue')
    ax.set_title("Daily Low Temperatures - 2018", fontsize=24)
    ax.set_xlabel('', fontsize=16)
    ax.set_ylabel("Temperature (F)", fontsize=16)
    fig.autofmt_xdate()
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()

# Main program logic
def main():
    filename = r'C:/School/Module 4/sitka_weather/sitka_weather_2018_simple.csv'

    # Read weather data
    dates, highs, lows = read_weather_data(filename)

    while True:
        # Display menu options
        print("\nWeather Data Menu:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")
        
        # Get user input
        choice = input("Please enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Plot high temperatures
            plot_highs(dates, highs)
        elif choice == '2':
            # Plot low temperatures
            plot_lows(dates, lows)
        elif choice == '3':
            # Exit message and terminate
            print("Exiting the program. Thank you for using the weather data viewer.")
            sys.exit()  # Exit the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
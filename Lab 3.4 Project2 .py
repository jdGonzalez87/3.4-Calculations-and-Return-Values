from datetime import datetime

# -----------------------------
# Conversion Function
# -----------------------------
def convertData(value, mode):
    """
    convertData(value, mode)
    value: numerical value to convert
    mode: 'temp', 'weight', or 'rain'
    returns: converted numerical value
    """
    if mode == "temp":      # Fahrenheit → Celsius
        return (value - 32) * 5/9
    elif mode == "weight":  # Pounds → Kilograms
        return value / 2.205
    elif mode == "rain":    # Inches → Centimeters
        return value * 2.54
    else:
        return None
# -----------------------------
# Input Function
# -----------------------------
def getInput(mode):
    """
    getInput(mode)
    mode: 'temp', 'weight', or 'rain'
    Asks user for number of entries, loops, converts, prints saved output.
    """
    print("How many entries are you inputting?")
    count = int(input())
    for i in range(count):
        print("Enter a date:")
        date = input()
        # Ask for correct value depending on mode
        if mode == "temp":
            print("Enter the highest temp for the inputted date:")
        elif mode == "weight":
            print("Enter the weight in pounds for the inputted date:")
        elif mode == "rain":
            print("Enter the rain amount in inches for the inputted date:")
        value = float(input())
        # -----------------------------------------
        # Calling convertData(value, mode)
        # Argument: numerical value
        # Expected return: converted numerical value
        # -----------------------------------------
        converted = convertData(value, mode)
        timestamp = datetime.now()
        print(f"The following was saved at {timestamp} :")
        print(f"{date},{value},{converted}")
# -----------------------------
# Main Program Menu
# -----------------------------
menu_options = [
    "1 Input Data",
    "2 View Current Data",
    "3 Generate Report"
]
print("Jaser3949's Spreadsheet Automation Menu")
print("Choose a number from the following options")
for option in menu_options:
    print(option)
choice = input()
valid_choices = ["1", "2", "3"]
if choice in valid_choices:
    print(f"You selected {choice} at {datetime.now()}")
    if choice == "1":
        # Choose which spreadsheet mode you want:
        # temp, weight, or rain
        print("Select data type from the following options:")
        data_types = ["1 Temperature", "2 Weight", "3 Rain"]
        for dt in data_types:
            print(dt)
        mode_choice = input()
        if mode_choice == "1":
            getInput("temp")
        elif mode_choice == "2":
            getInput("weight")
        elif mode_choice == "3":
            getInput("rain")
        else:
            print("Invalid data type selected.")
    else:
        print("Error: The chosen functionality is not implemented yet")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")

import random
import csv

# (Previous constants and dictionaries)

# Constants for the slots
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

# Number of rows and columns in the slot machine
ROWS = 3
COLS = 3

# Define the count of symbols in the slot machine and their corresponding values
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

# Function to check if the player wins and determine their winnings
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []

    # Check if the symbols match in the slot machine and calculate winnings
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)

    return winnings, winning_lines

# Function to create the slot machine with random symbols
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

# Function to print the slot machine to the console
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

# Function to prompt the player for the initial deposit
def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")

    return amount

# Function to prompt the player for the number of lines to bet on
def get_number_of_lines():
    while True:
        lines = input(
            "Enter the number of lines to bet on (1-" + str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number.")

    return lines

# Function to prompt the player for the bet amount on each line
def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

    return amount

# Function to handle the game logic and spinning the slot machine
def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(
                f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(
        f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)
    return winnings - total_bet

# Function to log player interactions to a CSV file

def log_player_interaction(filename, interaction):
        # Open the file in 'append' mode to add data without overwriting
    with open(filename, 'a', newline='') as file:
        # Create a CSV writer object
        writer = csv.writer(file)
        # Write the player interaction data as a row in the CSV file
        writer.writerow(interaction)

# Function to simulate spinning the slot machine
def spin(balance, log_filename):
    lines = get_number_of_lines()
    # Check balance and place bets
    while True:
        bet = get_bet()
        total_bet = bet * lines
        # Check if the total bet exceeds the balance
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines:", *winning_lines)

    # Log the interaction data
    interaction_data = [balance, lines, bet, total_bet, winnings, winning_lines]
    log_player_interaction(log_filename, interaction_data)

    return winnings - total_bet

# Main function to start the game
def main():
    # Collect the initial balance
    balance = deposit()
    log_filename = 'player_interactions.csv'

    # Play the game and log interactions
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance, log_filename)

    print(f"You left with ${balance}")

# Run the main function to start the game
main()



# pip install pandas
import pandas as pd

# Load data from the CSV file
data = pd.read_csv('player_interactions.csv', header=None, names=["Balance", "Lines", "Bet", "Total Bet", "Winnings", "Winning Lines"])

# Display the first few rows to understand the data structure
print("Data Preview:")
print(data.head())

# Calculate win rates and average bets
win_rates = (data['Winnings'] > 0).mean()
average_bet = data['Bet'].mean()

print("\nWin Rates:", win_rates)
print("Average Bet:", average_bet)

# Calculate the distribution of wins
wins_distribution = data['Winnings'].value_counts()
print("\nDistribution of Wins:")
print(wins_distribution)

# Install and load the necessary library
install.packages("readr")
library(readr)

# Load data from the CSV file
data <- read_csv("player_interactions.csv", col_names = c("Balance", "Lines", "Bet", "Total_Bet", "Winnings", "Winning_Lines"))

# Display the first few rows to understand the data structure
print("Data Preview:")
print(head(data))

# Calculate win rates and average bets
win_rates <- mean(data$Winnings > 0)
average_bet <- mean(data$Bet)

print("Win Rates:", win_rates)
print("Average Bet:", average_bet)

# Calculate the distribution of wins
wins_distribution <- table(data$Winnings)
print("Distribution of Wins:")
print(wins_distribution)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
file_path = 'player_interactions.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
print(data.head())

# Visualization 1: Line plot of balance over interactions
plt.figure(figsize=(10, 6))
sns.lineplot(x='Interaction', y='Balance', data=data, marker='o')
plt.title('Balance Over Interactions')
plt.xlabel('Interaction')
plt.ylabel('Balance ($)')
plt.show()

# Visualization 2: Bar plot of total winnings over interactions
plt.figure(figsize=(10, 6))
sns.barplot(x='Interaction', y='Total_Winnings', data=data, palette='viridis')
plt.title('Total Winnings Over Interactions')
plt.xlabel('Interaction')
plt.ylabel('Total Winnings ($)')
plt.show()

# Visualization 3: Box plot of bet distribution
plt.figure(figsize=(10, 6))
sns.boxplot(x='Lines', y='Bet', data=data, palette='pastel')
plt.title('Distribution of Bets')
plt.xlabel('Number of Lines')
plt.ylabel('Bet ($)')
plt.show()


print("Break point")
import numpy as np

# Task 1: Create 2D array for 4 branches × 6 months
transactions = np.array([
    [1200, 1350, 1600, 1450, 1700, 1800],  # Branch 1
    [900,  1100, 1150, 1200, 1300, 1400],  # Branch 2
    [1600, 1700, 1750, 1800, 1900, 2000],  # Branch 3
    [800,  950,  1000, 1050, 1100, 1200]   # Branch 4
])

print("Transaction Volumes (4x6):")
print(transactions)
print()

# Task 2: Total transactions per branch
total_per_branch = np.sum(transactions, axis=1)
print("Total Transactions Per Branch:")
print(total_per_branch)
print()

# Task 3: Identify branch with highest transactions
highest_branch = np.argmax(total_per_branch) + 1
print("Branch with the highest total transactions:", highest_branch)
print()

# Task 4: Average monthly transactions across all branches
average_monthly = np.mean(transactions)
print("Average Monthly Transaction Volume:", average_monthly)
print()

# Task 5: Reshape to 3x8
reshaped = transactions.reshape(3, 8)
print("Reshaped Array (3x8):")
print(reshaped)

print("\nImplication of reshaping:")
print("Reshaping changes the structure of the data but not the values.")
print("Original meaning (branches × months) is lost in the reshaped format.")

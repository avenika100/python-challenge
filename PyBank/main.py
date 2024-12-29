# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies

import csv
import os

# Input file path
cvs_path = os.path.join("Resources", "budget_data.csv") 

# Output file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  

# Define variables to track the financial data
total_months = 0
total_net = 0
previous_profit_loss = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_month = ''
greatest_decrease_month = ''

# Add more variables to track other necessary financial data

dates = []
net_changes = []

# Open and read the csv
with open(cvs_path) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_profit_loss = int(first_row[1])
    dates.append(first_row[0])

    # Track the total and net change


    # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1

        # Track the net change
        total_net += int(row[1])

        # Calculate the greatest increase in profits (month and amount)
        monthly_change = int(row[1]) - previous_profit_loss
        net_changes.append(monthly_change)

        if monthly_change > greatest_increase: 
            greatest_increase = monthly_change
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            greatest_decrease_month = row[0]

        previous_profit_loss = int(row[1])
        dates.append(row[0])


# Calculate the average net change across the months
average_change =sum(net_changes)/ len(net_changes) if len(net_changes) > 0 else 0

# Generate the output summary
# Print the output
print("Financial Analysis")
print("---------------------------")
print(f"Total Months:{total_months}")
print(f"Total:${total_net:,}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profit: {greatest_increase_month} (${greatest_increase:,})")
print(f"Greatest Decrease in Profit: {greatest_decrease_month} (${greatest_decrease:,})")

# # Write the results to a text file

with open(file_to_output, "w") as txt_file:
    txt_file.write("Financial Analysis\n")
    txt_file.write("---------------------------\n")
    txt_file.write(f"Total Months:{total_months}\n")
    txt_file.write(f"Total:${total_net:,}\n")
    txt_file.write(f"Average Change: ${average_change:.2f}\n")
    txt_file.write(f"Greatest Increase in Profit: {greatest_increase_month} (${greatest_increase:,})\n")
    txt_file.write(f"Greatest Decrease in Profit: {greatest_decrease_month} (${greatest_decrease:,})\n")

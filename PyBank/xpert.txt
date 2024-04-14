import csv
import os

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyBank/Resources/budget_data.csv"

total_sum = 0
months = 0
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Initialize variables for tracking changes
    previous_profit = 0
    total_change = 0

    for row in csv_reader:
        months += 1
        profit = int(row[1])
        total_sum += profit

        if months > 1:
            change = profit - previous_profit
            total_change += change

            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_month = row[0]

            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_month = row[0]

        previous_profit = profit

average_change = total_change / (months - 1)

print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {months}")
print(f"Total: ${total_sum}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})")
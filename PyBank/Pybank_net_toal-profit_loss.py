import csv
import os

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyBank/Resources/budget_data.csv"

# Initialize total sum
total_sum = 0

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)
    print(f"Header: {csv_header}")

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Assuming the numbers are in the second column (index 1)
        number = int(row[1])  # Convert the number to an integer
        total_sum += number

print("Total sum of numbers in the column:", total_sum)





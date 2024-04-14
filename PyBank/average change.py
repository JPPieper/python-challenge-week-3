import csv
import os

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyBank/Resources/budget_data.csv"


#The total number of months included in the dataset
with open(file_path) as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        line_count += 1

print(f'Number of lines in the CSV file: {line_count}')

#The net total amount of "Profit/Losses" over the entire period
import csv
import os

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyBank/Resources/budget_data.csv"

# Initialize total sum
total_sum = 0

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Assuming the numbers are in the second column (index 1)
        number = int(row[1])  # Convert the number to an integer
        total_sum += number

print("Total net profit /loss:", total_sum)

Average_P_L =(total_sum/line_count)

print(f'Averageprofit/loss: {Average_P_L}')
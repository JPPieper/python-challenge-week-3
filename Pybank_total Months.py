import csv
import os

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyBank/Resources/budget_data.csv"

with open(file_path) as csvfile:
    csv_reader = csv.DictReader(csvfile, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
        line_count += 1

print(f'Number of lines in the CSV file: {line_count}')





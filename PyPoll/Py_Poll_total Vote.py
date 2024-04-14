import csv
import os

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyPoll/Resources/election_data.csv"

total_votes = 0

with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    csv_header = next(csv_reader)  # Skip the header row

    for row in csv_reader:
        total_votes += 1

print("Total Votes:", total_votes)


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

import csv

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyPoll/Resources/election_data.csv"
total_votes = 0
candidate_votes = {}

# Load the dataset
with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Count the total number of votes and store candidate votes
    for row in csv_reader:
        total_votes += 1
        candidate = row['Candidate']
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate and print the percentage of votes each candidate won
print("Percentage of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")

    import csv

file_path = "C:/Users/Owner/OneDrive/Desktop/boot camp homework repo/python-challenge week 3/PyPoll/Resources/election_data.csv"
total_votes = 0
candidate_votes = {}

# Load the dataset
with open(file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    # Count the total number of votes and store candidate votes
    for row in csv_reader:
        total_votes += 1
        candidate = row['Candidate']
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Find the winner based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the winner of the election
print("Winner: " + winner)
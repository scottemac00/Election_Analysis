# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row
    headers = next(file_reader)
    print(headers)

    # The data we need to retrieve.
    # 1. Get the list of names of the candidates
    # 2. Add a vote count for each candidate
    # 3. Get the total votes for each candidate
    # 4. Get the total votes cast for the election
    # 5. Calculate the percentage of votes won by each candidate
    # 6. Calculate the winner of the election based on popular vote
    #print the file object
   









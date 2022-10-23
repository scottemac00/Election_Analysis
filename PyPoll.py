# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("Analysis", "election_analysis.txt")
#Initialize variable to count total votes and make it zero
total_votes = 0

# Declare a list to get candidate names from the csv
candidate_options = []

# Create a dictionary with key = candidate and value = vote count
candidate_votes = {}

# Decleare a variable that holds an empty string value for the winning candidate
winning_candidate = ""

# Declare a variable for the winning count and make it zero
winning_count = 0

#Declare a variable for the winning percentage and make it zero
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)
    
    # Print each row in the CSV file
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

    # Iterate through the candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of candidate
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n") 
        # Determine winning vote count and candidate
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage  
            winning_candidate = candidate_name 
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print (winning_candidate_summary)



       
  

    


    # The data we need to retrieve.
    # 1. Get the list of names of the candidates
    # 2. Add a vote count for each candidate
    # 3. Get the total votes for each candidate
    # 4. Get the total votes cast for the election
    # 5. Calculate the percentage of votes won by each candidate
    # 6. Calculate the winner of the election based on popular vote
    #print the file object
   









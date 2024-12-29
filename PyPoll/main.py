# Import necessary modules

import csv
import os

# Input file path
cvs_path = os.path.join("Resources", "election_data.csv") 


# Initialize variables to track the election data
# Track the total number of votes cast
total_votes = 0  

# Define lists and dictionaries to track candidate names and vote counts
candidates = {}

# Winning Candidate and Winning Count Tracker
winning_count = 0
winning_candidate = ""
winning_percentage = 0



# Open the CSV file and process it
with open(cvs_path) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1

        # Get the candidate's name from the row
        candidate_name = row[2]

        # If the candidate is not already in the candidate list, add them
        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        # Add a vote to the candidate's count
        candidates[candidate_name] += 1

# Output file path
cvs_output = os.path.join("analysis", "election_analysis.txt") 

# Open a text file to save the output
with open("Pypoll Analysis.txt", "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f"Election Results\n")
    print(f"--------------------------\n")
    print(f"Total Votes: {total_votes}\n")

    # Write the total vote count to the text file
    txt_file.write(f"Election Results\n")
    txt_file.write(f"--------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")


    # Loop through the candidates to determine vote percentages and identify the winner
    for candidate_name in candidates:

        # Get the vote count and calculate the percentage
        vote_count = candidates[candidate_name]
        vote_percentage = (vote_count / total_votes) * 100

        # Update the winning candidate if this one has more votes
        if vote_count > winning_count:
            winning_count = vote_count
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

        # Print and save each candidate's vote count and percentage
        print(f"{candidate_name}: {vote_percentage:.3f}% ({vote_count})\n")
        # Write each candidate's vote count and percentage to the output file
        txt_file.write(f"{candidate_name}: {vote_percentage:.3f}% ({vote_count})\n")


    # Generate and print the winning candidate summary
    print(f"-------------------------\n")
    print(f"Winner: {winning_candidate}\n")
    print(f"-------------------------\n")

    # Save the winning candidate summary to the text file
    txt_file.write(f"-------------------------\n")
    txt_file.write(f"Winner: {winning_candidate}\n")
    txt_file.write(f"-------------------------\n")
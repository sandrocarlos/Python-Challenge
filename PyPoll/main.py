
import os 
import csv

# Path to CSV File
csvpath = "./Resources/election_data.csv"

# Open CSV file "Budget Data" defined above
with open(csvpath, 'r') as csvfile:
    PyPollReader = csv.reader(csvfile)
    PyPoll_list = list(PyPollReader)
    PyPoll_header = PyPoll_list[0]
    PyPoll_data = PyPoll_list[1:]


# Setting our variables...
Total_Votes = 0
Stockham_Votes = 0
DeGette_Votes = 0
Doane_Votes = 0 



# Iterate through and count each candidates votes based on the 'if' 
for data in PyPoll_data:

    # Calculate total votes casted for all candidates
    Total_Votes += 1
    # Where element 2 is Charles Casper then count their vote + 1
    if data[2] == "Charles Casper Stockham":
        Stockham_Votes += 1
    # Where element 2 is Diana DeGette then count their vote + 1
    elif data[2] == "Diana DeGette":
        DeGette_Votes += 1
    # Take remaining candidate rows and count their vote + 1
    else:
        Doane_Votes += 1 

# Calculate each candidates votes then divide by total votes... multiply by 100 to get percentage. Add , 3 argument to limit decimal points to 3.
Stockham_Percentage = round((Stockham_Votes / Total_Votes *100), 3)
Doane_Percentage = round((Doane_Votes / Total_Votes * 100), 3)
DeGette_Percentage = round((DeGette_Votes / Total_Votes * 100), 3)

# Create a list of each candidates total votes to insert into max function
vote_list = [Stockham_Votes, DeGette_Votes, Doane_Votes]
# Identify the highest vote count of the candidates
winner_vote_cnt = max(vote_list)
# Create a dictionary key value pair to cycle through to identify the winner
candidate_list = {
   
    "Charles Casper Stockham": Stockham_Votes, 
    "Diana Degette": DeGette_Votes,
    "Raymon Anthony Doane" : Doane_Votes        
}
# Creating an empty string to hold the winner's name...
winner_name = ""

# Creating for loop to iterate through the dictionary's key value pair (k,v)
# In this k,v loop, I am setting if winner_vote_count(Max value of votes) is v (Candidate's vote count in the dictionary), then look at k (Key: candidate's name in the dictionary)
# This gives us our winner's name.   
for k, v in candidate_list.items():
    
    if winner_vote_cnt == v:
        winner_name = k

#  Generate output, limit the average change to three decimal points 
# Each curly brace is referencing the identified variables to answer this week's challenge
output = f"""
Election Results
------------------------

Total Votes: {Total_Votes}

------------------------
Charles Casper Stockham: {Stockham_Percentage}% ({Stockham_Votes})
Diana DeGette: {DeGette_Percentage}% ({DeGette_Votes})
Raymon Anthony Doane: {Doane_Percentage}% ({Doane_Votes})

------------------------

The Winner is {winner_name}

"""

# Print output to terminal
print(output)

# # Write output to a .txt file
output_file = "./analysis/PyPoll_Challenge.txt"
with open(output_file, 'w') as txtfile:
    txtfile.write(output)

# # write output to a .csv file
output_file = "./analysis/PyPoll_Output.csv"
with open(output_file, 'w') as csvfile:
    csvfile.write(output) 
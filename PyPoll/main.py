
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


# Create List to store total vote count
# Vote_Count= []  

# Defining variables to hold the month and values of greatest increase/decrease
# Most_Votes= ["",0]


# Iterate through each candidates votes
for data in PyPoll_data:

    # Calculate total votes casted for all candidates
    Total_Votes += 1
    # Where element 2 is Charles Casper then count his vote + 1
    if data[2] == "Charles Casper Stockham":
        Stockham_Votes += 1
    elif data[2] == "Diana DeGette":
        DeGette_Votes += 1
    else:
        Doane_Votes += 1 

Stockham_Percentage = round((Stockham_Votes / Total_Votes *100), 3)
Doane_Percentage = round((Doane_Votes / Total_Votes * 100), 3)
DeGette_Percentage = round((DeGette_Votes / Total_Votes * 100), 3)

vote_list = [Stockham_Votes, DeGette_Votes, Doane_Votes]
winner_vote_cnt = max(vote_list)
candidate_list = {
   
    "Charles Casper Stockham": Stockham_Votes, 
    "Diana Degette": DeGette_Votes,
    "Raymon Anthony Doane" : Doane_Votes        
}
winner_name = ""
    # three main dictionary functions
        # .items() gives both key value pairs
        # .keys() gives key data
        # .values() gives value data

# print(candidate_list.items())
# print(candidate_list.keys())
# print(candidate_list.values())

for k, v in candidate_list.items():
    
    if winner_vote_cnt == v:
        winner_name = k

#  Generate output, limit the average change to two decimal points
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
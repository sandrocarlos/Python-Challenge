
import os 
import csv

# Path to CSV File
csvpath = "./Resources/budget_data.csv"

# Open CSV file "Budget Data" defined above
with open(csvpath, 'r') as csvfile:
    csvReader = csv.reader(csvfile)
    csv_list = list(csvReader)
    csv_header = csv_list[0]
    csv_data = csv_list[1:]

# Setting our variables...
Month_Cnt = len(csv_data)
Money_Total = 0
Profit_Losses = 0

# Create List to store monthly differences
Monthly_Differences = []  

# Defining variables to hold the month and values of greatest increase/decrease
Greatest_Increase = ["",0]
Greatest_Decrease = ["",0]

# Iterate through each month's data and money
for data in csv_data:
    try:
        # Convert profit/loss (money) value to integer
        Money = int(data[1])
    except ValueError:
        continue  # if the cell does not contain a numerical value, skip and continue to next numerical value

    # Calculate total profit/loss (money total)
    Money_Total = Money_Total + Money

    # Calculate difference from previous month (but exclude the first month) 
    if Profit_Losses != 0:
        Monthly_Difference = Money - Profit_Losses
        Monthly_Differences.append(Monthly_Difference)

        # Update Greatest Increase and Decrease values 
        if Monthly_Difference > Greatest_Increase[1]:
            Greatest_Increase = [data[0], Monthly_Difference]
        if Monthly_Difference < Greatest_Decrease[1]:
            Greatest_Decrease = [data[0], Monthly_Difference]

    # Update Profit_Losses for next iteration
    Profit_Losses = Money

# Determine average_change... take the sum of our new element Monthly Differences and divide by the count of transactions. 
if len(Monthly_Differences) > 0:
    Average_Change = sum(Monthly_Differences) / len(Monthly_Differences)

# Generate output, limit the average change to two decimal points
output = f"""
Financial Analysis
------------------------
Total Months: {Month_Cnt}
Total: ${Money_Total}
Average Change: ${Average_Change:.2f} 
Greatest Increase in Profits: 
   Month: {Greatest_Increase[0]} 
   Amount: ${Greatest_Increase[1]} 
Greatest Decrease in Profits: 
   Month: {Greatest_Decrease[0]} 
   Amount: ${Greatest_Decrease[1]} 


"""

# Print output to terminal
print(output)

# Write output to a .txt file
output_file = "./analysis/PyBank_Challenge.txt"
with open(output_file, 'w') as txtfile:
    txtfile.write(output)

# write output to a .csv file
output_file = "./analysis/PyBank_Output.csv"
with open(output_file, 'w') as csvfile:
    csvfile.write(output)
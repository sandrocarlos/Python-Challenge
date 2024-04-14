import os 
import csv

# Source: Caite Green via Justin (the TA) 
# Path to CSV File
csvpath = "./Resources/budget_data.csv"
# Opening CSV file
with open(csvpath, 'r') as csvfile:
   csvReader = csv.reader(csvfile)
   #convert to a list and separate the header from the data
   csv_list = list(csvReader)
   csv_header = csv_list[0]
   csv_data = csv_list[1:]

# Determine the count of months
Count_of_Months = len(csv_data)
#print(Count_of_Months)

# Declare Variables

Total_Months = Count_of_Months
"""
Total = 
Average_Change = 
Greatest_Increase = 
Greatest_Decrease = 
"""

Profit_Losses = 0
Date = 0

print(Total_Months)

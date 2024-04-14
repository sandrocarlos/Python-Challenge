print("Something")

import os 
import csv

# Source: Caite Green via Justin (the TA) 
# Define the relative path to the CSV file
csvpath = "./budget_data.csv"
# Open the CSV file
with open(csvpath, 'r') as csvfile:
   csvReader = csv.reader(csvfile)
   #convert to a list and separate the header from the data
   csv_list = list(csvReader)
   csv_header = csv_list[0]
   csv_data = csv_list[1:]

   
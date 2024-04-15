
import os 
import csv
import math

# Source: Assistance received from Caite Green and Justin (the TA) 
# Path to CSV File
csvpath = "./budget_data.csv"
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

Month_Cnt = Count_of_Months
Monetary_Diff_Total = 0
Monetary_Diff = 0
MDT = Monetary_Diff_Total
MD = Monetary_Diff
Money_Total = 0
Profit_Losses = 0
Total = MDT
Greatest_Increase = ["", 0]
Greatest_Decrease = ["", 0]

for data in csv_data:
   try:
      Money = int(data[1])
   except ValueError:
      continue
   Money_Total = Money_Total + Money

   if Profit_Losses > 0:
      MD = Money - Profit_Losses
      MDT = MDT + MD

      if MD > Greatest_Increase[1]:
         Greatest_Increase = [data[0], MD]
      elif MD < Greatest_Decrease[1]:
         Greatest_Decrease = [data[0], MD]

   Profit_Losses = Money

   Average_Change = MD / (Month_Cnt - 1)


output = """
Financial Analysis
------------------------
Total Months: %d
Total: %d
Average Change: %d
Greatest Increase: %s
Greatest Decrease: %s
""" % (Month_Cnt, Money_Total, MDT, str(Greatest_Increase),str(Greatest_Decrease))
#print to the terminal
print(output)
#make a file in my main
output_file = "./PyBank_Challenge.txt"
#open the file as writeable and write the output into the the txtfile
with open(output_file,'w') as txtfile:
    txtfile.write(output)

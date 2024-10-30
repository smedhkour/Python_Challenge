# dependencies
import csv
import os
from datetime import datetime

file_to_load = os.path.join("Resources", "budget_data.csv")  
file_to_output = os.path.join("analysis", "budget_analysis.txt")  

#define variables
net_change = []
total_months = 0
total_net= 0
last_profit = None
greatest_increase={"date": "", "amount": float('-inf')}
greatest_decrease={"date": "", "amount": float('-inf')}

#add more variables to track other neccesary financial data
unique_months=set()
column_index = 1
#open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    #skip the header row
    header = next(reader)
    #process each row of data
    for row in reader:
        date = row[0]
        profit = int(row[1])
        #track net change
        total_net+= profit
        #track the total
        total_months +=1
        #track the changes in profit/losses
        if last_profit is not None:
            change = profit - last_profit
            net_change.append(change)   
        
            #calculate the greatest increase in profits (month and amount) 
            if change > greatest_increase['amount']:
                greatest_increase['date'] = date
                greatest_increase['amount'] = change
            #calclulate the greatest decrease in losses (month and amount)
            if change <= greatest_decrease['amount']:
                greatest_decrease['date'] = date
                greatest_decrease['amount'] = change
        last_profit = profit
#calculate the average net change across the months
if net_change:
    average_change = sum(net_change) / len(net_change)
else:
    average_change = 0

#print results
results = (
        "Financial Analysis"
        "-------------------------"
        f'Total Months: {total_months}'
        f'Total: {total_net}'
        f'Average Change: ${average_change}'
        f"Greatest Increase in Profits: {greatest_increase}\n"
        f"Greatest Decrease in Profits: {greatest_decrease}\n")

print(results)
#write the results to a text file

with open('budget_analysis.txt', 'w') as txt_file:
      txt_file.write(results)

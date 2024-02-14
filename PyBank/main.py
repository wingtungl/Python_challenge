import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')

total_month= 0
net_total_profit=0
changes_in_profit=[]
average_change= []
profit_loss=0
greatest_inc=0
greatest_dec=0
greatest_inc_date=""
greatest_dec_date=""

#ReadCSV
with open(csvpath)as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
#Total Month, Profit Change, Greatest Increase, Greatest Decrease
    for row in csvreader:
        total_month= total_month+1
        net_total_profit= net_total_profit + int(row[1])
        changes= int(row[1])- profit_loss
        profit_loss= int(row[1])
        changes_in_profit.append(changes)
        if changes > greatest_inc:
            greatest_inc=changes
            greatest_inc_date=row[0]
        if changes < greatest_dec:
            greatest_dec=changes
            greatest_dec_date=row[0]

#Average Change
    changes_in_profit.pop(0)
    average_changes= sum(changes_in_profit)/ (total_month -1)

# Analysis in terminal
    print("Financial Analysis")
    print("---------------------")
    print(f"Total Months: {total_month}")
    print(f"Total: ${net_total_profit}")
    print(f"Average Change: ${average_changes}")
    print(f"Greatest Increase in Profits:{greatest_inc_date} (${greatest_inc})")
    print(f"Greatest Decrease in Profits:{greatest_dec_date} (${greatest_dec})")

#analysis in text file
file1 = open('pybank.txt', 'w')
print("Financial Analysis", file = file1)
print("---------------------", file = file1)
print(f"Total Months: {total_month}", file = file1)
print(f"Total: ${net_total_profit}", file = file1)
print(f"Average Change: ${average_changes}", file = file1)
print(f"Greatest Increase in Profits:{greatest_inc_date} (${greatest_inc})", file = file1)
print(f"Greatest Decrease in Profits:{greatest_dec_date} (${greatest_dec})", file = file1)

    









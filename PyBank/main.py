#Importing modules
import os

import csv

#Setting the path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

 #Defining variables and create empy lists 
total_months = []
net_total = []
changes = []

#Store budget_data.csv in csvreader 
with open(budget_data_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    
    #Skip the header row
    header = next(csvreader)
    
    # for loop to read every row
    for row in csvreader:
        
        total_months.append(row[0])
        net_total.append(int(row[1]))

    #Calculate the number of months and the net total amount
    for i in range(len(net_total)-1):

    #Calculate the changes in Profit/Losses
        changes.append(net_total[i+1]-net_total[i])

    #Calculate the average of changes
        average_change = sum(changes) / len(changes)

    #Calculate the greatest increase/decrease (date and amount)over the entire period
    max_increase = max(changes)
    max_decrease = min(changes)
    max_increase_index = changes.index(max(changes)) + 1
    max_decrease_index = changes.index(min(changes)) + 1
    

    #Results
    print("Financial Analysis")
    print("-------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total:${sum(net_total)}")
    print(f"Average Change: {round(sum(changes)/len(changes),2)}")
    print(f"Greatest Increase in Profit: {total_months[max_increase_index]} (${max_increase})")
    print(f"Greatest Decrease in Profit: {total_months[max_decrease_index]} (${max_decrease})")
   


#Create a results.txt file with the results
with open("results.txt", 'w') as file:
    file.write("Financial Analysis")
    file.write("\n")
    file.write("-------------------")
    file.write("\n")
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
    file.write(f"Average Change: $ {sum(net_total)}")
    file.write("\n")
    file.write(f"Greatest Increase in Profit: {total_months[max_increase_index]} (${max_increase})")
    file.write("\n")
    file.write(f"Greatest Decrease in Profit:  {total_months[max_decrease_index]} (${max_decrease})")

#Importing Modules

import csv

import os
#Setting the path
election_data_csv = os.path.join("Resources","election_data.csv")


#Create variables, empty lists, and dictionaries
total_votes = 0
candidate_votes = {}
candidates = []
percentage_count = []

#Store election_data.csv in csvreader
with open(election_data_csv, newline='') as csvfile:
    
        csvreader = csv.reader(csvfile,delimiter=',')

        #Skip the header row
        header = next(csvreader)

        #For loop for every row
        for row in csvreader:
            total_votes += 1
            if row[2] not in candidates:
                candidates.append(row [2]) 
                candidate_votes[row[2]]=0
            candidate_votes[row[2]]+=1
                
#Print the results
print("Election Results")
print("-----------------")
print(f"Total Votes: {str(total_votes)}")
print("-----------------")

#Calculate the percentage of votes each candidate won
for candidate, votes in candidate_votes.items():
    print(candidate + ":" + "{:.3%}".format(votes/total_votes)+"("+ str(votes)+")")  
#Print the results           
print("-----------------")           
    
#Finding out the winner of the election
winner = max(candidate_votes,key=candidate_votes.get)
#Print the results
print(f"Winner: {winner}")
print("-----------------")

#Create a results.txt file with the results
with open("results.txt", 'w') as file:
    file.write("Election Results")
    file.write("\n")
    file.write("------------------")
    file.write("\n")
    file.write(f"Total Votes: {str(total_votes)}")
    file.write("\n")
    file.write("-------------------")
    file.write("\n")
    file.write(candidate + ":" + "{:.3%}".format(votes/total_votes)+"("+ str(votes)+")")
    file.write("\n")
    file.write("-------------------")
    file.write("\n")
    file.write(f"Winner: {winner}")
    file.write("\n")
    file.write("-------------------")


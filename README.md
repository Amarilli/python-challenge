# python-challenge

In this Challenge, I need to create two Python scripts:

1) A Financial Analysis that investigates the records of a company. 
The dataset is called budget_data.csv, and has two columns: "Date" and "Profit/Losses."
My task is to create a Python script that calculates the following values:
- The total number of months included in the dataset
- The net total amount of "Profit/Losses" over the entire period
- The changes in "Profit/Losses" over the entire period and then the average of those changes
- The greatest increase in profits (date and amount) over the entire period
- The greatest decrease in profits (date and amount) over the entire period
- In addition, my final script needs to print the analysis to the terminal and export a text file with the results.

2) An Election Analysis of poll data called "election_data.csv," composed of three columns: "Voter ID," "Country," and "Candidate." 
My task is to create a Python script that analyzes the votes and calculates the following values:
- The total number of votes cast
- A complete list of candidates who received votes
- The percentage of votes each candidate won
- The total number of votes each candidate won
- The winner of the election is based on the popular vote.
- In addition, my final script needs to print the analysis to the terminal and export a text file with the results.

I started both scripts by importing the os and csv modules. After that, I set the path to find the files. I defined the variables and created empty lists and a dictionary. I opened the files using a "with open" statement, stored them in variables, and skipped the first row (headers). Then, I created for loops to find out the values requested. 
I ended both scripts by printing the results in the terminal and a separate .txt file.

AskBCS Learning Assistant, Chat CGP, TAs, and a tutor helped me to debug my scripts. The string to print that returns the percentage of the votes in the election analysis comes from line 104: https://gitlab.com/laurelstewart/python-challenge/-/blob/master/PyPoll/main.py?ref_type=heads 

#Calculate the following
    #The total votes cast
    #Percentage of votes each candidate won
    #Total number of votes each candidate won
    #Winner of election based on popular vote

import os
import csv
election_data = os.path.join("election_data.csv")

#Set empty lists for the candidates, votes received, and percentage votes received
Candidates = []
Number_of_Votes = []
Percent_of_Votes = []

#Set inital value for vote counter
Total_Votes = 0

#Add path to csvfile and start reading-------------------------------------------- 
with open("Resources/election_data.csv", "r") as csvfile:
    #Reading csvfile, define comma as the boundary between data with delimiter
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Reading header first
    csv_header = next(csvreader)

    for row in csvreader:
        #Tally vote counter
        Total_Votes += 1 

        #Complete the list of candidates 
        if row[2] not in Candidates:
            Candidates.append(row[2])
            index = Candidates.index(row[2])
            Number_of_Votes.append(1)
        else:
            index = Candidates.index(row[2])
            Number_of_Votes[index] += 1
    
    #Tally Percent_of_Votes list 
    for votes in Number_of_Votes:
        percentage = (votes/Total_Votes) * (100)
        percentage = round(percentage)
        #Formats how the number is displayed (Out to 3 decimal places as shown in example)
        percentage = "%.3f%%" % percentage
        Percent_of_Votes.append(percentage)
    
    #Determine winner
    Winner = max(Number_of_Votes)
    index = Number_of_Votes.index(Winner)
    Winner = Candidates[index]

# Print Results to Terminal---------------------------------------------------------
print("Election Results")
print("--------------------------")
print(f"Total Votes: {str(Total_Votes)}")
print("--------------------------")
for i in range(len(Candidates)):
    print(f"{Candidates[i]}: {str(Percent_of_Votes[i])} ({str(Number_of_Votes[i])})")
print("--------------------------")
print(f"Winner: {Winner}")
print("--------------------------")
#Output matches example in instructions

#Create .txt file--------------------------------------------------------------------
    #"w" will overwrite existing file with the results rather than appending it
output = open("Analysis.txt", "w")
line1 = "Election Results"
line2 = "--------------------------"
line3 = str(f"Total Votes: {str(Total_Votes)}")
line4 = str("--------------------------")
output.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
#loop through number of candidates, displaying each one 
for i in range(len(Candidates)):
    line = str(f"{Candidates[i]}: {str(Percent_of_Votes[i])} ({str(Number_of_Votes[i])})")
    output.write('{}\n'.format(line))
line5 = "--------------------------"
line6 = str(f"Winner: {Winner}")
line7 = "--------------------------"
output.write('{}\n{}\n{}\n'.format(line5, line6, line7))
#Format matches example in instructions
# Calculate the Following
#     Net Profit/Loss over entire period
#     Change in Profit/Loss over entire period    
#         Average of those changes
#     Greatest increase in Profits (date & amount) over entire period
#     Greatest decrease in losses (date & amount) over entire period
import os
import csv
budget_data = os.path.join("budget_data.csv")

#Initial Values and Lists---------------------------------------------------
Total_Months = 0
Net_Change = 0
#Used for calculations
Change = 0
Value = 0
#Track dates and their repsective profits in lists
Dates = []
Profits = []


#Pass the path to the csv file and begin reading------------------------------
with open("Resources/budget_data.csv", "r") as csvfile:
    #Read csvfile, define comma as boundaries between data with delimiter
    csvreader = csv.reader(csvfile, delimiter = ",")
    #Reading header first--------------------------
    csv_header = next(csvreader)

    #Read a single line at a time to attain values
    First_Row = next(csvreader)
    #Continue adding these values to our months, net change, and value trackers  
    Total_Months += 1
    Net_Change += int(First_Row[1])
    Value = int(First_Row[1])
    
    #Iterate through each row in csvfile and mark through each date-------------
    for row in csvreader:
        Dates.append(row[0])
        
        # Calculate Total Change
        Change = int(row[1])-Value
        #Add to end of Change list
        Profits.append(Change)
        Value = int(row[1])
        
        #Add up values to total the net change over entire period
        Net_Change = Net_Change + int(row[1])

        #Add to month tally
        Total_Months += 1

    #Define and calculate average Change in Profits over entire period
    Average_Change = sum(Profits)/len(Profits)
    
# Increase/Decrease using max/min--------------------------------------------
    #Find greatest increase in profits
    Greatest_Increase = max(Profits)
    Greatest_Increase_Index = Profits.index(Greatest_Increase)
    Greatest_Increase_Date = Dates[Greatest_Increase_Index]

    #Find greatest decrease in profits 
    Greatest_Decrease = min(Profits)
    Greatest_Decrease_Index = Profits.index(Greatest_Decrease)
    Greatest_Decrease_Date = Dates[Greatest_Decrease_Index]
#---------------------------------------------------------------------------
    

#Print information to terminal-------------------------------------------------------
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(Total_Months)}")
print(f"Total Change Over Entire Period: ${str(Net_Change)}")
print(f"Average Change: ${str(round(Average_Change,2))}")
print("----------------------------")
print(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${str(Greatest_Increase)})")
print(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${str(Greatest_Decrease)})")
#Outputs match with example given in instructions confirming accuracy-----------------

#Create.txt file--------------------------------------------------------------------
    #"w" to overwrite existing file rather than appending it
output = open("Analysis.txt", "w")
line1 = "Financial Analysis"
line2 = "---------------------------"
line3 = str(f"Total Months: {str(Total_Months)}")
line4 = str(f"Total Change Over Entire Period: ${str(Net_Change)}")
line5 = str(f"Average Change: ${str(round(Average_Change,2))}")
line6 = str(f"Greatest Increase in Profits: {Greatest_Increase_Date} (${str(Greatest_Increase)})")
line7 = str(f"Greatest Decrease in Profits: {Greatest_Decrease_Date} (${str(Greatest_Decrease)})")

output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

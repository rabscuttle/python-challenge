# Import modules
import os
import csv

# Import CSV
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
    
    # Set variables
    monthcount = 0
    netprofit = 0
    lastprofit = 0
    maxprofitchange = 0
    minprofitchange = 0
    profitchange = []
    
    # Read each row of data after the header
    for row in csvreader:
        date = row[0]
        profit = int(row[1])
        # Skip the first entry
        if lastprofit != 0:
            change = profit - lastprofit
            profitchange.append(change)
            # Set greatest increase and decrease
            if change > maxprofitchange:
                maxprofitchange = change
                maxprofitchangedate = date
            if change < minprofitchange:
                minprofitchange = change
                minprofitchangedate = date
        # Advance month
        monthcount = monthcount + 1
        # Set net profit
        netprofit = netprofit + profit
        # Set previous month profit for next loop
        lastprofit = profit
    
    # Calculate final values for table
    avgprofitchange = sum(profitchange) / len (profitchange)
    maxprofitchange = max(profitchange)
    minprofitchange = min(profitchange)
    
    # Final table in console
    print("Financial Analysis")
    print("------------------")
    print("Total Months: " + str(monthcount))
    print("Total: $" + str(netprofit))
    print("Average Change: $" + str(round(avgprofitchange, 2)))
    print("Greatest Increase in Profits: " + str(maxprofitchangedate) + " ($" + str(maxprofitchange) + ")")
    print("Greatest Decrease in Profits: " + str(minprofitchangedate) + " ($" + str(minprofitchange) + ")")
    
# Write final table to csv

# Specify the file to write to
output_path = os.path.join("analysis", "analysis.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write csv
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------'])
    csvwriter.writerow(['Total Months: ' + str(monthcount)])
    csvwriter.writerow(['Total: $' + str(netprofit)])
    csvwriter.writerow(['Average Change: $' + str(round(avgprofitchange, 2))])
    csvwriter.writerow(['Greatest Increase in Profits: ' + str(maxprofitchangedate) + ' ($' + str(maxprofitchange) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits: ' + str(minprofitchangedate) + ' ($' + str(minprofitchange) + ')'])
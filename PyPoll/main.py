# Import modules
import os
import csv

# Import CSV
csvpath = os.path.join('Resources', '02-Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv')

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first
    csv_header = next(csvreader)
       
    # Set variables
    totalVotes = 0
    results = {}
        
    # Read each row of data after the header
    for row in csvreader:
        totalVotes = totalVotes + 1
        voterId = row[0]
        name = row[2]
        if name not in results:
            results[name] = 1
        else:
            results[name] = results[name] + 1
 
    winner = max(results.values())
    winnerName = [name for name, count in results.items() if count == winner][0]
    
    # Final table in console
    print("Election Results")
    print("----------------")
    print("Total Votes: " + str(totalVotes))
    print("----------------")
    for name, count in results.items():
        pct = round((count/totalVotes)*100, 3)
        print(name + ": " + str(pct) + "% ("+ str(count) + ")")
    print("----------------")
    print("Winner: " + winnerName)
    print("----------------")    
import csv

# open source data file
with open("resources/election_data.csv") as election_data:
    reader = csv.reader(election_data)
    data_header = next(election_data)

# generate results dictionary
    ttl_votes = 0
    results = {}
    for row in reader:
        ttl_votes = ttl_votes + 1
        if row[2] in results.keys():
            results[row[2]]=results[row[2]]+1
        else:
            results[row[2]]=0

# print results
best_votes = 0
print("Total Votes: " + str(ttl_votes))
for key in results.keys():
    print(key + ": " + str(round(100 * results[key] / ttl_votes,2)) + "% (" + str(results[key]) + ")")
    if(results[key]) > best_votes:
        winner = key
        best_votes = results[key]
print("Winner: " + winner)

# Write the relevant data to a text file
with open("./analysis/summary.txt", "w") as text_file:
    best_votes = 0
    n = text_file.write("Total Votes: " + str(ttl_votes) + "\n")
    for key in results.keys():
        n = text_file.write(key + ": " + str(round(100 * results[key] / ttl_votes,2)) + "% (" + str(results[key]) + ")" + "\n")
        if(results[key]) > best_votes:
            winner = key
            best_votes = results[key]
    n = text_file.write("Winner: " + winner + "\n")

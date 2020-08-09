import csv

# Read the .csv
with open('./resources/budget_data.csv') as trick:
	reader = csv.reader(trick)
	header = next(reader)

# Set the variables that will impact the first iteration of my for-loop
	ttl_mo = 0
	net_pl = 0
	last_pl = 0
	pl_changes = []
	gr_incr_dat = ""
	gr_decr_dat = ""
	gr_incr = 0
	gr_decr = 0

# Loop through the rows to capture the relevant data
	for row in reader:
		ttl_mo = ttl_mo +1
		net_pl = net_pl + int(row[1])
		pl_changes.append(int(row[1])-last_pl)
		if int(row[1])-last_pl > gr_incr:
			gr_incr = int(row[1])-last_pl
			gr_incr_dat = row[0]
		if int(row[1])-last_pl < gr_decr:
			gr_decr = int(row[1])-last_pl
			gr_decr_dat = row[0]
		last_pl = int(row[1])
	del pl_changes[0]

# Print the relevant data
	print("Total Months " + str(ttl_mo))
	print("Total: $" + str(net_pl))
	print("Average Change: $" + str(round(sum(pl_changes)/len(pl_changes),2)))
	print("Greatest Increase in Profits: " + gr_incr_dat + " ($" + str(gr_incr) + ")")
	print("Greatest Decrease in Profits: " + gr_decr_dat + " ($" + str(gr_decr) + ")")

# Write the relevant data to a text file
with open("./analysis/summary.txt", "w") as text_file:
	n = text_file.write("Total Months " + str(ttl_mo) + "\n")
	n = text_file.write("Total: $" + str(net_pl) + "\n")
	n = text_file.write("Average Change: $" + str(round(sum(pl_changes)/len(pl_changes),2)) + "\n")
	n = text_file.write("Greatest Increase in Profits: " + gr_incr_dat + " ($" + str(gr_incr) + ")" + "\n")
	n = text_file.write("Greatest Decrease in Profits: " + gr_decr_dat + " ($" + str(gr_decr) + ")" + "\n")

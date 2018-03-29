import csv
from collections import Counter

# Function Declaration
def avg_col (old, new):
	col_totals = Counter()
	averages = []

	# Open input CSV
	with open(old, 'rb') as f:
		reader = csv.reader(f)

		# Track number of rows processed to determine cutoffs for avgs
		row_count = 0.0

		# Group by column, accumulate sum of values 
		for row in reader:
			for col_idx, col_val in enumerate(row):
				try:
					n = float(col_val)
					col_totals[col_idx] += n
				except ValueError:
					print "Error -- ({}) Column({}) could not be converted to float!".format(col_val, col_idx)
			row_count += 1.0

			# Cutoff and restart acumulation every 24 rows
			if row_count % 24 == 0:

				# Make sure col index keys are in order
				col_indices = col_totals.keys()
				col_indices.sort()

				# Calculate averages every 24 rows
				cur_avg = ['{:.4f}'.format(col_totals[idx]/24) for idx in col_indices]

				# Add row of avgs to final array
				averages.append(cur_avg)

				# Reset values in col_totals
				col_totals = Counter()
			
	# Write to new CSV
	with open(new, 'wb') as res:
		writer = csv.writer(res)
		writer.writerows(averages)

# Main program
name1 = 'test_csv.csv'
name2 = 'destination.csv'
avg_col(name1, name2)




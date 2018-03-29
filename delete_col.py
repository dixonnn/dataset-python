import csv

# Function Declaration
def del_col (old, new):

	# Open source file
	with open(old, 'rb') as src:
		reader = csv.reader(src)

		# Open destination file
		with open(new, 'wb') as res:
			writer = csv.writer(res)

			# Delete row specified by index, write to new file
			for row in reader:
				del row[0]
				writer.writerow(row)

# Main program
name1 = "source.csv"
name2 = "dest.csv"
del_col(name1, name2)



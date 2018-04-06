import csv
import datetime

# Function Declaration
def add_date_col (old, new):

	# First relevant day is 2012-10-02
	day_low = datetime.date(2012, 10, 2)
	# Total days in date range
	num_days = 1267
	# Create array of num_days days from 2012-10-02
	new_col = [day_low + datetime.timedelta(days=x) for x in range(0, num_days)]	

	# Open source file
	with open(old, 'rb') as src:
		reader = csv.reader(src)

		# Open destination file
		with open(new, 'wb') as res:
			writer = csv.writer(res)

			# Outer Loop: operate on each row -- add column to end
			i = 0
			for row in reader:
				l = len(row)

				# Check to make sure rows are same as number of days
				if len(new_col) != num_days:
					raise Exception('num_rows != num_days...')

				row.append("x")

				# Inner Loop: Successively move elements from L to R, 
				for element in row:
					row[l] = row[l-1]
					l -= 1
					if l == 0:
						break

				# Replace first element with correct date
				row[0] = new_col[i]
				i += 1
				writer.writerow(row) 
				

# Main program
name1 = "test_csv.csv"
name2 = "dest.csv"
add_date_col(name1, name2)

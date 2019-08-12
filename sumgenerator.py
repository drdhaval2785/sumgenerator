import random
import sys
from datetime import datetime

def date_time():
	"""Generate datetime in string."""

	return datetime.now().strftime("%d%m%Y_%H%M%S")

def num_to_str(numList):
	"""Generate string from list of numbers."""

	result = ''
	for num in numList:
		result += str(num)
	return result

def create_sum(length, n, take='take'):
	"""Generate <n> sums of digits <length>."""

	result = []
	# Generate n sums.
	for j in range(n):
		first = []
		second = []
		# Generate a random number of <length> digits.
		for i in range(length):
			first.append(random.randint(0,9))
		# Generate a random number of <length> digits.
		for dig in first:
			# If take / carry is allowed, second number is purely random.
			if take == 'take':
				second.append(random.randint(0,9))
			# If take / carry is not allowed, second number is restricted so that its addition does not cross 9.
			else:
				second.append(random.randint(0,9-dig))
		# Convert from list of numbers to strings.
		dig1 = num_to_str(first)
		dig2 = num_to_str(second)
		# Append to the result.
		result.append((dig1, dig2))
	# Return the result.
	return result

def create_subtraction(length, n, take=True):
	"""Generate <n> subtraction of <length> digits."""

	result = []	
	# Generate n sums.
	for j in range(n):
		first = []
		second = []
		# Random number of <length> digits.
		for i in range(length):
			# if the first digit, it can be from 1 to 9
			if i == 0:
				first.append(random.randint(1,9))
			else:
				first.append(random.randint(0,9))
		# Random number of <length> digits.
		for x in range(len(first)):
			dig = first[x]
			# The first digit of second number is to remain less than the first digit of the first number, so that the result is not negative.
			if x == 0:
				second.append(random.randint(0,dig-1))
			# If take / carry is allowed, the second number is random.
			elif take == 'take':
				second.append(random.randint(0,9))
			# otherwise the second number is less than the first one.
			else:
				second.append(random.randint(0,dig))
		# Generate digits from list of numbers.
		dig1 = num_to_str(first)
		dig2 = num_to_str(second)
		# Append to the result.
		result.append((dig1, dig2))
	# Return result.
	return result

def pretty_sum(digitTuples, arithmaticOperator, dttm, sumsInARow=5, writeAnswer=False):
	"""Pretty print the sums in html.

	Show <sumsInARow> sums on a line.
	"""
	
	# If Answers are to be printed (for parents / teachers), append ans to the filename.
	if writeAnswer:
		fout = open('math_ans_'+dttm+'.html', 'w')
	# Otherwise for kids, append que to filename.
	else:
		fout = open('math_que_'+dttm+'.html', 'w')
	# Generic HTML and CSS starting.
	fout.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n<title>\nMath sum generator</title>\n<style>\ntable, td {  border: 2px solid black; padding: 10px; font-size: 20px;}\n td { text-align: right; }\n</style>\n</head>\n<body>\n<table>\n')
	# Initialize counter
	counter = 0
	# a and b are the numbers
	for (a, b) in digit_tuples:
		# At every sumsInARow, insert a new table row.
		if counter % sumsInARow == 0:
			startCounter = counter
			fout.write('<tr>\n')
		# Generate Sum.
		summ = '<td>'
		summ += '<br>' + a + '<br/>'
		summ += arithmaticOperator + ' ' + b + '<br/>'
		summ += '--------------' + '<br/>'
		# If answer is to be written, do sum actually and print.
		if writeAnswer:
			if arithmaticOperator == '+':
				summ += str(int(a) + int(b)) + '<br/>'
			elif arithmaticOperator == '-':
				summ += str(int(a) - int(b)) + '<br/>'
		# Else leave a blank line.
		else:
			summ += '<br/>'
		# Close the td.
		summ += '</td>'	
		# Write summ to the file.
		fout.write(summ)
		# Close the row at specified interval i.e. <sumsInARow>.
		if counter - startCounter == sumsInARow - 1:
			fout.write('\n</tr>\n')
		# Increment counter.
		counter += 1
	# Close HTML.
	fout.write('</table>\n</body>\n</html>')


if __name__ == "__main__":
	# Operation can be + or -
	operation = sys.argv[1]
	# how many digits in the number?
	digits = int(sys.argv[2])
	# Default sums to generate are 25.
	if len(sys.argv) > 3:
		sumsToGenerate = int(sys.argv[3])
	else:
		sumsToGenerate = 25
	# Default is to allow take / carry.
	# If there is specific mention of 'notake', take / carry is not allowed.
	if len(sys.argv) > 4:
		take = sys.argv[4]
	else:
		take = 'take'
	# Date time in string format.
	dttm = date_time()
	# If addition,
	if operation == '+':
		# Create sums
		digit_tuples = create_sum(digits, sumsToGenerate, take)
		# Write without answers to HTML.
		pretty_sum(digit_tuples, '+', dttm)
		# Write with answers to HTML.
		pretty_sum(digit_tuples, '+', dttm, writeAnswer=True)
	# If subtraction,
	elif operation == '-':
		# Create sums.
		digit_tuples = create_subtraction(digits, sumsToGenerate, take)
		# Write without answers to HTML.
		pretty_sum(digit_tuples, '-', dttm)
		# Write with answers to HTML.
		pretty_sum(digit_tuples, '-', dttm, writeAnswer=True)



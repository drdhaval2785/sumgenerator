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
			first.append(random.randint(0,9))
		# Random number of <length> digits.
		for x in range(len(first)):
			dig = first[x]
			# The first digit of second number is to remain less than the first digit of the first number, so that the result is not negative.
			if x == 0:
				second.append(random.randint(0,dig))
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

def pretty_sum(digitTuples, arithmaticOperator, dttm, sumsInARow=10, writeAnswer=False):
	if writeAnswer:
		fout = open('math_ans_'+dttm+'.html', 'w')
	else:
		fout = open('math_que_'+dttm+'.html', 'w')
	fout.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="utf-8"/>\n<title>\nMath sum generator</title>\n<style>\ntable, td {  border: 2px solid black; padding: 10px;}\n td { text-align: right; }\n</style>\n</head>\n<body>\n<table>\n')
	counter = 0
	for (a, b) in digit_tuples:
		if counter % sumsInARow == 0:
			startCounter = counter
			fout.write('<tr>\n')
		summ = '<td>'
		summ += '<br>' + a + '<br/>'
		summ += arithmaticOperator + ' ' + b + '<br/>'
		summ += '--------------' + '<br/>'
		if writeAnswer:
			if arithmaticOperator == '+':
				summ += str(int(a) + int(b)) + '<br/>'
			elif airthmaticOperator == '-':
				summ += str(int(a) - int(b)) + '<br/>'
		else:
			summ += '<br/>'
		summ += '</td>'			
		fout.write(summ)
		if counter - startCounter == sumsInARow - 1:
			fout.write('\n</tr>\n')
		counter += 1
	fout.write('</table>\n</body>\n</html>')

if __name__ == "__main__":
	operation = sys.argv[1]
	digits = int(sys.argv[2])
	if len(sys.argv) > 3:
		sumsToGenerate = int(sys.argv[3])
	else:
		sumsToGenerate = 100
	if len(sys.argv) > 4:
		take = sys.argv[4]
	else:
		take = 'take'
	dttm = date_time()
	if operation == '+':
		digit_tuples = create_sum(digits, sumsToGenerate, take)
		pretty_sum(digit_tuples, '+', dttm)
		pretty_sum(digit_tuples, '+', dttm, writeAnswer=True)
	elif operation == '-':
		digit_tuples = create_subtraction(digits, sumsToGenerate, take)
		pretty_sum(digit_tuples, '-', dttm)
		pretty_sum(digit_tuples, '-', dttm, writeAnswer=True)



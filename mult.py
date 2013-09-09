import fileinput

max_product = 1
input = []
index = 0
num_zeroes = 0
is_first = True
for line in fileinput.input():
	if is_first:
		num_elems = int(line)
		is_first = False
	else:
		input.append(int(line))
		if input[index] != 0:
			max_product = max_product * input[index]
		else:
			num_zeroes = num_zeroes + 1
		index = index + 1

for x in xrange(len(input)):
	if num_zeroes > 1:
		print(int(0));
	else:
		if num_zeroes == 1:
			if input[x] == 0:
				print(max_product)
			else:
				print(int(0))
		else:
			print(max_product / input[x])
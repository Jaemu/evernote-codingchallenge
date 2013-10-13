import fileinput

top = [0,0,0,0]
minmax = -999999999
containsZero = False

def compare(arg):
	global top
	global minmax
	top.append(arg)
	temp = []
	for j in xrange(4):
		temp.append(max(top))
		top.remove(temp[j])
	top = temp
	minmax = min(top)
	return top
	return minmax	

for line in fileinput.input():
	if(int(line) == 0):
		containsZero = True
	if(int(line) > minmax):
		compare(int(line))

for i in xrange(4):
	if(containsZero):
		print(top[i])
	else:
		if(top[i] != 0):
			print(top[i])
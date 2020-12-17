def initialize():
	global x, result
	x = 0
	result = [x]

def observe():
	global x, result
	result.append(x)

def update():
	global x, result
	x = (x + (4464*3)) * 0.9

initialize()
for t in xrange(30):
	update()
	observe()

print result

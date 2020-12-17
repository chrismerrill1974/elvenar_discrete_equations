# library
import matplotlib.pyplot as plt
import numpy as np


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
for t in range(30):
	update()
	observe()

print(result)


# create data
x=range(31)
 
# stem function: first way
plt.stem(x, result)
plt.ylim(0, 120000)
plt.show()
 
# stem function: If no X provided, a sequence of numbers is created by python:
plt.stem(values)
#plt.show()
 
# stem function: second way
(markerline, stemlines, baseline) = plt.stem(x, result)
plt.setp(baseline, visible=False)
#plt.show()



from matplotlib import pyplot
import random

 

xValues = [0,4,7,20,22,25]
yValues = [random.randint(0,30) for elt in xValues]
pyplot.plot(xValues, yValues, "o-")

pyplot.ylabel("Value")
pyplot.xlabel("Time")
pyplot.title("Test plot")

pyplot.show()

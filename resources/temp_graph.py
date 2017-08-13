import matplotlib
import pylab

matplotlib.pyplot.switch_backend('Agg')
print(matplotlib.pyplot.get_backend())

class Graph(object):

	@staticmethod
	def generateGraph():
		file = open("resources/number.txt", "r+")
		try:
			number = int(file.read(1))
		except:
			number = 1
		file.close()
		print("Trying to graph: " + str(number))
		x = [1, 2, 3, 4, 5]
		y = [number, 2, 3, 4, 5]
		matplotlib.pyplot.scatter(x, y)
		pylab.savefig('static/images/graph.png')

import matplotlib
import pylab

matplotlib.pyplot.switch_backend('Agg')
print(matplotlib.pyplot.get_backend())

x = [1, 2, 3, 4, 5]
y = [1, 2, 3, 4, 5]

matplotlib.pyplot.scatter(x, y)
pylab.savefig('graph.png')

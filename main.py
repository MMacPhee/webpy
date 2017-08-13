import web
from resources import temp_graph

urls = (
	'/', 'home',
	'/calendar', 'calendar',
	'/fermentation', 'fermentation',
	'/(.*)/(.*)', 'index'
	)

render = web.template.render("resources/", base="MainLayout")
app = web.application(urls, globals())
set = []

class home:
	def GET(self):
		return render.home()

class index:
	def GET(self, name, age):
		set.append({"name": name, "age": age})
		for items in set:
			string = items["name"], items["age"] + " | "
		return render.main(string)

class calendar:
	def GET(self):
		return render.calendar()

class fermentation:
	def GET(self):
		file = open("resources/number.txt", "r+")
		try:
			number = int(file.read(1))
		except:
			number = 1
		print("Trying to write number: " + str(number))
		file.seek(0)
		file.write(str(number+1))
		file.close()
		temp_graph.Graph.generateGraph()
		return render.fermentation()

if __name__ == "__main__":
	app.run()


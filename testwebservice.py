import web
import structure

urls = (
	'/products/(\d+)', 'product',
	'/(.*)', 'search'
)

render = web.template.render('.')

class product:
	def GET(self, id):
		return render.index(id)

class search:
	def GET(self, keyword):
		return render.index(keyword)
	


if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
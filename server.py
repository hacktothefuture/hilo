import web
import structure
import json

web.config.debug = False

urls = (
	'/', 'index',

	# GETs
	'/products/(\d+)/gettoppros', 'gettoppros',
	'/products/(\d+)/gettoppros', 'gettopcons',
	'/products/(\d+)/getpros', 'getpros',
	'/products/(\d+)/getcons', 'getcons',

	# POSTs
	'/products/(\d+)/addpro_message=(\w+)', 'addpro',
	'/products/(\d+)/addcon_message=(\w+)', 'addcon',
	'/products/(\d+)/voteup_proconid=(\d+)', 'voteup',
	'/products/(\d+)/votedown_proconid=(\d+)', 'votedown'
	)

class index:
	def GET(self):
		render = web.template.render('./')    
		return render.index()

# GETs

class gettoppros:
	def GET(self, prod_id):
		return json.dumps(model.productList[prod_id].getTopPros())

class gettopcons:
	def GET(self, prod_id):
		return json.dumps(model.productList[prod_id].getTopCons())

class getpros:
	def GET(self, pro_id):
		return json.dumps(model.productList[prod_id].getPros())

class getcons:
	def GET(self, prod_id):
		return json.dumps(model.productList[prod_id].getCons())

# POSTs

class addpro:
	def POST(self, prod_id, message):
		model.productList[prod_id].addPro(message)
class addcon:
	def POST(self, prod_id, message):
		model.productList[prod_id].addCon(message)

class voteup:
	def POST(self, prod_id, pcID):
		model.productList[prod_id].voteUp(pcID)

class votedown:
	def POST(self, prod_id, pcID):
		model.productList[prod_id].voteDown(pcID)


if __name__ == "__main__": 
	model = structure.dataModel()
	app = web.application(urls, globals())
	app.run()

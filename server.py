import web
from structure import dataModel, product, pro_con
import json

web.config.debug = False # don't give us debug messages

urls = (
    # routes regex-formatted urls to Python classes.
    # any regex matchgroups are passed as arguments
    # to the class's GET or POST method

    # *** BEWARE OF MISSING COMMAS *** #

	'/', 'index',
    '/query=(.+)', 'index',
	'/products/(\d+)', 'prod',

	# GETs
	'/products/(\d+)/gettoppros=(\d+)', 'gettoppros',
	'/products/(\d+)/gettopcons=(\d+)', 'gettopcons',
	'/products/(\d+)/getpros', 'getpros',
	'/products/(\d+)/getcons', 'getcons',

	# POSTs
	'/products/(\d+)/addpro', 'addpro',
	'/products/(\d+)/addcon', 'addcon',
	'/products/(\d+)/voteup_proconid=(\d+)', 'voteup',
	'/products/(\d+)/votedown_proconid=(\d+)', 'votedown',
	'/saveVals', 'save'
	)

# classes to serve base html pages

class index:
	def GET(self, searchQuery=""):
		render = web.template.render('./')    
		return render.index(searchQuery)

class prod:
	def GET(self, prodID):
		render = web.template.render('./') # look in this directory for templates
		return render.product(prodID) # use product.html, fill in the $var with prodID


# GETs

class gettoppros:
	def GET(self, prod_id, n):
		if (model.productList.get(int(prod_id),-1) ==-1): # avoid key errors
			return ""
		return json.dumps(model.productList[int(prod_id)].getTopPros(int(n)),
                            default=lambda o: o.__dict__) # required to json.dump a dict

class gettopcons:
	def GET(self, prod_id, n):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getTopCons(int(n)),
                            default=lambda o: o.__dict__)

class getpros:
	def GET(self, prod_id):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getPros(),
                            default=lambda o: o.__dict__)

class getcons:
	def GET(self, prod_id):
		if (model.productList.get(int(prod_id),-1) ==-1):
			return ""
		return json.dumps(model.productList[int(prod_id)].getCons(),
                            default=lambda o: o.__dict__)

# POSTs

class addpro:
	def POST(self, prod_id):
		message = web.data() # extract the POSTed data
		model.addPro(int(prod_id), message)

class addcon:
	def POST(self, prod_id):
		message = web.data()
		model.addCon(int(prod_id), message)

class voteup:
	def POST(self, prod_id, pcID):
		model.productList[int(prod_id)].voteUp(int(pcID))

class votedown:
	def POST(self, prod_id, pcID):
		model.productList[int(prod_id)].voteDown(int(pcID))



if __name__ == "__main__":
    # start the webserver
	model = dataModel()
	app = web.application(urls, globals())
	app.run()

import pickle

class data_model:
	def __init__(self):
		self.saveFile = "save.p"
		try:
			self.productList = pickle.load( open("save.p", "rb")) 
		except EOFError:
			self.productList = []
	
	def outputText(self):
		pickle.dump(self.productList, open("save.p", "wb"))
		
		
		
class product:
	def __init__(self, prod_id, pro_con_list):
		self.id = prod_id
		self.list = pro_con_list
		

class pro_con:
	def __init__(self, pro_con_id, is_pro, message, votes):
		self.pro = is_pro
		self.id = pro_con_id
		self.message = message
		self.votes = votes	
		


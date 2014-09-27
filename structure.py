import pickle

class dataModel:
	def __init__(self):
		#initializes dataModel from the pickled file
		self.saveFile = "save.p"
		try:
			self.productList = pickle.load( open("save.p", "rb")) 
		except EOFError:
			self.productList = {}
	
	def outputText(self):
		#writes the pickle file to pickle.dump
		pickle.dump(self.productList, open("save.p", "wb"))

	def addPro(self, prod_id, message):
		#Checks whether the product is represented in the model, if not adds it
		if prod_id not in self.productList.keys():
			self.productList[prod_id] = product(self, prod_id, [], [])
		#Calls addPro at the product level
		self.productList[prod_id].addPro(message)


	def addCon(self, id, message):
		if id not in self.productList.keys():
			self.productList[id] = product(self, id, [], [])
		self.productList[id].addCon(message)

		
		
class product:
	def __init__(self, data_model, prod_id, pro_list, con_list):
		self.id = prod_id
		self.proList = pro_list
		self.conList = con_list
		self.model = data_model
		self.currentID = 0;
		
	def getTopPros(self, n=1):
		self.proList.sort(key=lambda x: x.votes, reverse=True)
		for i in self.proList:
			print(i.message)
		return self.proList[0:n]
		
	def getTopCons(self, n=1):
		self.conList.sort(key=lambda x: x.votes, reverse=True)
		return self.conList[0:n]
		
	def getPros(self):
		self.proList.sort(key=lambda x: x.votes, reverse=True)
		return self.proList
		
	def getCons(self):
		self.conList.sort(key=lambda x: x.votes, reverse=True)
		return self.conList
		
	def addPro(self, message):
		#increments id for the pros and cons to avoid duplicate ids
		self.currentID += 1
		if (self.model.productList.get(self.id, -1) != -1):
			self.proList.append(pro_con(self.currentID, message, 1))
		else:
			self.proList.append(pro_con(self.currentID, message, 1))
			self.model.productList[self.id] = product(self.model, self.id, self.proList, [])
		self.model.outputText()
			
	def addCon(self, message):
		#imcrements id for the pros and cons to avoid duplicate ids
		self.currentID += 1
		if (self.model.productList.get(self.id, -1) != -1):
			self.conList.append(pro_con(self.currentID, message, 1))
		else:
			self.conList.append(pro_con(self.currentID, message, 1))
			self.model.productList[self.id] = product(self.model, self.id, [], self.conList)
		self.model.outputText()
			
	def voteUp(self, pcID):
		# searches for pros or cons with that id
		for i in self.conList:
			if i.id==pcID:
				i.votes += 1
		for i in self.proList:
			if i.id==pcID:
				i.votes += 1
		self.model.outputText()
				
	def voteDown(self, pcID):
		# searches for pros or cons with that id
		for i in self.conList:
			if i.id==pcID:
				i.votes -= 1
		for i in self.proList:
			if i.id==pcID:
				i.votes -=1
		self.model.outputText()	
			
class pro_con:
	def __init__(self, pro_con_id, message, votes):
		self.id = pro_con_id
		self.message = message
		self.votes = votes	

		


import pickle

class dataModel:
	def __init__(self):
		self.saveFile = "save.p"
		try:
			self.productList = pickle.load( open("save.p", "rb")) 
		except EOFError:
			self.productList = {}
	
	def outputText(self):
		pickle.dump(self.productList, open("save.p", "wb"))

	def addPro(self, prod_id, message):
		print str(self.productList.keys())
		if prod_id not in self.productList.keys():
			print "creating new product"
			self.productList[prod_id] = product(self, prod_id, [], [])
		self.productList[prod_id].addPro(message)
		print "Now, product's pros are " + str(self.productList[prod_id].getTopPros(5))

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
		self.currentID += 1
		if (self.model.productList.get(self.id, -1) != -1):
			self.proList.append(pro_con(self.currentID, message, 1))
		else:
			self.proList.append(pro_con(self.currentID, message, 1))
			self.model.productList[self.id] = product(self.model, self.id, self.proList, [])
		for pro in self.proList:
			print(pro.message)
			
	def addCon(self, message):
		self.currentID += 1
		if (self.model.productList.get(self.id, -1) != -1):
			self.conList.append(pro_con(self.currentID, message, 1))
		else:
			self.conList.append(pro_con(self.currentID, message, 1))
			self.model.productList[self.id] = product(self.model, self.id, [], self.conList)
			
	def voteUp(self, pcID):
		for i in self.conList:
			if i.id==pcID:
				i.votes += 1
		for i in self.proList:
			if i.id==pcID:
				i.votes += 1
				
	def voteDown(self, pcID):
		for i in self.conList:
			if i.id==pcID:
				i.votes -= 1
		for i in self.proList:
			if i.id==pcID:
				i.votes -=1		
			
class pro_con:
	def __init__(self, pro_con_id, message, votes):
		self.id = pro_con_id
		self.message = message
		self.votes = votes	

def populate():
	model = dataModel()
	proList = [pro_con(1, "Better than anything I've ever used", 1759), pro_con(3, "Looks Pretty", -15)]
	conList = [pro_con(2, "Worst product ever", 158), pro_con(4, "Meh", -1000000)]
	model.productList[1] = product(model, 1, proList, conList)
	model.outputText()
	
		
if __name__ == "__main__":
	populate()
		


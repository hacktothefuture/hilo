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
		
		
		
class product:
	def __init__(self, data_model, prod_id, pro_list, con_list):
		self.id = prod_id
		self.proList = pro_list
		self.conList = con_list
		self.model = data_model
		self.currentID = 0;
		
	def getTopPros(self, n=3):
		self.proList.sort(key=lambda x: x.votes, reverse=True)
		return self.conList[0:n]
		
	def getTopCons(self, n=3):
		self.conList.sort(key=lambda x: x.votes, reverse=True)
		return self.proList[0:n]
		
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
			proList = [pro_con(self.currentID, message, 1)]
			self.model.productList[self.id] = product(self.model, self.id, proList, [])
			
	def addCon(self, message):
		self.currentID += 1
		if (self.model.productList.get(self.id, -1) != -1):
			self.conList.append(pro_con(self.currentID, message, 1))
		else:
			conList = [pro_con(self.currentID, message, 1)]
			self.model.productList[self.id] = product(self.model, self.id, conList, [])
			
	def voteUp(self, pcID):
		for i in conList:
			if i==pcID:
				i.votes += 1
		for i in proList:
			if i==pcID:
				i.votes +=1
				
	def voteUp(self, pcID):
		for i in conList:
			if i==pcID:
				i.votes -= 1
		for i in proList:
			if i==pcID:
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
		


# Python3
class Player:
	def __init__(self):
		self.hygiene = 0
		self.energy = 10
		self.fun = 0

	def valueOut(self):
		print('''Hygiene = {:d}\nEnergy = {:d}\nFun = {:d}''').format(self.hygiene, self.energy, self.fun)

	def check(self):
		if (self.hygiene > 15): self.hygiene = 15
		if (self.energy > 15): self.energy = 15
		if (self.fun > 15): self.fun = 15
		if (self.hygiene < 0): self.hygiene = 0
		if (self.energy < 0): self.energy = 0
		if (self.fun < 0): self.fun = 0
		self.valueOut()

	'''
			self.hygiene %= 16
			self.energy %= 16
			self.fun %= 16
	'''
	def tidur(self, waktu):
		if (waktu == "Siang"):
			self.energy += 10
		else:
			self.energy += 15
		self.check()

	def makan(self, makanan):
		m = {
			"Hamburger": (lambda x: x+5),
			"Pizza": (lambda x: x+10),
			"Steak and Beans": (lambda x: x+15)
		}
		self.energy = m.get(makanan)(self.energy)
		self.check()

	def minum(self, minuman):
		m = {
			"Air": (lambda x,y: (x-5,y)),
			"Kopi": (lambda x,y: (x-10,y+5)),
			"Jus": (lambda x,y: (x-5,y+10))
		}
		self.hygiene, self.energy = m.get(minuman)(self.hygiene, self.energy)
		self.check()

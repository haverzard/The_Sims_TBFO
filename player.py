# Python3
class Player:
	def __init__(self):
		self.hygiene = 0
		self.energy = 10
		self.fun = 0

	def valueOut(self):
		print('''Hygiene = {:d}\nEnergy = {:d}\nFun = {:d}'''.format(self.hygiene, self.energy, self.fun))

	def IsFinal(self):
		return (self.hygiene == 15 and  self.energy == 15 and self.fun == 15) or (self.hygiene == 0 and self.energy == 0 and self.fun == 0)

	def check(self, a, b, c):
		a += self.hygiene
		b += self.energy
		c += self.fun
		return (a <= 15 and  b <= 15 and c <= 15) and (a >= 0 and b >= 0 and c >= 0)
	
	def sign(self, a, b, c):
		self.hygiene += a
		self.energy += b
		self.fun += c
	
	def t_sign(self, a, b, c):
		if (self.check(a,b,c)):
			self.hygiene += a
			self.energy += b
			self.fun += c
			self.valueOut()
		else:
			print("Aksi tidak valid")
		return self
	
	def tidur(self, waktu):
		c = {
			"Siang": (lambda x: x.t_sign(0,10,0)),
			"Malam": (lambda x: x.t_sign(0,15,0))
		}
		self = c.get(waktu)(self)

	def makan(self, makanan):
		c = {
			"Hamburger": (lambda x: x.t_sign(0,5,0)),
			"Pizza": (lambda x: x.t_sign(0,10,0)),
			"Steak and Beans": (lambda x: x.t_sign(0,15,0))
		}
		self = c.get(makanan)(self)

	def minum(self, minuman):
		c = {
			"Air": (lambda x: x.t_sign(-5,0,0)),
			"Kopi": (lambda x: x.t_sign(-10,5,0)),
			"Jus": (lambda x: x.t_sign(-5,10,0))
		}
		self = c.get(minuman)(self)
	
	def buang_air(self, ukuran):
		c = {
			"Kecil": (lambda x: x.t_sign(5,0,0)),
			"Besar": (lambda x: x.t_sign(10,-5,0))
		}
		self = c.get(ukuran)(self)
	
	
	
	

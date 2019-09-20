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
		if (self.check(a,b,c)):
			self.hygiene += a
			self.energy += b
			self.fun += c
			self.valueOut()
		else:
			print("Aksi tidak valid")
		return self

	def doing(self, aksi):
		choices = {
			"Tidur Siang": (lambda x: x.sign(0,10,0)),
			"Tidur Malam": (lambda x: x.sign(0,15,0)),
			"Makan Hamburger": (lambda x: x.sign(0,5,0)),
			"Makan Pizza": (lambda x: x.sign(0,10,0)),
			"Makan Steak and Beans": (lambda x: x.sign(0,15,0)),
			"Minum Air": (lambda x: x.sign(-5,0,0)),
			"Minum Kopi": (lambda x: x.sign(-10,5,0)),
			"Minum Jus": (lambda x: x.sign(-5,10,0)),
			"Buang Air Kecil": (lambda x: x.sign(5,0,0)),
			"Buang Air Besar": (lambda x: x.sign(10,-5,0)),
			# Ubah yg di bawah
			"Bersosialisasi ke Kafe": (lambda x: x.sign(0,0,0)),
			"Bermain Media Sosial": (lambda x: x.sign(0,0,0)),
			"Bermain Komputer": (lambda x: x.sign(0,0,0)),
			"Mandi": (lambda x: x.sign(0,0,0)),
			"Cuci Tangan": (lambda x: x.sign(0,0,0)),
			"Membaca Koran": (lambda x: x.sign(0,0,0)),
			"Membaca Novel": (lambda x: x.sign(0,0,0))
		}
		choices.get(aksi, (lambda x: print("Opsi tidak ada")))(self)
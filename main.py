from player import *

p1 = Player()
# x.sign(hygiene,energy,fun)

print("Game Dimulai!")
while not(p1.IsFinal()):
	aksi = input()
	p1.doing(aksi)

print("Game Selesai!")
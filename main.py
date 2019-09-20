from player import *

p1 = Player()

choices = {
	"Tidur": (lambda p,a: (p.tidur(a))),
	"Makan": (lambda p,a: (p.makan(a))),
	"Minum": (lambda p,a: (p.makan(a))),
	"Buang Air": (lambda p,a: (p.makan(a))),
	"Bersosialisasi ke Kafe": (lambda p: (p.sos_ke_kafe())),
	"Bermain Media Sosial": (lambda p: (p.main_medsos())),
	"Bermain Komputer": (lambda p: (p.main_komputer())),
	"Mandi": (lambda p: (p.mandi())),
	"Cuci Tangan": (lambda p: (p.cuci_tangan())),
	"Membaca": (lambda p,a: (p.membaca(a))),
}

while not(p1.IsFinal()):
	masukan = input().split(" ")
	if (masukan[0] == "Tidur" or "Makan" or "Minum" or "Membaca"):
		choices.get(masukan[0])(p1, masukan[1])
	elif (masukan[0] == "Buang" and masukan[1] == "Air"):
		choices.get(masukan[0]+" "+masukan[1])(p1, masukan[2])
	else:
		choices.get(" ".join(masukan))(p1)
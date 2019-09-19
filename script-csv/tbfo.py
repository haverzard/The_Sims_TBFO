# KUMPULAN FUNGSI UNTUK STATE

# a: hygiene
# b: energy
# c: fun

# TIDUR
def tidur1(a, b, c):
	# tidur Siang
	if(b+10<=15):
		b+=10
	return "{}|{}|{}".format(a,b,c)

def tidur2(a, b, c):
	# tidur Malam
	if(b+15<=15):
		b+=15
	return "{}|{}|{}".format(a,b,c)


# MAKAN
def makan1(a, b, c):
	# makan Hamburger
	if(b+5<=15):
		b+=5
	return "{}|{}|{}".format(a,b,c)

def makan2(a, b, c):
	# makan Pizza
	if(b+10<=15):
		b+=10
	return "{}|{}|{}".format(a,b,c)

def makan3(a, b, c):
	# makan Steak and Beans
	if(b+15<=15):
		b+=15
	return "{}|{}|{}".format(a,b,c)


# MINUM
def minum1(a, b, c):
	# minum Air
	if(a-5>=0):
		a-=5
	return "{}|{}|{}".format(a,b,c)

def minum2(a, b, c):
	# minum Kopi
	if(a-10>=0) and (b+5<=15):
		a-=10; b+=5
	return "{}|{}|{}".format(a,b,c)

def minum3(a, b, c):
	# minum Jus
	if(a-5>=0) and (b+10<=15):
		a-=5; b+=10
	return "{}|{}|{}".format(a,b,c)


# BUANG AIR
def buangAir1(a, b, c):
	# buang air Kecil
	if(a+5<=15):
		a+=5
	return "{}|{}|{}".format(a,b,c)

def buangAir2(a, b, c):
	# buang air Besar
	if(a+10<=15) and (b-5>=0):
		a+=10; b-=5
	return "{}|{}|{}".format(a,b,c)


# BERSOSIALISASI KE KAFE
def kafe(a, b, c):
	# kafe
	if(a-5>=0) and (b-10>=0) and (c+15<=15):
		a-=10; b-=10; c+=15
	return "{}|{}|{}".format(a,b,c)


# BERMAIN MEDIA SOSIAL
def medsos(a, b, c):
	# medsos
	if(b-10>=0) and (c+10<=15):
		b-=10; c+=10
	return "{}|{}|{}".format(a,b,c)

# BERMAIN KOMPUTER
def komputer(a, b, c):
	# komputer
	if(c+15<=15):
		c+=15
	return "{}|{}|{}".format(a,b,c)

# MANDI
def mandi(a, b, c):
	# mandi
	if(a+15<=15) and (b-5>=0):
		a+=15; b-=5
	return "{}|{}|{}".format(a,b,c)


# CUCI TANGAN
def cuciTangan(a, b, c):
	# cuci tangan
	if(a+5<=15):
		a+=5
	return "{}|{}|{}".format(a,b,c)


# MENDENGARKAN MUSIK DI RADIO
def radio(a, b, c):
	# radio
	if(b-5>=0) and (c+10<=15):
		b-=5; c+=10
	return "{}|{}|{}".format(a,b,c)


# MEMBACA
def baca1(a, b, c):
	# koran
	if(b-5>=0) and (c+5<=15):
		b-=5; c+=5
	return "{}|{}|{}".format(a,b,c)

def baca2(a, b, c):
	# novel
	if(b-5>=0) and (c+10<=15):
		b-=5; c+=10
	return "{}|{}|{}".format(a,b,c)
from tbfo import *
# PEMBUATAN CSV

# HEADER
print "state/input,tidur1,tidur2,makan1,makan2,makan3,minum1,minum2,minum3,buangAir1,buangAir2,kafe,medsos,komputer,mandi,cuciTangan,radio,baca1,baca2"

# ISI
for a in range(0, 16, 5):
	for b in range(0, 16, 5):
		for c in range(0, 16, 5):
			s = ""
			s += "{}|{}|{}".format(a, b, c)
			s += "," + tidur1(a,b,c)
			s += "," + tidur2(a,b,c)
			s += "," + makan1(a,b,c)
			s += "," + makan2(a,b,c)
			s += "," + makan3(a,b,c)
			s += "," + minum1(a,b,c)
			s += "," + minum2(a,b,c)
			s += "," + minum3(a,b,c)
			s += "," + buangAir1(a,b,c)
			s += "," + buangAir2(a,b,c)
			s += "," + kafe(a,b,c)
			s += "," + medsos(a,b,c)
			s += "," + komputer(a,b,c)
			s += "," + mandi(a,b,c)
			s += "," + cuciTangan(a,b,c)
			s += "," + radio(a,b,c)
			s += "," + baca1(a,b,c)
			s += "," + baca2(a,b,c)
			print s
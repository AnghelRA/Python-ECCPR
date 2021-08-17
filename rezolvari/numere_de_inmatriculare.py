judete = ["AB", "AR", "AG", "B", "BC", "BH", "BN", "BT", "BV", "BR", "BZ", "CS", "CL", "CJ", "CT", "CV", "DB", "DJ", "GL", "GR", "GJ", "HR", "HD", "IL", "IS", "IF", "MM", "MH", "MS", "NT", "OT", "PH", "SM", "SJ", "SB", "SV", "TR", "TM", "TL", "VS", "VL", "VN"]
litere_mari = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numere_inmatriculare = []

verificare = True
while verificare == True:
	numar_inmatriculare = input()
	if numar_inmatriculare == "":
		verificare = False
	else:
		numar_inmatriculare = numar_inmatriculare.split(" ")
		numere_inmatriculare.append(numar_inmatriculare)

numere_inmatriculare = [x for y in numere_inmatriculare for x in y]

x = 0
while x < len(numere_inmatriculare):
	if numere_inmatriculare[x] not in judete:
		numere_inmatriculare.pop(x)
		numere_inmatriculare.pop(x)
		numere_inmatriculare.pop(x)
		x += 3
	x += 3

x = 0
while x < len(numere_inmatriculare):
	if len(numere_inmatriculare[x+1]) == 2 or len(numere_inmatriculare[x+1]) == 3:
		tmp = numere_inmatriculare[x+1]
		for y in tmp:
			if y.isdecimal() == False:
				numere_inmatriculare.pop(x)
				numere_inmatriculare.pop(x)
				numere_inmatriculare.pop(x)
	else:
		numere_inmatriculare.pop(x)
		numere_inmatriculare.pop(x)
		numere_inmatriculare.pop(x)
	x += 3

x = 0
while x < len(numere_inmatriculare):
	string3 = numere_inmatriculare[x+2]
	for y in string3:
		if y not in litere_mari: 
			numere_inmatriculare.pop(x)
			numere_inmatriculare.pop(x)
			numere_inmatriculare.pop(x)
	x += 3


numere_inmatriculare_final = []
x = 0
while x < len(numere_inmatriculare):
	numar_inmatriculare_final = numere_inmatriculare[x] + " " + numere_inmatriculare[x+1] + " " + numere_inmatriculare[x+2]
	numere_inmatriculare_final.append(numar_inmatriculare_final)
	x += 3

for x in numere_inmatriculare_final:
	print(x)
#Timp rezolvare 64 min
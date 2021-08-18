litere_mari = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numere = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26"]
verificare = ["01","02","03","04","05","06","07","08","09"]
modificare = {}
cod = dict(zip(numere,litere_mari))
x = 0
while x <len(verificare):
	modificare.update({verificare[x]: x+1})
	x += 1

mesaj_primit = input()
decodare = []
mesaj_decodat = []

x = 0
while x <len(mesaj_primit):
	tmp = mesaj_primit[x] + mesaj_primit[x+1]
	if tmp == "00":
		decodare.append(" ")
		x += 2
	elif int(tmp) > 26:
		tmp = mesaj_primit[x]
		decodare.append(tmp)
		x += 1
	else:
		decodare.append(tmp)
		x += 2

x = 0
while x < len(decodare):
	if decodare[x] in modificare:
		decodare[x] = modificare[decodare[x]]
		x += 1
	else:
		x += 1

decodare = [str(x) for x in decodare]

for x in decodare:
	if x in cod:
		tmp = cod[x]
		mesaj_decodat.append(tmp)
	elif x == ' ':
		mesaj_decodat.append(' ')

mesaj_decodat = "".join(mesaj_decodat)
print(mesaj_decodat)

# Timp rezolvare 53 min
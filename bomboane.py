zile_bani = int(input())
suma_de_bani = input()
suma_de_bani = suma_de_bani.split(" ")
bomboane = []
preturi = []
satisfactie = []

# Creez o lista care contine costul bomboanelor si nivelurile lor de satisfactie

x = 0
while x < zile_bani:
	bomboana = input()
	bomboana = bomboana.split()
	bomboane.append(bomboana)
	x += 1

bomboane = [x for y in bomboane for x in y]

# Impart lista bomboanelor in doua liste, una cu pretul bomboanelor si alta cu nivelul de satisfactie

x = 0
while x < len(bomboane):
	preturi.append(bomboane[x])
	satisfactie.append(bomboane[x+1])
	x += 2

# Calculez nivelul de satisfactie final conform cerintei

x = 0
satisfactie_totala = 0
zile_satisfactoare = []
while x < len(suma_de_bani):
	if int(suma_de_bani[x]) >= int(preturi[x]):
		rest = int(suma_de_bani[x]) - int(preturi[x])
	else: 
		rest = int(suma_de_bani[x])
	if rest < int(suma_de_bani[x]):
		satisfactie_totala += int(satisfactie[x])
		zile_satisfactoare.append(int(satisfactie[x]))
	elif rest == int(suma_de_bani[x]) and max(zile_satisfactoare) < int(satisfactie[x]):
		satisfactie_totala -= int(satisfactie[x])
	if x+1 < len(suma_de_bani):
		suma_de_bani[x+1] = int(suma_de_bani[x+1]) + rest
	else:
		break			
	x += 1

print(satisfactie_totala)

# Timp rezolvare 42 min
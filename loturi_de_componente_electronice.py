nr_loturi = int(input())
componente = []
numere = []

x = 0
while x < nr_loturi:
	nr_componente = int(input())
	numere.append(nr_componente)
	tipuri_componente = input()
	tipuri_componente = tipuri_componente.split(" ")
	componente.append(tipuri_componente)
	x += 1

x = 0
numar = 1
while x < len(componente):
	lot = [y for y in componente[x]]
	if lot.count('C') >= lot.count('T') and lot.count('R') >= lot.count('C') and lot.count('R') >= 1 and lot.count('C') >= 1 and lot.count('T') >= 1:
		lot_bun = numar
	else:
		numar += 1
	x += 1

print(lot_bun, max(numere))

# Timp rezolvare 24 min 

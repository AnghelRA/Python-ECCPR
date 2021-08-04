numar_zaruri = input()
suma_fete_zaruri = 21
lista_fete_vizibile = []
suma_fete_vizibile = []
lista_fete_ascunse = []

x = 0
while x < int(numar_zaruri):
	fete_vizibile = input()
	fete_vizibile = fete_vizibile.split(" ")
	fete_vizibile_int = [int(i) for i in fete_vizibile]
	lista_fete_vizibile.append(fete_vizibile_int)
	x += 1

for x in lista_fete_vizibile:
	fete_vizibile_zar = []
	fete_vizibile_zar = sum(x)
	suma_fete_vizibile.append(fete_vizibile_zar)

for i in suma_fete_vizibile:
	fata_ascunsa = suma_fete_zaruri - i
	lista_fete_ascunse.append(fata_ascunsa)

output = sum(lista_fete_ascunse)
print(output)

# Timp rezolvare 50 min
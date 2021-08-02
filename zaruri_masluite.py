numar_aruncari = int(input())
aruncari = []
zaruri = []

# Introduc aruncarile cu zarul intr-o lista

x = 0
while x < numar_aruncari:
	aruncare = input()
	aruncari.append(aruncare)
	x += 1

# Numar numarul de aparitii a fetei pentru fiecare aruncare

for x in aruncari:
	zar = aruncari.count(x)
	zaruri.append(zar)

# Verific daca zarurile sunt masluite sau nu

if numar_aruncari // 10 <= max(zaruri)-min(zaruri):
	print(0)
else:
	print(1)

# Timp rezolvare 26 min
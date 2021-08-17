n = int(input())
numere_intrare = input()
numere_intrare = numere_intrare.split(" ")
numere_intrare.sort()
numere_intrare = numere_intrare[::-1]

tmp = True
aparitii = []
for x in numere_intrare:
	if tmp == True:
		aparitie = numere_intrare.count(x)
		aparitii.append(aparitie)
		tmp = x
	elif x == tmp:
		tmp = x
	else:
		aparitie = numere_intrare.count(x)
		aparitii.append(aparitie)
		tmp = x

verificare = 0
x = 0
while x < len(aparitii):
	if aparitii[x] % 2 == 1:
		verificare += 1 
	x += 1 

# Verific daca numarul este palindrom
tmp = 0
if verificare > 1:
	print("0")
else:
	verificare = 0
	for x in numere_intrare:
		if numere_intrare.count(x) == 1:
			tmp = x
			numere_intrare.pop(verificare)
		elif numere_intrare.count(x) == 3:
			tmp = x
			numere_intrare.pop(verificare)
		else:
			verificare += 1 

	first_half = ""
	x = 0
	while x < len(numere_intrare):
		first_half = first_half + numere_intrare[x]
		x += 2

	second_half = ""
	x = 0
	while x < len(numere_intrare):
		second_half = second_half + numere_intrare[x+1]
		x += 2

	second_half = second_half[::-1]
	if tmp == 0:
		numar = first_half + second_half
		print(numar)
	else:
		numar = first_half + tmp + second_half
		print(numar)
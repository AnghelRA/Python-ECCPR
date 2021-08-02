n = int(input())
numar_decimal = []

binar = bin(n).replace("0b","")                                    # Transformare decimal in binar
numar_binar = list(binar)                                          # Transform numarul binar intr-o lista
                                                                   # Rezolv permutarile numarului binar si le convertesc in numere decimale pe care le adaug intr-o lista
lungime_lista = len(numar_binar) - 1
x = 0
while x < len(binar):
	permutare = "".join(numar_binar)
	numar = int(permutare,2)
	numar_decimal.append(numar)
	numar_binar.insert(0 , numar_binar[lungime_lista])
	numar_binar.pop()
	x += 1

print(max(numar_decimal))                                          # Din lista cu numere decimale scot maximul

# Timp rezolvare 45 min
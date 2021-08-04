nr_biti = int(input())
cod_binar = input()
secventa1 = 0
secventa2 = 0
secventa3 = 0
secventa4 = 0
secventa = []

# Verific de cate ori exista secventele 00 01 10 11
x = 0
y = 2
while x < nr_biti:
	doi_biti = cod_binar[x:y]
	if '00' in doi_biti:
		secventa1 +=1
	elif '01' in doi_biti:
		secventa2 += 1
	elif '10' in doi_biti:
		secventa3 += 1
	elif '11' in doi_biti:
		secventa4 += 1
	x += 2
	y += 2

secventa.append(secventa1)
secventa.append(secventa2)
secventa.append(secventa3)
secventa.append(secventa4)

R1 = max(secventa)/min(secventa)

# Calculez R2
if cod_binar.count('1') >= cod_binar.count('0'):
	R2 = cod_binar.count('1') / cod_binar.count('0')
else:
	R2 = cod_binar.count('0') / cod_binar.count('1')

print(R1, R2)

# Verific daca codul e random sau nu
if R1 <= 1.1 and R2 <= 1.1:
	print('1')
else:
	print('0')

#Timp rezolvare 25 min
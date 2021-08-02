n = input()
maini_jucate = []
carte = {}
afisat = False

# Creez o lista care contine mainile jucate

x = 0
while x < int(n):
	mana_jucata = input()
	maini_jucate.append(mana_jucata)
	x += 1

# Verific daca exista o carte trucata si o afiseaza

for x in maini_jucate:
	if x in carte:
		carte[x] += 1
	else:
		carte[x] = 1

	if carte[x] >= 3 and afisat == False:
		print(x)
		afisat = True

# Daca nu exista carti trucate afiseaza JOC OK 

if afisat == False:
	print("JOC OK")

#Timp rezolvare 39 min

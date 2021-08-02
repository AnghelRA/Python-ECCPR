n = input()
maini_jucate = []
afisat = False

# Creez o lista care contine mainile jucate

x = 0
while x < int(n):
	mana_jucata = input()
	maini_jucate.append(mana_jucata)
	x += 1

# Verific daca exista o carte trucata si o afiseaza

for x in maini_jucate:
	carte = x
	if maini_jucate.count(carte) >= 3 and afisat == False:
		print(carte)
		afisat = True

# Daca nu exista carti trucate afiseaza JOC OK 

if afisat == False:
	print("JOC OK")

#Timp rezolvare 39 min
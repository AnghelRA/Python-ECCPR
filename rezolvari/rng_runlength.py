nr_biti = int(input())
biti = input()
secvente_biti = []
nr_aparitii = []
verificare = []

biti = biti + "0"
tmp = 0
x = 0
while x < nr_biti:
	if biti[x] == "1":
		tmp += int(biti[x])
		if biti[x+1] == "0":
			secvente_biti.append(tmp)
			tmp = 0
			x += 1
		else: 
			x += 1
	else:
		x += 1

x = 1
while x < max(secvente_biti)+1:
	tmp = secvente_biti.count(x)
	nr_aparitii.append(tmp)
	x += 1
print(nr_aparitii)

x = 0
while x < len(nr_aparitii)-1:
	if nr_aparitii[x] >= nr_aparitii[x+1]:
		verificare.append("1")
		x += 1
	else:
		verificare.append("0")
		x += 1

if "0" in verificare:
	print("0")
else:
	print("1")

# Timp rezolvare 60 min
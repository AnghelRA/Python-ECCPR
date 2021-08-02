date_intrare = input()
date_intrare = date_intrare.split(" ")
numar_studenti = int(date_intrare[0])
numar_discipline = int(date_intrare[1])
numar_burse_merit_disponibile = int(date_intrare[2])
studenti = []
medii_studenti = []
medii_finale_studenti =[]
integralisti = []
catalog = {}

x = 0
while x < numar_studenti:
	nume_student = input()
	studenti.append(nume_student)
	medii_student = input()
	medii_student = medii_student.split(" ")
	medii_studenti.append(medii_student)
	x += 1

medii_studenti = [int(x) for y in medii_studenti for x in y]

x = 1
while x < len(medii_studenti):
	if medii_studenti[x-1] > 5 and medii_studenti[x] > 5 and medii_studenti[x+1] > 5:
		integralist = (medii_studenti[x-1] + medii_studenti[x] + medii_studenti[x+1])
		integralisti.append(integralist)
		medie_finala_student = integralist / 3
		medii_finale_studenti.append(medie_finala_student)
	x += 3

x = 0
while x < len(studenti):
	catalog[studenti[x]] = medii_finale_studenti[x]
	x += 1

medie_performanta = max(x for x in catalog.values())

x = 0
nr_burse_merit = 0
while x < len(medii_finale_studenti):
	if nr_burse_merit < numar_burse_merit_disponibile:
		if medii_finale_studenti[x] > 8:
			nr_burse_merit += 1
		else:
			nr_burse_merit == nr_burse_merit
	else:
		break
x += 1
print(medii_finale_studenti)
print(nr_burse_merit)
print({x:catalog[x] for x in catalog for x in catalog if catalog[x] == medie_performanta})

# Timp rezolvare 64 min
def punctaj(meciuri):
	scor = 0
	x = 0
	while x < len(meciuri):
		if meciuri[x+1] > meciuri[x+2]:
			scor += 3
		elif meciuri[x+1] == meciuri[x+2]:
			scor += 1
		x += 3
	return scor

nr_echipe_participant = int(input())
nr_meciuri_disputate = int(input())
meciuri = []
tari = []
scor_final = []

x = 0
while x < nr_meciuri_disputate:
	meci = input()
	meci = meci.split(" ")
	meciuri.append(meci)
	x += 1

meciuri = [x for y in meciuri for x in y]
meciuri.remove('-')

x = 0
while x < len(meciuri):
	if meciuri[x] not in tari:
		tari.append(meciuri[x])
	x += 3

scor = punctaj(meciuri)

print(scor)

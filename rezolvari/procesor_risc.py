nr_instructiuni = int(input())
reg = []
instructiuni = []

x = 0
while x < nr_instructiuni:
	instructiune = input()
	instructiune = instructiune.split(" ")
	instructiuni.append(instructiune)
	x += 1

instructiuni = [x for y in instructiuni for x in y]

x = 0
index = 0
while x < len(instructiuni):
	if instructiuni[x] == 'lconst':
		index += 1
		reg.append(x)
		if int(instructiuni[x+1]) > len(reg) - 1:
			reg.append(x)
			reg[int(instructiuni[x+1])] = int(instructiuni[x+2])
		else:
			reg[int(instructiuni[x+1])] = int(instructiuni[x+2])
	elif instructiuni[x] == 'print':
		index += 1
		print(int(reg[int(instructiuni[x+1])]))		
	elif instructiuni[x] == 'add':
		index += 1
		suma = int(reg[int(instructiuni[x+2])]) + int(reg[int(instructiuni[x+3])])
		reg[int(instructiuni[x+1])] = str(suma)
	elif instructiuni[x] == 'mul':
		index += 1
		produs = int(reg[int(instructiuni[x+2])]) * int(reg[int(instructiuni[x+3])])
		reg[int(instructiuni[x+1])] = str(produs)
	elif instructiuni[x] == 'div':
		index += 1
		try:
			diviziune = int(reg[int(instructiuni[x+2])]) / int(reg[int(instructiuni[x+3])])
			reg[int(instructiuni[x+1])] = int(diviziune)
		except:
			print("Exception: line", index)
			break
		
	x += 1

# Timp rezolvare 1h 15 min
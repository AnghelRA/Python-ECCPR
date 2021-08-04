nr_cifre = int(input())
cifre = input()
cifre = cifre.split(" ")
tmp = cifre
numere = []
palindrom = []

x = 0
while x < len(cifre):
	numar = "".join(tmp)
	numere.append(numar)
	tmp.insert(len(tmp), cifre[x])
	tmp.pop(0)
	x += 1

print(numere)
for x in numere:
	if x == x[::-1]:
		palindrom.append(x)

if palindrom == []:
	print("0")
else:
	print(max(palindrom))
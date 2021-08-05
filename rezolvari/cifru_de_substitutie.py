text = input()
cifru = input()
text_nou = []
caractere = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']

cifru = cifru.replace(',',' ')
cifru = cifru.split(' ')
cifru = [x for y in cifru for x in y]

text = [x for y in text for x in y]


x = 0
while x < len(text):
	y = 0
	check = False
	while y < len(cifru):
		if text[x] == cifru[y]:
			text_nou.append(cifru[y+1])
		elif text[x] != cifru[y] and text[x] not in caractere and check == False:
			text_nou.append(text[x])
			check = True
		y += 2
	x += 1
	
text_nou = "".join(text_nou)
print(text_nou)

# Timp rezolvare 1h 12 min
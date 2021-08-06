ora = input()
n = input()
x = 0
lista_filme = []
filme_aceeasi_ora = []

####################################################
# Introduc filmele de la cinematograf intr-o lista
####################################################

while x < int(n):
	film = input()
	film = film.split(" ")
	lista_filme.append(film)
	x += 1
lista_filme = [film for filme in lista_filme for film in filme]
x = 0

########################################################
# Modific orele filmelor din lista pentru a elimina ":"
########################################################

while x < len(lista_filme):
	ore = lista_filme[x]
	ore = ore.replace(":","")
	lista_filme[x] = ore
	x += 3
                                                                      
ora = ora.replace(":","")
lista_filme_disponibile = []
x = 0

########################################################################################################
#Creez o lista noua care sa contina doar filmele care se difuzeaza dupa ora la care am ajuns la cinema
########################################################################################################

while x < len(lista_filme):
	if int(lista_filme[x]) >= int(ora):
		ora_disponibila = lista_filme[x]
		lista_filme_disponibile.append(ora_disponibila)
		pret_disponibil = lista_filme[x+1]
		lista_filme_disponibile.append(pret_disponibil)
		film_disponibil = lista_filme[x+2]
		lista_filme_disponibile.append(film_disponibil)
	else:
		x = x
	x += 3

x = 0
minim = lista_filme_disponibile[0]
pret_minim = lista_filme_disponibile[1]

#############################################################################################################
# Verifica care ora e cea mai apropiata de ora la care am ajuns
# Daca sunt mai multe filme la aceeasi ora compara preturile acestora pentru a afla care are pretul mai mic
#############################################################################################################

while x < len(lista_filme_disponibile):
        if int(minim) >= int(lista_filme_disponibile[x]):
                minim = lista_filme_disponibile[x]
                
        if int(minim) == int(lista_filme_disponibile[x]) and int(pret_minim) >= int(lista_filme_disponibile[x+1]):
                pret_minim = lista_filme_disponibile[x+1]
        x += 3

x = 0
while x < len(lista_filme_disponibile):
        if int(lista_filme_disponibile[x]) == int(minim):
               pret_minim = lista_filme_disponibile[x+1]
        x += 3

x = 0
while x < len(lista_filme_disponibile):
        if int(minim) == int(lista_filme_disponibile[x]) and int(pret_minim) >= int(lista_filme_disponibile[x+1]):
               pret_minim = lista_filme_disponibile[x+1]
        x += 3

#######################################################################################################
# Returneaza filmul care a se difuzeaza la cea mai apropiata ora de cea care am ajuns si e mai ieftin
#######################################################################################################



x = 0
while x < len(lista_filme_disponibile):
	if lista_filme_disponibile[x] == minim and lista_filme_disponibile[x+1] == pret_minim:
		cel_mai_recent_film = lista_filme_disponibile[x+2]
		break
	x += 3

print(cel_mai_recent_film)

lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 4, 5]
lst_3 = [1, 6, 2, 3, 4, 5]
lst_4 = [10, 5, 7, 12, 9, 2, 1]
lst_5 = [4, 9, 1, 6, 8, 3, 7, 2, 5]

def renverse(G):#Code by h4ck3rM4n°4 valide
	return G[::-1]

def r(T):#Code by ChatGPT................................................................................................
    n = len(T)
    for i in range(n//2):
        T[i], T[n-1-i] = T[n-1-i], T[i]
    return T

def renverse(C):#Code by h4ck3rM4n°4 non valide par Mr
	cpt = -1
	x = []
	for i in range(len(C)):
		x.append(C[cpt])
		cpt -= 1
	return x

def somme_d_une_liste(H):#Code by h4ck3rM4n°4
	nbr = 0
	for j in H:
		nbr += j
	return nbr

def maximum(J):#Code by h4cK3rM4n°4	#
	max_value = J[0]				#
	for x in range(len(J)):			#
		while max_value < J[x]:		#
			max_value = J[x]		#
	return max_value				#
									#	Les deux fonctions ont pour but de trouver l'indice du maximum dans une liste!
def indice_maximum(K):
	for i in range(len(K)):
		if K[i] == maximum(K):
			return i
print(indice_maximum(lst_4))
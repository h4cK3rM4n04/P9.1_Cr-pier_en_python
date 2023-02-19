lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 4, 5]
lst_3 = [1, 6, 2, 3, 4, 5]

def renverse(T):#Code by h4ck3rM4n°4 valide
	return T[::-1]

def r(T):#Code by ChatGPT................................................................................................
    n = len(T)
    for i in range(n//2):
        T[i], T[n-1-i] = T[n-1-i], T[i]
    return T

def renverse(T):#Code by h4ck3rM4n°4 non valide par Mr
	cpt = -1
	x = []
	for i in range(len(T)):
		x.append(T[cpt])
		cpt -= 1
	return x

def somme_d_une_liste(T):#Code by h4ck3rM4n°4
	cpt = 0
	nbr_max = 0
	nbr = 0
	for j in T:
		nbr += j
	return nbr
print(somme_d_une_liste(lst_3))
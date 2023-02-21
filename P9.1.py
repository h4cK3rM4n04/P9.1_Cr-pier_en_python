import random

lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 4, 5]
lst_3 = [1, 6, 2, 3, 4, 5]
lst_4 = [10, 5, 7, 12, 9, 2, 1]
lst_5 = [4, 9, 1, 6, 8, 3, 7, 2, 5]
lst_6 = [11, 7, 13, 12, 14, 16, 19, 18, 9, 3, 5, 17, 1, 20, 10, 8, 6, 4, 2, 15]
lst_7 = [2, 1, 3]

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

#=========Code by h4cK3rM4n°4=======#
def maximum(J):						#
	max_value = J[0]				#
	for x in range(len(J)):			#
		while max_value < J[x]:		#
			max_value = J[x]		#
	return max_value				#
									#	Les deux fonctions ont pour but de trouver l'indice du maximum dans une liste!
def indice_maximum(K):				#
	for i in range(len(K)):			#
		if K[i] == maximum(K):		#
			return i  				#
#===================================#

def tas_de_crepes(n):#Code by h4cK3rM4n04
	v = [x for x in range(1, n+1)]
	return v

def melange_crepier(T):#Code in JupyterHub
	random.shuffle(T)
	return T


def max_indice_0(T):
    v = [x for x in renverse(T)]
    lv = []
    if v[0] != maximum(v):
        lv = v[0]
        b = indice_maximum(v)
        v[0] = maximum(v)
        v[b] = lv
    return v

def crepier(liste):#Code by ChatGPT................................................................................................
    n = len(liste)
    for i in range(n):
        for j in range(0, n-i-1):
            if liste[j] < liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
    return liste

def crepier(T):#Code by h4cK3rM4n04
	pass
lst_1 = [1, 2, 3, 4]
lst_2 = [1, 2, 3, 4, 5]
lst_3 = [1, 6, 2, 3, 4, 5]

def renverse(T):#Code by h4ck3rM4n°4
	return T[::-1]

def r(T):#Code by ChatGPT................................................................................................
    n = len(T)
    for i in range(n//2):
        T[i], T[n-1-i] = T[n-1-i], T[i]
    return T

def renverse(T):#Code by h4ck3rM4n°4
	cpt = -1
	x = []
	for i in range(len(T)):
		x.append(T[cpt])
		cpt -= 1
	return x

def indice_maximum(T):#Code by h4ck3rM4n°4
	cpt = 0
	nbr_max = 0
	for j in range(len(T)):
		pass
print(indice_maximum(lst_3))
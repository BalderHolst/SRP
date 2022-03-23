def insertionsort(l):
	for i in range(1,len(l)):
		element = l[i]

		if element < l[0]:
			for j in range(i,0,-1):
				l[j] = l[j-1]
			l[0] = element
		else:
			j = i
			while(l[j-1]>element):
				l[j] = l[j-1]
				j -= 1
			l[j] = element
	return(l)

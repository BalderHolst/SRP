def mergesort(l):
	if len(l) <= 1:
		return(l)
	else:
		return(merge(mergesort(l[:len(l)//2]),mergesort(l[len(l)//2:])))

def merge(a,b):
	c = []
	while True:
		if (len(a) == 0):
			return(c + b)
		elif (len(b) == 0):
			return(c + a)
		elif (a[0] <= b[0]):
			c.append(a[0])
			a.pop(0)
		else:
			c.append(b[0])
			b.pop(0)

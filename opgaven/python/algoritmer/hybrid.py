from insertionsort import *

n0 = 30

def hybrid(l):
	if len(l) <= n0:
		return(insertionsort(l))
	else:
		return(merge(hybrid(l[:len(l)//2]),hybrid(l[len(l)//2:])))

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

if __name__ == "__main__":
	r = hybrid([1,4,25,2,7,2,1536,3,7,25,1,4,6,36,2,5,36,2,6,3,7,47,67,8,69,78,9,46,3,52,31,34,23,4,3,4,5675,67,567,67,84,65,3,52,343,456,46,456,123])
	print(r)

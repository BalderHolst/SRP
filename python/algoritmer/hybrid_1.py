from insertionsort import *
from mergesort import *

n0 = 10

def hybrid_1(l):
    if(len(l) <= n0):
        return(insertionsort(l))
    return(mergesort(l))


if __name__ == "__main__":
    l1 = [4,15,25,2,636,25,2,413]
    l2 = [1,4,2,14,1,25,35,24,1,242,5,3,64,74,6,34,23,13,2,41,32,42,5,35,63,24,1]

    print(l1)
    print(l2)
    print(hybrid_1(l1))
    print(hybrid_1(l2))

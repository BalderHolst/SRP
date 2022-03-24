import random
import time
import pandas as pd
import os

import sys
sys.path.insert(1, 'algoritmer')
from mergesort import *
from insertionsort import *

def test(fun,l):
	start_time = time.perf_counter()



	fun(l)

	return(time.perf_counter() - start_time)


def createRandomList(n):
	return([random.randint(0,1000) for i in range(n)])


def makeIfNeeded(dir_path):
	if(os.path.isdir(dir_path) == False):
		print(f"made dir: {dir_path}")
		os.mkdir(dir_path)
	return(dir_path)


def newVersionNumber(dir_path,extention):
	file_names = os.listdir(dir_path)
	version = 0

	thisfilename = f"{version}{extention}"

	while(thisfilename in file_names):
		version += 1
		thisfilename = f"{version}{extention}"

	return(thisfilename)


def fullTest(functions):

	trials = 10

	data_dir = "data/"
	version_number = newVersionNumber(data_dir,"")

	for function in functions:

		ns = []
		times = []

		for trial in range(0,trials):

			for i in range(0,80):
				n = round(pow(1.1,i))

				print(f"function=\"{function.__name__}\":   Trial: [{trial+1}/{trials}]    {i=},{n=}")

				l = createRandomList(n)

				ns.append(n)
				times.append(test(function,l))





			# trials_dir = newVersionNumber(data_dir)
				

			data = {
				"n": ns,
				"t": times
				}

			version_dir = makeIfNeeded(data_dir + version_number + "/")
			algorithm_dir = makeIfNeeded(version_dir + function.__name__ + "/")
			full_path = algorithm_dir + newVersionNumber(algorithm_dir,".csv")

			print(f"\ndata saved to \"{full_path}\"\n")

			pd.DataFrame(data).to_csv(full_path,index = False)


if __name__ == "__main__":
	functions = [mergesort,insertionsort]
	print("hello")
	print("helo")
	#fullTest(functions)
	print("hello")

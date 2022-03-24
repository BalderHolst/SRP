import random
import time
import pandas as pd
import os

import sys
sys.path.insert(1, './algoritmer')
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

	trials = 10	 # hvor mange datapunkter pr. n-værdir

	data_dir = "../data/"
	version_number = newVersionNumber(data_dir,"")

	seed = time.time()
	print(f"Seed: {seed}")

	for function in functions:

		ns = []	 # i denne liste gemmes antallet af elementer at den liste som algoritmen sorterer for hvert datapunkt.
		times = []  # i denne liste gennes den tid det tager at sorterer listen med n elementer
	
		random.seed(seed) # Bruger det samme frø til test at hver algoritme. På den måde er det de samme pseudo-tilfældige liste som algoritmerne sorterer

		for trial in range(0,trials):   # Vi laver testen et antal (trials) gange pr. n-værdi

			for i in range(0,80):	   # En lykke der køre et abitrært antal gange (jo højere en i-værdi jo højere maks antal elementer i listen)
				n = round(pow(1.1,i))   # Jeg bruger en potensfunktion til at få flere datapunker tættere på y-aksen og færre lange oberationer (pga. lange liste)

				print(f"function=\"{function.__name__}\":   Trial: [{trial+1}/{trials}]	{i=},{n=}")  # lidt feedback

				l = createRandomList(n)		 # gennererer en tilfældig liste

				ns.append(n)					# gem størrelsen af listen der skal sorteres
				times.append(test(function,l))  # gen den tid det tager at sortere listen





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

	fullTest(functions)

import random
import time
import pandas as pd
import os


# Denne funktion timer køretiden af en funktion med input l og returnerer funktionen køretid i milisekunder
def test(fun,l):
	start_time = time.perf_counter()

	fun(l)

	return(time.perf_counter() - start_time)

# Denne funktion returnerer en liste af tilfældige tal mellem 0 og 1000, med n elementer
def createRandomList(n):
	return([random.randint(0,1000) for i in range(n)])

# Laver en mappe i filsystemet hvis der ikke allerede er en med stien 
def makeIfNeeded(dir_path):
	if(os.path.isdir(dir_path) == False):
		print(f"made dir: {dir_path}")
		os.mkdir(dir_path)
	return(dir_path)

# Finder det næste versionsnummer for til navngivning af fil på baggrund af indholdet i en folder
def newVersionNumber(dir_path,extention):
	file_names = os.listdir(dir_path)
	version = 0

	thisfilename = f"{version}{extention}"

	while(thisfilename in file_names):
		version += 1
		thisfilename = f"{version}{extention}"

	return(thisfilename)

# Dette er funktionen der tester en liste med funktioner og gemmer deres køretider
def fullTest(functions):


	data_dir = "../data/"
	version_number = newVersionNumber(data_dir,"")

	# hvor mange datapunkter pr. n-værdi
	trials = 10	

	# Bruger tidspunkt som frø til pseudotilfældige tal.
	seed = time.time()
	print(f"Seed: {seed}")

	for function in functions:

		# i denne liste gemmes antallet af elementer at den liste som algoritmen sorterer for hvert datapunkt.
		ns = []	
		# i denne liste gennes den tid det tager at sorterer listen med n elementer
		times = [] 
	
		# Bruger det samme seed til test at hver algoritme. på den måde er det de samme pseudo-tilfældige liste som algoritmerne sorterer
		random.seed(seed) 

		# Vi laver testen et antal (trials) gange pr. n-værdi
		for trial in range(0,trials):   

			# En lykke der køre et abitrært antal gange (jo højere en i-værdi jo højere maks antal elementer i listen)
			for i in range(0,80):	   

        	# Jeg bruger en potensfunktion til at fa flere datapunker tættere på y-aksen og færre lange oberationer (pga. lange liste)
				n = round(pow(1.1,i))   

				# lidt feedback
				print(f"function=\"{function.__name__}\":   Trial: [{trial+1}/{trials}]	{i=},{n=}")  

				# gennererer en tilfældig liste med længden n
				l = createRandomList(n)		

				# gem størrelsen af listen der skal sorteres
				ns.append(n)				
				# gem den tid det tager at sortere listen
				times.append(test(function,l))  

				
            # gemmer data
			data = {
				"n": ns,
				"t": times
				}

			version_dir = makeIfNeeded(data_dir + version_number + "/")
			algorithm_dir = makeIfNeeded(version_dir + function.__name__ + "/")
			full_path = algorithm_dir + newVersionNumber(algorithm_dir,".csv")

			print(f"\ndata saved to \"{full_path}\"\n")

			pd.DataFrame(data).to_csv(full_path,index = False)



library(ggplot2)
library(plyr)

#working dir
setwd("/home/Balder/Documents/Skole/Gym/SRP/data/9")

#dir = "1"
algorithm_dirs = list.files()

M = NULL
for (j in 1:length(algorithm_dirs)){
	algorithm_dir = algorithm_dirs[j]

	files = list.files(algorithm_dir)

	for (i in 1:length(files)){
		file_path = paste(algorithm_dir,files[i],sep="/")
		print(file_path)
		m = read.csv(file_path,header=TRUE,sep=",")
		m$Algorithm = algorithm_dirs[j]
		M = rbind(M, m)
	}

}

M$algorithm = factor(M$Algorithm)
summary(M)

# punktmængder for hver algoritme
m_merge = subset(M,M$algorithm=="mergesort")
m_insertion = subset(M,M$algorithm=="insertionsort")

# laver modeller
model_merge = nls(t~a*n*log2(n), data=m_merge, start=list(a=0.000001))
model_insertion = nls(t~a*n^2 + b*n + c, data=m_insertion, start=list(a=1,b=1,c=1))


# Sætter ny path til hvor outputtet skal være
setwd("/home/Balder/Documents/Skole/Gym/SRP/img")

# laver modelerede v?rdier for hver n
m_merge$model = predict(model_merge)

m_merge$residual = resid(model_merge)

# kombinerer de to
M = m_merge

summary(M)


farve = c("#3a6ced","#ff9b00")


ggplot(M, aes(x=log10(model), y=residual, colour=black)) +
	geom_hline(yintercept = 0)+
	geom_point(size=1.5,alpha=0.2,shape=19) +
	labs(x="Log10 af Modellens Forudsigelse", y="residualer") +
	facet_wrap(~algorithm,scales="free",ncol=1) +
	guides(colour = guide_legend(override.aes = list(alpha = 1))) + # lav legend alpha 1
	theme_bw() +
		theme(legend.position="top",legend.title = element_blank())


	ggsave("forsidePlot.png",width=8,height=6,scale=0.7)


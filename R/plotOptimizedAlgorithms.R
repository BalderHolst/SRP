library(ggplot2)
#library(tikzDevice)

#working dir
setwd("/home/Balder/Documents/Skole/Gym/SRP/data/the_one")

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

# gemmer r2-værdierne i to filer
writeLines(toString(round(with(m_merge,cor(t,n)),digits=3)),"r2-merge.txt")
writeLines(toString(round(with(m_insertion,cor(t,n)),digits=3)),"r2-insertion.txt")
print("r2 saved to files")


# laver modelerede v?rdier for hver n
m_merge$model = predict(model_merge)
m_insertion$model = predict(model_insertion)

m_merge$residual = resid(model_merge)
m_insertion$residual = resid(model_insertion)

# kombinerer de to
M = rbind(m_merge,m_insertion)

summary(M)


ggplot(M, aes(x=n, y=t, colour=Algorithm)) +
	geom_point(size=1.5,alpha=0.1,shape=19) +
	geom_line(aes(x=n, y=model,color=Algorithm), size=2, alpha=0.6) +
	labs(title="To Sorteringsalgoritmer") +
	theme(legend.position = c(.9, .9)) + # virker ikke!!
	guides(colour = guide_legend(override.aes = list(alpha = 1))) + # lav legend alpha 1
	theme_bw()

	ggsave("toAlgoritmer.png")

	ggplot(M, aes(x=log10(model), y=residual, colour=Algorithm)) +
		geom_point(size=1.5,alpha=0.1,shape=19) +
		labs(title="Residualer") +
		facet_wrap(~algorithm,scales="free",ncol=1) +
		theme_bw() +
		theme(legend.position="none")
	ggsave("toAlgoritmerResidual.png")

	C = data.frame(
		       Algorithm = unique(M$Algorithm),
		       R2 = c(with(m_merge, cor(t,n)), with(m_insertion, cor(t,n)))
	)
	
	ggplot(subset(M,n <= 100), aes(x=n, y=t, colour=Algorithm)) +
	  geom_point(size=1.5,alpha=0.08,shape=19) +
	  labs(title="To Sorteringsalgoritmer") +
	  guides(colour = guide_legend(override.aes = list(alpha = 1))) + # lav legend alpha 1
	  theme_bw()
	
	ggsave("toAlgoritmerZoomed.png")

	write.table(C, "r2.txt", quote=FALSE,sep="\t", row.names=FALSE)



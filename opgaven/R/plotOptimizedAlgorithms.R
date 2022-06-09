library(ggplot2)
library(plyr)
#library(tikzDevice)

#working dir
setwd("/home/Balder/Documents/Skole/Gym/SRP/data/the_second_one")

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
m_hybrid = subset(M,M$algorithm=="hybrid")

# laver modeller
model_merge = nls(t~a*n*log2(n), data=m_merge, start=list(a=0.000001))
model_hybrid = nls(t~a*n*log2(n), data=m_hybrid, start=list(a=0.000001))
  

# Sætter ny path til hvor outputtet skal være
setwd("/home/Balder/Documents/Skole/Gym/SRP/img")

# gemmer r2-værdierne i to filer
#writeLines(toString(round(with(m_merge,cor(t,n)),digits=3)),"r2-merge.txt")
#writeLines(toString(round(with(m_insertion,cor(t,n)),digits=3)),"r2-insertion.txt")
#print("r2 saved to files")


# laver modelerede v?rdier for hver n
m_merge$model = predict(model_merge)
m_hybrid$model = predict(model_hybrid)


m_merge$residual = resid(model_merge)
m_hybrid$residual = resid(model_hybrid)

# kombinerer de to
M = rbind(m_merge,m_hybrid)

summary(M)


farve = c("forestgreen","#ff9b00")


ggplot(M, aes(x=n, y=t, colour=Algorithm)) +
	geom_point(size=1.5,alpha=0.1,shape=19) +
	labs(y="t (s)")+
  scale_color_manual(values = farve)+
	guides(colour = guide_legend(override.aes = list(alpha = 1))) + # lav legend alpha 1
	theme_bw()+
  theme(legend.position="top",legend.title = element_blank())

	ggsave("toMergesort.png",width=5,height=4,scale=1.3)

# Laver ges data.frame
f = function(x) {
	data.frame(
		   t = mean(x$t)
	)
}

gns = ddply(subset(M,n <= 100), .(Algorithm, n), f)	

ggplot(subset(M,n <= 100), aes(x=n, y=t, colour=Algorithm)) +
	geom_line (size=1.5, data=gns) +
	geom_point(size=1.5,alpha=0.1,shape=19) +
	labs(y="t (s)")+
  scale_color_manual(values = farve)+
	guides(colour = guide_legend(override.aes = list(alpha = 1))) + # lav legend alpha 1
	theme_bw()+
  theme(legend.position="top",legend.title = element_blank())

	ggsave("toMergesortZoomed.png",width=5,height=4,scale=1.3)


	ggplot(M, aes(x=log10(model), y=residual, colour=Algorithm)) +
	  geom_hline(yintercept = 0)+
	  scale_color_manual(values = farve)+
		geom_point(size=1.5,alpha=0.1,shape=19) +
		labs(x="Log10 af Modellens Forudsigelse", y="residualer") +
		facet_wrap(~algorithm,scales="free",ncol=1) +
	  guides(colour = guide_legend(override.aes = list(alpha = 1))) + # lav legend alpha 1
		theme_bw() 
#theme(legend.position="bottom",legend.title = element_blank())
	
	  
	ggsave("toMergesortResidual.png",width=8,height=6)



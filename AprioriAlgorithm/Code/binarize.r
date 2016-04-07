#data<-read.csv("./Data/Car/car.txt",header=FALSE,sep=",")
#colnames(data)<-c('buying','maint','doors','persons','lug_boot','safety','class')
#Removing maint,lug_boot,persons 
#data<-data[,-c("maint","persons","lug_boot","safety")]
#data<-data[,-c(2,4,5,6)]

#data<-read.csv("./Data/nursery/nursery.data.txt",header=FALSE,sep=",")
#colnames(data)<-c('parents','has_nurs','form','children','housing','finance','social','health')
#binarize(data)
binarize<-function(data,dataset){
  df=as.data.frame(matrix(nrow=nrow(data)))
  
  for (i in 1:ncol(data)){
    df<-cbind(df,(model.matrix(~data[,i]+0,data=data)))
  }
  
  #removing NA column
  df<-df[,-1]
  
  #cleaning colnames names
  for (i in 1:ncol(df)){
    colnames(df)[i]<-gsub(pattern="[[:punct:]]", colnames(df)[i], replacement=" ") 
    colnames(df)[i]<-gsub(pattern="data", colnames(df)[i], replacement=" ")
    colnames(df)[i]<-gsub(pattern="\\s", colnames(df)[i], replacement=" ") 
    #colnames(df)[i]<-gsub(pattern="\\d", colnames(df)[i], replacement=" ")
  }
  write.csv(df,file=paste("./Data/", dataset,"/binarize_",dataset,".csv",sep=""),row.names=FALSE,sep=",")
  return (df)
}

library(reshape2) 


bubbles <- read.csv("bubbles.csv")


bubbleslong <- melt(bubbles,id.vars = c("CONCELHO","LAT","LONG"),
             variable.name = "DATA",value.name = "INC")
             
write.csv(bubbleslong,"bubbleslong.csv",row.names = TRUE)


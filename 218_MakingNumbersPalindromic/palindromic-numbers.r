library(gmp)
palin = function(ns){
    rv <- function(s){return(gsub("(?<![0-9])0+", "", paste(rev(strsplit(toString(s),NULL)[[1]]),collapse=''), perl=1))}
    n <- as.bigz(ns); k <- 0
    while (toString(n) != rv (n)) {n <- as.bigz(rv(n))+n; k<-k+1}
    message(paste0(toString(ns)," gets palindromic after ", k ," steps: ",toString(n)))
}
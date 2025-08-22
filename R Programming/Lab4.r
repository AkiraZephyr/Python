num <- 9
fact <- 1
if (num < 0){
  cat("Factorial is not defined for negative numbers")
} else if (num == 0) {
  cat("Factorial of 0 is 1")
} else {
  for (i in 1:num) {
    fact <- fact * i
  }
  cat("Factorial of", num, "is:", fact)
}
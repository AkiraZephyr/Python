numbers <- c(2, 3, 4, 5, 10, 13, 17, 20) 
 
check_prime <- function(n) 
{   if (n <= 1) return(FALSE) 
   
 for (i in 2:sqrt(n)) 
  {     if (n %% i == 0) return(FALSE)   } 
   
return(TRUE) 
} 
 
prime_status <- sapply (numbers, check_prime) 
 
result <- data.frame(Number = numbers, IsPrime = prime_status) 
 
print (result)
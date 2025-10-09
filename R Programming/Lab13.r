calculator <- function(a, b, operator) {
  if (operator == "+") {
    result <- a + b
  } else if (operator == "-") {
    result <- a - b
  } else if (operator == "*") {
    result <- a * b
  } else if (operator == "/") {
    if (b == 0) {
      result <- "Division by zero is not allowed!"
    } else {
      result <- a / b
    }
  } else {
    result <- "Invalid operator!"
  }
  return(result)
}
a <- as.numeric(readline(prompt = "Enter first number: "))
b <- as.numeric(readline(prompt = "Enter second number: "))
operator <- readline(prompt = "Enter operator (+, -, *, /): ")
output <- calculator(a, b, operator)
cat("Result:", output, "\n")
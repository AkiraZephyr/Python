# Create a sample dataframe
data <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David"),
  Age = c(24, 27, 22, 32),
  Gender = c("F", "M", "M", "M"),
  Score = c(85, 90, 88, 75)
)
cat("Original Dataframe:\n")
print(data)

data1 <- subset(data, select = -Gender)
cat("\nDataframe after dropping 'Gender' column:\n")
print(data1)

data2 <- subset(data, select = -c(Age, Score))
cat("\nDataframe after dropping 'Age' and 'Score' columns:\n")
print(data2)
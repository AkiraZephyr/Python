# Create a sample dataframe
data <- data.frame(
  Name = c("Alice", "Bob", "Charlie", "David"),
  Age = c(25, 30, 35, 40),
  Gender = c("F", "M", "M", "M"),
  Salary = c(50000, 55000, 60000, 65000)
)

# Display the original dataframe
print("Original Dataframe:")
print(data)

# Drop a single column (e.g., 'Age')
data1 <- data[, !(names(data) %in% c("Age"))]

# Display dataframe after dropping one column
print("Dataframe after dropping 'Age' column:") 
print(data1)

# Drop multiple columns (e.g., 'Gender' and 'Salary')
data2 <- data[, !(names(data) %in% c("Gender", "Salary"))]

# Display dataframe after dropping multiple columns
print("Dataframe after dropping 'Gender' and 'Salary' columns:")
print(data2)

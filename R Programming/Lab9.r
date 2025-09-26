# Create a list
my_list <- list(
  Name = c("John", "Alice", "Bob"),
  Age = c(25, 30, 28),
  Marks = c(85, 90, 78)
)

# Convert to data frame
df <- as.data.frame(my_list)

# Display result
print(df)
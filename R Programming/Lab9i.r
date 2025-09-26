# List of lists
my_list <- list(
  list(Name = "John", Age = 25, Marks = 85),
  list(Name = "Alice", Age = 30, Marks = 90),
  list(Name = "Bob", Age = 28, Marks = 78)
)
# Convert to data frame
df <- do.call(rbind, lapply(my_list, as.data.frame))
print(df)
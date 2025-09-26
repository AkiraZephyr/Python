# First data frame
df1 <- data.frame(ID = c(1, 2, 3), Name = c("John", "Alice", "Bob"))
# Second data frame
df2 <- data.frame(ID = c(2, 3, 4), Marks = c(90, 78, 85))
# Merge on 'ID' column
combined_df <- merge(
  df1, df2, by = "ID", all = TRUE
)  # all=TRUE for full outer join
# Display result
print(combined_df)
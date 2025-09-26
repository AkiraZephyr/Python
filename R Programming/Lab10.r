# First data frame
df1 <- data.frame(Name = c("John", "Alice", "Bob"))
# Second data frame
df2 <- data.frame(Marks = c(85, 90, 78))
# Combine column-wise
combined_df <- cbind(df1, df2)
# Display result
print(combined_df)
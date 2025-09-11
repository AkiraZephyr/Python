# Define a vector of strings
strings <- c("R", "Programming", "Language")
# Find length of each string
lengths <- nchar(strings)
# Display results
#data.frame(String = strings, Length = lengths)
result <- data.frame(String = strings, Length = lengths)
# Print the result
print(result)
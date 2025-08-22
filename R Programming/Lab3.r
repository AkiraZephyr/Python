# Step 2: Define a numeric vector
numbers <- c(34, 12, 78, 5, 23, 56)

# Step 3: Sort in ascending order
sorted_asc <- sort(numbers)

# Step 4: Sort in descending order
sorted_desc <- sort(numbers, decreasing = TRUE)

# Step 5: Display results
cat("Original Vector:", numbers, "\n")
cat("Sorted (Ascending):", sorted_asc, "\n")
cat("Sorted (Descending):", sorted_desc, "\n")

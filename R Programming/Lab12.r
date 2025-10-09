# Create a sample vector
numbers <- c(10, 20, 30, 40, 50)

# Display the vector
print("The vector elements are:")
print(numbers)

# Element to check
element <- 30

# Check if the element exists in the vector
if (element %in% numbers) {
  print(paste(element, "is present in the vector."))
} else {
  print(paste(element, "is NOT present in the vector."))
}
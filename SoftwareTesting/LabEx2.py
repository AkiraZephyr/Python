def validate_input(number):
    if 10 <= number <= 100:
        return "Valid Input"
    else:
        return "Invalid Input"

# Equivalence Partitioning Tests
def equivalence_partitioning_tests():
    print("\n--- Equivalence Partitioning Tests ---")
    test_cases = [5, 10, 20, 50, 100, 120]  # Expanded coverage: invalid, valid, invalid partitions
    for num in test_cases:
        result = validate_input(num)
        print(f"Test with input {num}: {result}")

# Boundary Value Analysis Tests
def boundary_value_analysis_tests():
    print("\n--- Boundary Value Analysis Tests ---")
    boundary_values = [9, 10, 11, 99, 100, 101]  # Testing critical boundary points
    for num in boundary_values:
        result = validate_input(num)
        print(f"Test with input {num}: {result}")

# Main Execution: User Input Validation + Automated Tests
if __name__ == "__main__":
    try:
        user_input = input("Enter a number between 10 and 100: ")
        if user_input.isdigit():
            print(validate_input(int(user_input)))
        else:
            print("Invalid input: Please enter a valid integer.")
    except ValueError:
        print("Error: Unexpected input type.")

    # Perform Black Box Testing
    equivalence_partitioning_tests()
    boundary_value_analysis_tests()
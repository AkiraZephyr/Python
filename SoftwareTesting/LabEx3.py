# --------------------------------------------
# AUTOMATED SOFTWARE TESTING SIMULATION
# --------------------------------------------

# Step 1: Define the function to be tested
def square(x):
    """Returns the square of a number"""
    if isinstance(x, (int, float)):  # Ensuring valid numeric input
        return x * x
    else:
        return "Invalid Input"

# Step 2: Function to generate test cases dynamically
def get_test_cases():
    return [
        {"input": 2, "expected": 4},
        {"input": -3, "expected": 9},
        {"input": 0, "expected": 0},
        {"input": 5, "expected": 25},
        {"input": 10, "expected": 100},
        {"input": -1, "expected": 1},
        {"input": 3.5, "expected": 12.25},  # Float test case
        {"input": "text", "expected": "Invalid Input"}  # Non-numeric case
    ]

# Step 3: Function to run automated tests
def run_tests():
    print("Running Automated Tests...\n")
    test_cases = get_test_cases()
    passed = 0  

    for index, test in enumerate(test_cases):
        input_value = test["input"]
        expected_output = test["expected"]
        actual_output = square(input_value)

        # Compare expected vs actual output
        result = "PASS" if actual_output == expected_output else "FAIL"
        if result == "PASS":
            passed += 1

        print(f"Test Case {index + 1}: Input={input_value} | Expected={expected_output} | Actual={actual_output} --> {result}")

    total = len(test_cases)
    print(f"\nTesting Completed: {passed}/{total} Tests Passed.")

# Step 4: Run the test process
if __name__ == "__main__":
    run_tests()
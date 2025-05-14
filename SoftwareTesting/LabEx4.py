import time
import os

# --------------------------------------------
# AUTOMATED TEST CASE EXECUTION AND LOGGING
# --------------------------------------------

# Step 1: Define the function to be tested
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    try:
        return int(a) + int(b)
    except ValueError:
        return "Invalid Input"

# Step 2: Read test cases from a file
def read_test_cases(file_path):
    test_cases = []
    
    if not os.path.exists(file_path):
        print(f"Error: Test case file '{file_path}' not found. Creating a sample file...")
        with open(file_path, 'w') as file:
            file.write("2,3,5\n10,20,30\n5,5,10\n1,1,2\n0,0,0\n100,200,300\n4,5,8\n")
        return read_test_cases(file_path)  # Re-read file after creating it
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split(',')
            if len(parts) == 3 and all(p.replace('-', '').isdigit() for p in parts):
                input1, input2, expected = map(int, parts)
                test_cases.append((input1, input2, expected))
            else:
                print(f"Skipping invalid test case: {line.strip()}")
    
    return test_cases

# Step 3: Execute tests and log results
def execute_tests_and_log(test_cases, result_file_path):
    with open(result_file_path, 'a') as result_file:  # Appending instead of overwriting
        result_file.write(f"\n--- Test Run: {time.strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        passed = 0

        for index, (input1, input2, expected) in enumerate(test_cases):
            actual = add_numbers(input1, input2)
            result = "PASS" if actual == expected else "FAIL"
            result_file.write(f"Test Case {index+1}: Inputs=({input1},{input2}), Expected={expected}, Actual={actual} --> {result}\n")

            if result == "PASS":
                passed += 1

        total = len(test_cases)
        result_file.write(f"\nTesting Summary: {passed}/{total} Tests Passed.\n")
    
    print(f"Testing complete. Results saved in '{result_file_path}'.")

# Step 4: Main Execution
if __name__ == "__main__":
    test_case_file = "test_cases.txt"
    result_file = "test_results.txt"

    test_cases = read_test_cases(test_case_file)
    if test_cases:  # Only proceed if valid test cases are found
        execute_tests_and_log(test_cases, result_file)
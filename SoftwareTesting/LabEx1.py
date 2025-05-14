import inspect
import re

# Define functions
def sample_function(x):
    if x > 0:
        print("Positive number")
    elif x < 0:
        print("Negative number")
    else:
        print("Zero")

def sample_function_modified(x):
    if x > 0:
        for i in range(x):
            if i % 2 == 0:
                print(i, "is even")
            else:
                print(i, "is odd")
    elif x < 0:
        print("Negative number")
    else:
        print("Zero")

# Function to calculate Cyclomatic Complexity
def calculate_cyclomatic_complexity(function_code):
    """
    Cyclomatic Complexity (CC) = E - N + 2P
    E (Edges) ~ Decision Points + 1
    N (Nodes) ~ Statements
    P (Connected Components) ~ 1
    """
    decision_keywords = ['if', 'elif', 'for', 'while', 'case', 'except', 'try']
    lines = function_code.split('\n')

    decisions = 0
    nodes = 0

    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        nodes += 1

        # Using regex for better keyword matching in line
        if any(re.search(rf'\b{keyword}\b', line) for keyword in decision_keywords):
            decisions += 1

    edges = decisions + 1  # Improved estimate
    complexity = edges - nodes + 2  # McCabe's formula
    return max(1, complexity)  # Complexity should be at least 1

# Display Control Flow
def display_control_flow_diagram_simple():
    print("\nSimple Control Flow Diagram for 'sample_function':\n")
    print("""
        [Start]
           |
        [Check x > 0]
         /     \\
    Yes /       \\ No
     [Print Positive]   [Check x < 0]
                         /     \\
                    Yes /       \\ No
                  [Print Negative] [Print Zero]
                         \\     /
                          [End]
    """)

# Control Flow Demonstration
def control_flow_demo(x):
    print("\nControl Flow Execution for input:", x)
    print("Start")
    if x > 0:
        print("Decision: x > 0 → True path")
    elif x < 0:
        print("Decision: x < 0 → True path")
    else:
        print("Else path (Zero)")
    print("End")

# Import inspect and analyze functions
print("---- Analyzing Original 'sample_function' ----")
function_source = inspect.getsource(sample_function)
complexity = calculate_cyclomatic_complexity(function_source)
print("Cyclomatic Complexity of 'sample_function':", complexity)
control_flow_demo(5)
control_flow_demo(-3)
control_flow_demo(0)
display_control_flow_diagram_simple()

print("\n---- Analyzing Modified 'sample_function_modified' ----")
function_source_modified = inspect.getsource(sample_function_modified)
complexity_modified = calculate_cyclomatic_complexity(function_source_modified)
print("Cyclomatic Complexity of 'sample_function_modified':", complexity_modified)
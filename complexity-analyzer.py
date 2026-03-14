import ast

# 👇 PASTE THE PYTHON CODE YOU WANT TO ANALYZE INSIDE THESE TRIPLE QUOTES 👇
CODE_TO_ANALYZE = """
def example_function(arr):
    for i in arr:
        for j in arr:
            print(i, j)
"""
# 👆 ------------------------------------------------------------------ 👆

# Capture the code from the string above, or from the 'cmd' global if available
user_code = cmd if "cmd" in globals() and cmd.strip() else CODE_TO_ANALYZE

if not user_code.strip():
    print("Welcome to the Big-O Code Analyzer! 🔍")
    print("---------------------------------------")
    print(
        "Paste your Python code into the CODE_TO_ANALYZE variable at the top and hit Run."
    )
    print(
        "I will analyze its Abstract Syntax Tree (AST) to estimate its Time Complexity."
    )
else:
    try:
        # Parse the user's string into an actual Python Abstract Syntax Tree
        tree = ast.parse(user_code)

        # Recursive function to find the maximum depth of nested loops
        def get_max_depth(node, current_depth=0):
            max_depth = current_depth

            # Iterate through all child nodes of the current AST node
            for child in ast.iter_child_nodes(node):
                # If we hit a loop construct, increment the depth
                if isinstance(
                    child, (ast.For, ast.While, ast.ListComp, ast.DictComp, ast.SetComp)
                ):
                    child_depth = get_max_depth(child, current_depth + 1)
                    max_depth = max(max_depth, child_depth)
                else:
                    # Otherwise, keep traversing at the current depth
                    child_depth = get_max_depth(child, current_depth)
                    max_depth = max(max_depth, child_depth)

            return max_depth

        # Calculate the depth of the parsed code
        depth = get_max_depth(tree)

        print("🔍 --- Big-O Complexity Analysis --- 🔍\n")

        if depth == 0:
            print("Estimated Time Complexity: O(1) or O(N)")
            print(
                "Reason: No loops were detected. \n(Note: Native Python functions like .sort() or min() under the hood may still be O(N) or O(N log N))."
            )
        elif depth == 1:
            print("Estimated Time Complexity: O(N) [Linear]")
            print(
                "Reason: Found a single loop. Execution time scales linearly with the input."
            )
        elif depth == 2:
            print("Estimated Time Complexity: O(N^2) [Quadratic]")
            print(
                "Reason: Found nested loops (depth of 2). This is typical for algorithms like Bubble Sort or iterating over 2D arrays/matrices."
            )
        elif depth == 3:
            print("Estimated Time Complexity: O(N^3) [Cubic]")
            print(
                "Reason: Found deeply nested loops (depth of 3). Watch out for performance bottlenecks on large datasets!"
            )
        else:
            print(f"Estimated Time Complexity: O(N^{depth})")
            print(
                "Reason: Found extremely deep nesting. You should definitely optimize this code."
            )

        print("\n✅ Code parsed and analyzed successfully.")

    except SyntaxError as e:
        print(f"❌ Syntax Error: Could not parse the provided code snippet.")
        print("Please ensure what you pasted inside CODE_TO_ANALYZE is valid Python.")
        print(f"Details: {e}")
    except Exception as e:
        print(f"⚠️ An error occurred during analysis:\n{e}")

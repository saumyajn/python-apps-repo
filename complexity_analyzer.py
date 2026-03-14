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
        tree = ast.parse(user_code)

        def get_max_depth(node, current_depth=0):
            max_depth = current_depth
            for child in ast.iter_child_nodes(node):
                if isinstance(
                    child, (ast.For, ast.While, ast.ListComp, ast.DictComp, ast.SetComp)
                ):
                    child_depth = get_max_depth(child, current_depth + 1)
                    max_depth = max(max_depth, child_depth)
                else:
                    child_depth = get_max_depth(child, current_depth)
                    max_depth = max(max_depth, child_depth)
            return max_depth

        depth = get_max_depth(tree)

        print("🔍 --- Big-O Complexity Analysis --- 🔍\n")

        if depth == 0:
            print("Estimated Time Complexity: O(1) or O(N)")
        elif depth == 1:
            print("Estimated Time Complexity: O(N) [Linear]")
        elif depth == 2:
            print("Estimated Time Complexity: O(N^2) [Quadratic]")
        elif depth == 3:
            print("Estimated Time Complexity: O(N^3) [Cubic]")
        else:
            print(f"Estimated Time Complexity: O(N^{depth})")

        print("\n✅ Code parsed and analyzed successfully.")

    except SyntaxError as e:
        print(
            f"❌ Syntax Error: Could not parse the provided code snippet.\nDetails: {e}"
        )
    except Exception as e:
        print(f"⚠️ An error occurred during analysis:\n{e}")

# Balanced Parentheses using Stack

def balanced_parentheses(s):
    """
    Returns True if the parentheses are balanced,
    otherwise returns False.
    """
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)

        elif ch == ')':
            # No matching opening parenthesis
            if not stack:
                return False
            stack.pop()

    # Stack should be empty if all parentheses are matched
    return len(stack) == 0


# Example Usage
expression = "(()())"

if balanced_parentheses(expression):
    print("Balanced")
else:
    print("Not Balanced")

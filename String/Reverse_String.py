# ------------------------------------------------------------
# Algorithm : Reverse String (Two Pointers)
# Purpose   : Reverse a string using the two-pointer technique.
# Time      : O(n)
# Space     : O(n)
# ------------------------------------------------------------

def reverse_string(s):
    """
    Returns the reversed version of the input string.
    """
    chars = list(s)
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    s = "Hello"
    print("Original String:", s)
    print("Reversed String:", reverse_string(s))

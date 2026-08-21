# Function to check whether a string is a palindrome
def isPalindrome(s):
    
    # Initialize two pointers
    left = 0
    right = len(s) - 1

    # Compare characters from both ends
    while left < right:

        # Skip non-alphanumeric characters from the left
        while left < right and not s[left].isalnum():
            left += 1

        # Skip non-alphanumeric characters from the right
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters ignoring case
        if s[left].lower() != s[right].lower():
            return False

        # Move both pointers towards the center
        left += 1
        right -= 1

    # String is a palindrome
    return True


# Input string
s = "A man, a plan, a canal: Panama"

# Check and print the result
print(isPalindrome(s))

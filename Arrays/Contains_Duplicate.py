# Check whether the array contains duplicate elements
def contains_duplicate(arr):
    seen = {}  # Dictionary to store elements that have already been seen

    # Traverse through each element in the array
    for num in arr:

        # If the element is already in the dictionary, duplicate exists
        if num in seen:
            return True

        # Store the element in the dictionary
        seen[num] = 1

    # No duplicate elements found
    return False


# Example array
arr = [1, 2, 3, 4]

# Call the function and print the result
print(contains_duplicate(arr))

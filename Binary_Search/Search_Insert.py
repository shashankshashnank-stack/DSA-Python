# Function to search for a target using Binary Search
def Search(arr, target):

    # Set the left pointer to the first index
    i = 0

    # Set the right pointer to the last index
    j = len(arr) - 1

    # Continue searching while the search range is valid
    while i <= j:

        # Calculate the middle index
        mid = (i + j) // 2

        # Check if the middle element is the target
        if arr[mid] == target:

            # Return the index if the target is found
            return mid

        # If the middle element is smaller than the target,
        # search in the right half
        elif arr[mid] < target:
            i = mid + 1

        # If the middle element is greater than the target,
        # search in the left half
        else:
            j = mid - 1

    # Target is not found
    # Return the index where the target can be inserted
    return i


# Input sorted array
arr = [1, 3, 4, 5]

# Target value
target = 10

# Call the function and print the result
print(Search(arr, target))

# Function to find the index of the smallest element
# that is greater than or equal to x
def Ceil_Index(arr, x):

    # Initialize the binary search range
    low = 0
    high = len(arr) - 1

    # Store the answer index
    ans = -1

    # Perform binary search
    while low <= high:

        # Find the middle index
        mid = (low + high) // 2

        # If middle element is greater than or equal to x
        if arr[mid] >= x:
            ans = mid

            # Search for a smaller valid element on the left
            high = mid - 1

        else:
            # Search on the right side
            low = mid + 1

    # Return the ceil index
    return ans


# Sorted array
arr = [3, 5, 8, 15, 19]

# Value to find the ceil for
x = 15

# Print the ceil index
print(Ceil_Index(arr, x))

# Function to move all zeroes to the end of the array
def move_zeroes(arr):
    """
    Moves all zeroes to the end of the array
    while maintaining the order of non-zero elements.

    Uses the Two-Pointer approach.
    """

    # j points to the position where the next
    # non-zero element should be placed
    j = 0

    # i traverses through the entire array
    for i in range(len(arr)):

        # Check if the current element is non-zero
        if arr[i] != 0:

            # Swap the non-zero element with arr[j]
            arr[i], arr[j] = arr[j], arr[i]

            # Move j to the next position
            j += 1

    return arr


# Example
arr = [0, 1, 0, 3, 12]

# Call the function
result = move_zeroes(arr)

# Display the result
print("Original array: [0, 1, 0, 3, 12]")
print("After moving zeroes:", result)

def insertion_sort(arr):
    """Sort an array in ascending order using Insertion Sort."""

    # Start from the second element
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Move larger elements one position to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert the key into its correct position
        arr[j + 1] = key

    return arr


# Example
arr = [100, 80, 25, -100, 20]

print(insertion_sort(arr))

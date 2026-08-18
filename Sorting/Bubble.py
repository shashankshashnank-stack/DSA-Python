def bubble_sort(arr):
    """Sort an array in ascending order using Bubble Sort."""

    n = len(arr)

    # Perform multiple passes through the array
    for i in range(n):
        swapped = False

        # The last i elements are already sorted
        for j in range(0, n - i - 1):

            # Swap adjacent elements if they are out of order
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # Stop early if the array is already sorted
        if not swapped:
            break

    return arr


# Example
arr = [60, 10, 5, 200, -100, -100]

print(bubble_sort(arr))

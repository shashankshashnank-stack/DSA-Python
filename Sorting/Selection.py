# Selection Sort
def selection_sort(arr):
    n = len(arr)

    # Traverse through each position in the array
    for i in range(n):

        # Assume the current position contains the minimum element
        min_index = i

        # Find the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    # Return the sorted array
    return arr


# Example array
arr = [20, 10, 30, -100]

# Call the function and print the sorted array
print(selection_sort(arr))

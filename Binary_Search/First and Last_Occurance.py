# Find the first occurrence of x using Binary Search
def First_Occurance(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1                     # Stores the first occurrence index

    # Continue searching while the search space is valid
    while low <= high:
        mid = (low + high) // 2  # Find the middle index

        if arr[mid] == x:
            ans = mid            # Found x, store the index
            high = mid - 1       # Search on the left for an earlier occurrence

        elif arr[mid] < x:
            low = mid + 1        # Search in the right half

        else:
            high = mid - 1       # Search in the left half

    # Return the first occurrence index, or -1 if not found
    return ans
# Find the last occurrence of x using Binary Search
def Last_Occurance(arr, x):
    low = 0
    high = len(arr) - 1
    ans = -1                     # Stores the last occurrence index

    # Continue searching while the search space is valid
    while low <= high:
        mid = (low + high) // 2  # Find the middle index

        if arr[mid] == x:
            ans = mid            # Found x, store the index
            low = mid + 1        # Search on the right for a later occurrence

        elif arr[mid] < x:
            low = mid + 1        # Search in the right half

        else:
            high = mid - 1       # Search in the left half

    # Return the last occurrence index, or -1 if not found
    return ans
arr = [1, 2, 2, 2, 3, 4]
x = 2

print(First_Occurance(arr, x))   # 1
print(Last_Occurance(arr, x))    # 3

# Binary Search (Array must be sorted)
def Binary(arr, key):
    low = 0                  # Start from the first index
    high = len(arr) - 1      # End at the last index

    # Continue searching while the search space is valid
    while low <= high:

        # Find the middle index
        mid = (low + high) // 2

        # Check if the middle element is the key
        if arr[mid] == key:
            return mid       # Key found, return its index

        # If the key is greater, search the right half
        elif arr[mid] < key:
            low = mid + 1

        # If the key is smaller, search the left half
        else:
            high = mid - 1

    # Key is not present in the array
    return -1


# Sorted array (required for Binary Search)
arr = [5, 10, 20, 25, 30, 33, 50]

# Element to search
key = 30

# Call the Binary Search function
result = Binary(arr, key)

# Check whether the key was found
if result != -1:
    print(f"Element was found at index {result}")
else:
    print("Element was not found")

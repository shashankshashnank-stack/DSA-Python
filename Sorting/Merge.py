def Merge_Sort(arr):
    # Divide the array until each part contains one element
    if len(arr) > 1:

        # Find the middle and split the array into two halves
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursively sort both halves
        Merge_Sort(left)
        Merge_Sort(right)

        # Initialize pointers
        i = j = k = 0

        # Compare and merge elements from both halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements from the left half
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements from the right half
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


# Take array size from the user
n = int(input("Enter the number of elements: "))

# Take array elements from the user
arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

print("Original Array:", arr)

# Apply Merge Sort
Merge_Sort(arr)

print("Sorted Array:", arr)

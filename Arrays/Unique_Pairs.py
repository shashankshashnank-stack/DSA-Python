# Find all unique pairs in a sorted array whose sum is equal to k
def Pair(arr, k):

    # Store all valid pairs
    result = []

    # Initialize two pointers
    i = 0
    j = len(arr) - 1

    # Continue until the pointers meet
    while i < j:

        # Calculate the sum of elements at both pointers
        cursum = arr[i] + arr[j]

        # If the sum matches the target, store the pair
        if cursum == k:
            result.append((arr[i], arr[j]))

            # Move both pointers
            i += 1
            j -= 1

            # Skip duplicate elements
            while i < j and arr[i] == arr[i - 1]:
                i += 1

            while i < j and arr[j] == arr[j + 1]:
                j -= 1

        # If the sum is smaller, move left pointer forward
        elif cursum < k:
            i += 1

        # If the sum is larger, move right pointer backward
        else:
            j -= 1

    return result


# Take array input from the user
n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    arr.append(value)

# Sort the array for the two-pointer approach
arr.sort()

# Take the target sum from the user
k = int(input("Enter the target sum: "))

# Find and display all valid pairs
result = Pair(arr, k)

print("Sorted Array:", arr)
print("Pairs with sum", k, ":", result)

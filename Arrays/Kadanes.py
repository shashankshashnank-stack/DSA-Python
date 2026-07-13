# Kadane's Algorithm
# Problem: Find the maximum sum of a contiguous subarray.
# Time Complexity: O(n)
# Space Complexity: O(1)

def kadanes_algorithm(arr):
    max_current = max_global = arr[0]

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])
        max_global = max(max_global, max_current)

    return max_global


if __name__ == "__main__":
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(kadanes_algorithm(arr))

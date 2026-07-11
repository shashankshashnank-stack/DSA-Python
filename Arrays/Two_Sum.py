# Problem: Two Sum (Sorted Array)
# Approach: Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

def TwoSum(arr, target):
    i, j = 0, len(arr) - 1

    while i < j:
        curr_sum = arr[i] + arr[j]

        if curr_sum == target:
            return arr[i], arr[j]
        elif curr_sum < target:
            i += 1
        else:
            j -= 1

    return -1


arr = [2, 7, 10, 20]
target = 17

print(TwoSum(arr, target))

# Two Sum - Unsorted Array
# Approach: Hash Map (Dictionary)
# Time Complexity: O(n)
# Space Complexity: O(n)

def Two_Sum(nums, target):
    seen = {}

    for i, num in enumerate(nums):
        diff = target - num

        if diff in seen:
            return (seen[diff], i)

        seen[num] = i

    return []


arr = [7, 2, 0, 10]
target = 9

print(Two_Sum(arr, target))

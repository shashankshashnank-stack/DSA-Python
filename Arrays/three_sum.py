"""
Three Sum Problem

Given an integer array and a target value, return all unique triplets
whose sum equals the target.

Approach:
1. Sort the array.
2. Fix one element.
3. Use the two-pointer technique to find the remaining two elements.
4. Skip duplicate values to avoid duplicate triplets.

Time Complexity: O(n²)
Space Complexity: O(1) (excluding the output list)
"""


def three_sum(arr, target):
    """
    Find all unique triplets whose sum equals the target.

    Args:
        arr (list): List of integers.
        target (int): Target sum.

    Returns:
        list: List of unique triplets.
    """
    arr.sort()
    n = len(arr)
    result = []

    for i in range(n - 2):

        # Skip duplicate first elements
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        left = i + 1
        right = n - 1

        while left < right:
            total = arr[i] + arr[left] + arr[right]

            if total == target:
                result.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1

                # Skip duplicate second elements
                while left < right and arr[left] == arr[left - 1]:
                    left += 1

                # Skip duplicate third elements
                while left < right and arr[right] == arr[right + 1]:
                    right -= 1

            elif total < target:
                left += 1

            else:
                right -= 1

    return result


def main():
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0

    print("Array:", arr)
    print("Target:", target)
    print("Triplets:", three_sum(arr, target))


if __name__ == "__main__":
    main()

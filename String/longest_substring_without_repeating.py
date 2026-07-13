# ------------------------------------------------------------
# Algorithm : Longest Substring Without Repeating Characters
# Approach  : Sliding Window + Hash Set
# Time      : O(n)
# Space     : O(n)
# ------------------------------------------------------------

def longest_substring_without_repeating(s):
    """
    Returns the length of the longest substring
    without repeating characters.
    """
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


if __name__ == "__main__":
    s = "abccabc"
    print("Length of Longest Substring:", longest_substring_without_repeating(s))

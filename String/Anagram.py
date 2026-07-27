# Check if Two Strings are Anagrams

def is_anagram(s1, s2):
    """
    Returns True if s1 and s2 are anagrams,
    otherwise returns False.
    """

    # If lengths are different, they cannot be anagrams
    if len(s1) != len(s2):
        return False

    freq = {}

    # Count the frequency of each character in s1
    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    # Decrease the frequency using characters from s2
    for ch in s2:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True


# Example Usage
s1 = "cat"
s2 = "act"

if is_anagram(s1, s2):
    print("Anagram")
else:
    print("Not Anagram")

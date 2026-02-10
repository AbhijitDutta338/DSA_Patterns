#Dynamic Window Approach
def length_of_longest_substring_sliding_window(self, s):
    seen = set()
    max_length = left = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
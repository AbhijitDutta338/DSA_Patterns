class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)  # length of the input string
        if n == 0:
            return ""  # empty string edge-case

        start = 0  # start index of the longest palindrome found
        maxLength = 1  # max palindrome length found (single char at least)

        for i in range(n):
            # Check odd-length palindromes centered at i (single center)
            length1 = self.expand(s, i, i)
            if length1 > maxLength:
                maxLength = length1
                # For odd length L centered at i, start = i - (L-1)//2
                start = i - (length1 - 1) // 2

            # Check even-length palindromes centered between i and i+1
            length2 = self.expand(s, i, i + 1)
            if length2 > maxLength:
                maxLength = length2
                # For even length L with right-center at i+1, start = i - (L//2) + 1
                start = i - (length2 // 2) + 1

        # Return substring from start with length maxLength
        return s[start:start + maxLength]

    def expand(self, s: str, left: int, right: int) -> int:
        # Expand around the center defined by left and right indices.
        # Stops when characters differ or bounds are exceeded.
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # After the loop, left and right are one step beyond the palindrome bounds.
        # Length is right - left - 1 (inclusive span).
        return right - left - 1
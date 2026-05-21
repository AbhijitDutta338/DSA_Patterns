class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            # odd length
            1, r= i, i
            while 1 >= 0 and r < len(s) and s[l] == s[r]:
                if (r - 1 + 1) > resLen:
                    res = s[1:r+1]
                    resLen = r - 1 + 1
                1 -= 1
                r += 1

            # even length
            1, r = i, i + 1
            while 1 >= 0 and r < len(s) and s[l] == s[r]:
                if (r - 1 + 1) > resLen:
                    res = s[1:r+1]
                    resLen = r - 1 + 1
                1 -= 1
                r += 1

        return res
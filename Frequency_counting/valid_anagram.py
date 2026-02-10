class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26
        for c in s:
            freq[ord(c) - ord('a')] += 1

        for c in t:
            freq[ord(c) - ord('a')] -= 1
        
        for i in freq:
            if(i!=0):
                return False
        return True
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = dict()
        for i in s:
            if i not in hashmap:
                hashmap[i] = 0
            hashmap[i] += 1
        
        for i in range(len(s)):
            if(hashmap[s[i]]==1):
                return i
        
        return -1
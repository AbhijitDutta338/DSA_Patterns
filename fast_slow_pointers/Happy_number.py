def getSumOfSquares(self, n):
    return sum(int(digit)**2 for digit in str(n))

def isHappyFastAndSlowPointersApproach(self, n):
    slow = n
    fast = self.getSumOfSquares(n)
    while fast != 1 and slow != fast:
        slow = self.getSumOfSquares(slow)
        fast = self.getSumOfSquares(self.getSumOfSquares(fast))
    return fast == 1


#Hashset Approach
def isHappyHashSetApproach(self, n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = self.getSumOfSquares(n)
    return n == 1
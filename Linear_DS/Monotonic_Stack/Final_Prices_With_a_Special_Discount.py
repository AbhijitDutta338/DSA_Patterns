import copy
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answerlist = copy.deepcopy(prices)
        stack = []
        
        for i in range(len(prices)):
            while(stack and prices[i]<=prices[stack[-1]]):
                idx = stack.pop()
                answerlist[idx] -= prices[i]
            stack.append(i)
            
        return answerlist
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def is_valid(path):
            stack = []
            for i in path:
                if(i=='('):
                    stack.append('(')
                elif(len(stack)>0):
                    stack.pop()
                else:
                    return False
            
            if(len(stack)==0):
                return True
            return False
        
        def backtrack(path):
            if len(path) == 2*n:
                if is_valid(path):
                    result.append(''.join(path))
                return 
            
            #Only have 2 choices - Execising First Choice
            path.append('(')
            backtrack(path)
            path.pop()

            #Execising 2nd Choice
            path.append(')')
            backtrack(path)
            path.pop()
        
        backtrack([])
        return result

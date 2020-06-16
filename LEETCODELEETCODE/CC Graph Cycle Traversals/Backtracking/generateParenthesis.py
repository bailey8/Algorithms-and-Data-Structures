class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        answer = []
        
        def dfs(openP = n,closeP = n, string = ""):
            if openP == 0 and closeP == 0:
                answer.append(string)
                return 
            
            # I CAN EITHER PLACE AN OPEN PARETHESIS IF THERE ARE ANY LEFT
            if openP > 0:
                dfs(openP-1, closeP, string + "(")
            
            # OR I CAN CLOSE THE PARENTHESIS IF I HAVE MORE CLOSED THAN OPEN
            if closeP > openP:
                dfs(openP,closeP-1, string + ")")
        
        dfs()
        return answer
        
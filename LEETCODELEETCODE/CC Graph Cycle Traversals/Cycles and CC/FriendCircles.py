class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        
        def dfs(row):
            
            # THE COLUMN CELLS FOR THE SPECIFIC ROW INDEX PASSED IN ARE CHILDREN
            for col in range(len(M)):
                
                # M[ROW][COL] ENSURES THE CELL IS 1, WHICH MEANS THE COL NODE IS ACTUALLY A CHILD
                # THEN WE CHECK TO SEE IF WE ALREADY VISITED THE CHILD
                if M[row][col] and col not in visited:
                    #IF WE HAVE NOT VISITED THE CHILD, THEN ADD IT TO VISITED AND VISIT IT
                    visited.add(col)
                    dfs(col)
                    
        count = 0
        visited = set()
        
        # EACH ROW IN THE ADJACENCY MATRIX REPRESENTS A NODE
        for row in range(len(M)):
            # THE INDEX OF THE ROW REPRESENTS THE NODE
            if row not in visited:
                # INCREMENT THE NUMBER OF CONNECTED COMPONENTS
                count +=1
                # EXPLORE THE NODE BC IT HASNT BEEN EXPLORED YET
                dfs(row)
        return count
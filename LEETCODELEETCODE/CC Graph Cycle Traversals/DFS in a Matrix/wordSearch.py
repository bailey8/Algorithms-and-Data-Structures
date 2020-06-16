import collections

class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    # 3:42
    def exist(self, board, word):

        # USED TO TRACK WHICH CELLS YOU HAVE VISITED
        visited = collections.defaultdict(int)

        # FOR EACH CELL IN THE MATRIX, USE IT AS THE STARTING LOCATION
        for i in range(len(board)):
            for j in range(len(board[0])):

                # IF IT TRUE, THAT MEANS THE WORD CAN BE CREATED AT THIS CELL
                if self.getWords(board, word, i, j, visited):
                    return True
        return False

    def getWords(self, board, word, i, j, visited, pos = 0):
        if pos == len(word):
            return True

        # IF WE ARE OUT OF BOUNDS THEN RETURN FALSE
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]): return False

        if visited[(i, j)] == 1 or word[pos] != board[i][j]:
            return False

        visited[(i, j)] = True
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
                or self.getWords(board, word, i, j - 1, visited, pos + 1) \
                or self.getWords(board, word, i + 1, j, visited, pos + 1) \
                or self.getWords(board, word, i - 1, j, visited, pos + 1)
        visited[(i, j)] = False

        return res


import collections
class Solution2:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    # 3:42
    def exist(self, board, word):

        # USED TO TRACK WHICH CELLS YOU HAVE VISITED
        visited = collections.defaultdict(int)

        # FOR EACH CELL IN THE MATRIX, USE IT AS THE STARTING LOCATION
        for i in range(len(board)):
            for j in range(len(board[0])):

                # IF IT TRUE, THAT MEANS THE WORD CAN BE CREATED AT THIS CELL
                if self.getWords(board, word, i, j, visited):
                    return True
        return False

    def getWords(self, board, word, i, j, visited, pos = 0):
        
        # THIS MEANS WE HAVE INCREMENTED "1 PAST THE END OF THE WORD" MEANING THE WHOLE WORD IS VALID
        if pos == len(word):
            return True

        # IF WE ARE OUT OF BOUNDS THEN RETURN FALSE
        if i < 0 or i == len(board) or j < 0 or j == len(board[0]): return False

        # IF WE HAVE VISITED THIS CELL, OR THE CELL DOESNT MATCH THE NEXT LETTER IN THE WORD
        if board[i][j] == "visited" or word[pos] != board[i][j]:
            return False

        # Mark this cell as visited FOR THE SPECIFC START NODE
        temp = board[i][j]
        board[i][j] = "visited"
        
        # MAIN THING HERE IS TO UPDATE THE CHARACTER WE ARE SEARCHING FOR (pos+1)
        # if ANY OF THE DIRECTIONS RETURN TRUE THEN THE SOLUTION IS GOOD!
        res = self.getWords(board, word, i, j + 1, visited, pos + 1) \
                or self.getWords(board, word, i, j - 1, visited, pos + 1) \
                or self.getWords(board, word, i + 1, j, visited, pos + 1) \
                or self.getWords(board, word, i - 1, j, visited, pos + 1)
        
        # THIS IS THE KEY. THIS IS THE KEY. We mark the cell as not visited after
        # we explore all possibilites. We want to reset the visited set for each cell that 
        # we START ON. NEW VISITED FOR EAHC CELL WE START ON. But for all chains OFF
        # THAT START CELL WE KEEP THE SAME VISITED
        board[i][j] = temp

        return res

 
 class Solution:
    
    def __init__(self):
        self.directions = [[1,0],[-1,0],[0,1],[0,-1]]
        
    def exist(self, board: List[List[str]], word: str) -> bool:
            
        def dfs(row,col,index):
            
            # THIS MEANS ALL THE CHARACTERS WERE VALID. LINE BELOW IS BOUNDING FUNCTION
            if index == len(word): return True
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != word[index]: return False
      
            # WE DO NOT WANT TO RE-VISIT THESE CELLS IN FUTURE ITERATIONS (DUPLICATES)
            temp = board[row][col]
            board[row][col] = None
            
            #SEARCH EVERY CELL
            for direction in self.directions:
                x,y = row + direction[0], col + direction[1]
                if dfs(x,y, index+1): return True
             
            #RESET THE BOARD PIECE BC WE ARE DONE USING IT
            board[row][col] = temp    
            return False

        
        # SEARCH EVERY CELL IN THE GRID
        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row,col, 0): return True
        return False
        
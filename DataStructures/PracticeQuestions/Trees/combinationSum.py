def combinationSum(self, candidates, target):
    res = []
    candidates.sort()
    self.dfs(candidates, target, 0, [], res)
    return res
    
def dfs(self, nums, target, index, path, res):
    if target < 0:
        return  # backtracking
    # If the target is 0, then add the path you've built to results
    if target == 0:
        res.append(path)
        return 
    # For every other node, perform DFS after subtracting current val from target
    for i in range(index, len(nums)):
        #              Subtract from target, index we at, new path, response
        self.dfs(nums, target-nums[i], i, path+[nums[i]], res)

# The only thing that changes if you subtract the current value from target and add it to your path


# a= [1,2,3] 4
# DFS(candidates, target, index, path, solutions)
# DFS(a,4,0,[],[])
    # DFS(a,3,0,[1],[])
        # DFS(a,2,0,[1,1],[])
            # DFS(a,1,0,[1,1,1],[])
                # DFS(a,0,0,[1,1,1,1],[])  \\ BASECASE
                # DFS(a,-1,1,[1,1,1,2],[[1,1,1,1]]) \\BACKTRACK
                # DFS(a,-2, 2, [1,1,1,3],[[1,1,1,1]]) \\BACKTRACK
            # DFS (a,0,1,[1,1,2],[[1,1,1,1]]) \\ BASECASE
            # DFS (a,-1,2,[1,1,3],[[1,1,1,1],[1,1,2]]) \\BACKTRACK
        # DFS (a,1,1,[1,2],[[1,1,1,1],[1,1,2]])
            # DFS (a,-1,1,[1,2,2],[[1,1,1,1],[1,1,2]]) \\BACKTRACK
            # DFS (a,-2,2,[1,2,3],[[1,1,1,1],[1,1,2]]) \\BACKTRACK
        # DFS (a,0,2,[1,3],[[1,1,1,1],[1,1,2]]) \\BASECASE
    # DFS (a,2,1,[2],[[1,1,1,1],[1,1,2],[1,3]])
        # DFS (a,0,1,[2,2],[[1,1,1,1],[1,1,2],[1,3]]) \\BASECASE
        # DFS (a,-1,2,[2,3],[[1,1,1,1],[1,1,2],[1,3],[2,2]]) \\BACKTRACK
    # DFS (a,1,2,[3],[[1,1,1,1],[1,1,2],[1,3]])
        # DFS (a,-1,2,[3,3],[[1,1,1,1],[1,1,2],[1,3],[2,2]]) \\BACKTRACK

# AT every index, we start at that index, and stay
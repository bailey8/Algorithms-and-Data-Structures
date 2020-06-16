class Solution:
    def numTrees(self, n: int) -> int:

        # We will answer every subproblem from 0 to n hence the n + 1 to accomodate the 0 subproblem
        G = [0]*(n + 1)

        # The answer to the subproblem when n = 0 is 0.
        # The answer to the subproblem when n = 1 (we can only place a 1 as a value and have a single node) is 1. 
                # A single node can only make 1 unique tree.
        G[0] = G[1] = 1

        # We will solve every subproblem from 2 to our target subproblem n
        for sizeOfTree in range(2, n+1):
            """
                The answer to the ith subproblem will be the summation
                of F(i, n) for i = 0 to i = n (we plant every number we
                have available at the root)
                Remember that we expressed:
                F(i, n) = G(i - 1) * G(n - i)
                The answer to the total unique BST's we can construct with
                values from 1...n with i representing what is rooted at the
                root of the tree is F(i, n).
                All possible unique left BST's count is G[j - 1] if we plant at i.
                All possible unique right BST's count is G[i - j] if we plan at i.
                Taking a product is the same as taking all pairing between the
                two sets of possibilites.
            """
            # EX)         ---G(5) BREAKS INTO-------
            #            /    |       |       |     \
            #        F(1,5) , F(2,5), F(3,5), F(4,5), F(5,5)
            #       /   |       |  \
            #   G(0), G(4)    G(1), G(3) ...
            # SO THIS FOR LOOP WILL ADD G(0), G(4), G(1), G(3).... AND SUM IT UP INTO G(5)
            for nodesInLeftSubtree in range(sizeOfTree):
                G[sizeOfTree] += G[nodesInLeftSubtree ] * G[sizeOfTree - nodesInLeftSubtree - 1] 

        return G[n]

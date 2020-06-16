class Solution:
    def canPartitionKSubsets(self,arr, k):
  
        def canPartition(iterationStart, k, inProgressBucketSum):

            # WATCH VIDEO TO SEE WHY THIS IS VALID
            if k == 1: return True

            # Bucket full. continue the recursion with k - 1 as the new k value, 
            # BUT the targetBucketSum stays the same. We just have 1 less bucket to fill.
            if inProgressBucketSum == targetBucketSum:
                # RESET THE ITERATIONSTART BC WE NEED TO LOOP OVER THE 
                return canPartition(0, k - 1, 0)


            #Try all values from 'iterationStart' to the end of the array ONLY if:
            #1.) They have not been used up to this point in the recursion's path
            #2.) They do not overflow the current bucket we are filling
        
            
            # TARGET IS 6. NUMS ARE 1 2 9 2 1
            # 1
            #   2
            #      9 2
            for i in range(iterationStart, len(arr)):
                if not used[i] and inProgressBucketSum + arr[i] <= targetBucketSum:
                    used[i] = True
                    
                    if canPartition(i + 1, k, inProgressBucketSum + arr[i]): return True

                    # MAYBE USING 5 WONT WORK, SO WE FREE 5 TO USE LATER DOWN THE LINE AND TRY THE NEXT NUMBER
                    used[i] = False

            # Partitioning from this point is impossible. Whether we are at the top level of the recursion or deeper into it.
            return False

        """
            1.) k can not be negative or 0 because we can not fill 0 or negative buckets
            2.) k can not be greater than the length of the array, we can't partition more buckets than there are elements in the array
            3.) SUM/K MUST NOT BE A DECIMAL
        """
        if k <= 0 or k > len(arr) or sum(arr) % k != 0: return False
        
        targetBucketSum = sum(arr)/k
        used = [False] * len(arr)
    
        return canPartition(0, k, 0)
        
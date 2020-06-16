
    


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
 
        rows = len(matrix)
        cols = len(matrix[0])

        """
        Create an array that will be a "vertical" array and record
        the running sums for each row in the each iteration of the
        left bound
        """
        runningRowSums =[0]* rows

        """
        This is the max rectangle that we will update along the way
        """
        maxRectangle = Rectangle()

    """
    We will try all left bound plantings from index 0
    to index cols - 1
    """
    for left in range(cols):

        """
      We will reset the running row sums all to 0 since
      this is a new planting of the left bound
        """
     
        runningRowSums[:] = 0

        """
      For each left bound, we will try all of the right bounds
      starting at the left bound we are planted at.
        """
    for right in range(left,cols):

        """
        Add all items in column 'right' to their respective
        row's running sum
        """
        for i in range(rows):
            runningRowSums[i] += matrix[i][right]
      

      """
        Perform Kadane's algorithm on the running sum array
        so that we can determine the best top and bottom
        bound to choose for the rectangle.
      """
      kadaneResult = kadane(runningRowSums)

      """
        If we notice that this rectangle can achieve a better
        maxSum than the best we have done so far then we need
        to adjust our new best
      """
      if kadaneResult.maxSum > maxRectangle.interiorSum:

        """
          Set a new interiorSum for our maxRectangle
        """
        maxRectangle.interiorSum = kadaneResult.maxSum

        """
          The left and the right of the maxRectangle become
          the 'left' and 'right' where our for loop pointers
          are sitting
        """
        maxRectangle.leftBorderIndex = left
        maxRectangle.rightBorderIndex = right

        """
          Our top and bottom bounds for the max rectangle are
          going to be the startIndex and endIndex of the max
          subarray region in the 'runningRowSums' sum cache
          (respectively).
        """
        maxRectangle.topBorderIndex = kadaneResult.startIndex
        maxRectangle.bottomBorderIndex = kadaneResult.endIndex
  
  return maxRectangle


"""
  An implementation of Kadane's algorithm that remembers the
  start and end of the Max Contiguous Subarray Sum region
  in the KadaneResult object returned
  This video explains Kadane's algorithm: https://www.youtube.com/watch?v=2MmGzdiKR9Y
"""
def kadane(arr):

  """
    The best sum achieved for a region so far
  """
    bestMaxSoFar = 0

  """
    maxRegionStart: start index of the max sum region
    maxRegionEnd: end index of the max sum region
  """
    maxRegionStart = -1
    maxRegionEnd = -1

    currentStart = 0
    bestMaxAtThisIndex = 0

  """
    We will process every
  """
  for i in range(len(arr)): 

    """
      Add this item to the best subarray achieved at
      index i - 1. Then we will decided what to do
      after this.
    """
    bestMaxAtThisIndex += arr[i]

    """
      If 'bestMaxAtThisIndex' is < 0 then we will
      decide to not extend the best subarray at i - 1.
      We will just set the best we can achieve for subarrays
      ending at this index i to 0.
      The new 'currentStart' to the max subarray region becomes
      i + 1
    """
    if bestMaxAtThisIndex < 0:
      bestMaxAtThisIndex = 0
      currentStart = i + 1
    

    """
      If the best max (now the best max at this index) beats the
      best global max achieved so far then we need to adjust:
      'maxRegionStart' becomes the 'currentStart' we were keeping track
      of all along.
      'maxRegionEnd' becomes the index we are sitting at 'i'.
      The 'bestMaxSoFar' becomes the 'bestMaxAtThisIndex'.
    """
    if bestMaxAtThisIndex > bestMaxSoFar:
      maxRegionStart = currentStart
      maxRegionEnd = i
      bestMaxSoFar = bestMaxAtThisIndex
    

  

  return KadaneResult(bestMaxSoFar, maxRegionStart, maxRegionEnd)


    """
  Holds the result of running Kadan's algorithm
  maxSum: the actual sum of the Max Contiguous Subarray Sum region
  startIndex: start of Max Contiguous Subarray Sum region
  endIndex: end of Max Contiguous Subarray Sum region
    """
class KadaneResult:

  def __init__(maxSum, startIndex, endIndex) 
    self.maxSum = maxSum
    self.startIndex = startIndex
    self.endIndex = endIndex
  
"""
  A rectangle with left, right, top, and bottom bounds. The sum
  of all items contained within the rectangle are also recorded
  in the 'interiorSum' variable.
"""
class Rectangle:

    def __init__(self):
        self.interiorSum = 0
        self.leftBorderIndex
        self.rightBorderIndex
        self.topBorderIndex
        self.bottomBorderIndex




# ---------------------------------------------------------------------------------------------------
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
 
        rows = len(matrix)
        cols = len(matrix[0])

        """
        Create an array that will be a "vertical" array and record
        the running sums for each row in the each iteration of the
        left bound
        """
        runningRowSums =[0]* rows

        
        # This is the max rectangle that we will update along the way
        maxRectangle = Rectangle()

        # We will try all left bound plantings from index 0 to index cols - 1
        for left in range(cols):

             
          # We will reset the running row sums all to 0 since this is a new planting of the left bound
            for i in range(rows):
                runningRowSums[i] = 0
            
          # For each left bound, we will try all of the right bounds starting at the left bound we are planted at.
            for right in range(left,cols):

                # Add all items in column 'right' to their respective row's running sum
                for i in range(rows):
                    runningRowSums[i] += matrix[i][right]


                # Perform Kadane's algorithm on the running sum array so that we can determine the best top and bottom bound to choose for the rectangle.
                kadaneResult = self.kadane(runningRowSums)
        
                # If we notice that this rectangle can achieve a better maxSum than the best we have done so far then we need to adjust our new best
                if kadaneResult.maxSum > maxRectangle.interiorSum and kadaneResult.maxSum <= k:

                    # Set a new interiorSum for our maxRectangle
                    maxRectangle.interiorSum = kadaneResult.maxSum
                 

        return maxRectangle.interiorSum


    """
      An implementation of Kadane's algorithm that remembers the
      start and end of the Max Contiguous Subarray Sum region
      in the KadaneResult object returned
      This video explains Kadane's algorithm: https://www.youtube.com/watch?v=2MmGzdiKR9Y
    """
    def kadane(self,arr):
        
        # The best sum achieved for a region so far
        bestMaxSoFar = float('-inf')
        currSum = 0

        # We will process every element
        for i in range(len(arr)): 
 
            # Add this item to the best subarray achieved at index i - 1. Then we will decided what to do after this.
            currSum += arr[i]

            """
              If 'bestMaxAtThisIndex' is < 0 then we will
              decide to not extend the best subarray at i - 1.
              We will just set the best we can achieve for subarrays
              ending at this index i to 0.
              The new 'currentStart' to the max subarray region becomes
              i + 1
            """
            bestMaxSoFar = max(bestMaxSoFar,currSum)
            if currSum < 0:
                currSum = 0
    
            """
              If the best max (now the best max at this index) beats the
              best global max achieved so far then we need to adjust:
              'maxRegionStart' becomes the 'currentStart' we were keeping track
              of all along.
              'maxRegionEnd' becomes the index we are sitting at 'i'.
              The 'bestMaxSoFar' becomes the 'bestMaxAtThisIndex'.
            """   
        return KadaneResult(bestMaxSoFar)
"""
  Holds the result of running Kadan's algorithm
  maxSum: the actual sum of the Max Contiguous Subarray Sum region
  startIndex: start of Max Contiguous Subarray Sum region
  endIndex: end of Max Contiguous Subarray Sum region
"""
class KadaneResult:

    def __init__(self,maxSum):
        self.maxSum = maxSum
         
        """
        A rectangle with left, right, top, and bottom bounds. The sum
        of all items contained within the rectangle are also recorded
        in the 'interiorSum' variable.
        """
class Rectangle:

    def __init__(self):
        self.interiorSum = float('-inf')
        self.leftBorderIndex = 0
        self.rightBorderIndex = 0
        self.topBorderIndex = 0
        self.bottomBorderIndex = 0


  
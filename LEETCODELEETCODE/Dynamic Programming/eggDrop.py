class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        totalEggs, totalFloors = K,N
        cache = [[0 for _ in range(N+1)] for _ in range(K + 1)]

        # If we have 0 floors we need 0 trials, no matter the egg amount given
        # If we have 1 floor we need 1 trial, no matter the egg amount given
        # THE FIRST CELL IN ALL ROWS WILL BE 0, THE SECOND CELL IN ALL ROWS WILL BE 1
        for eggs in range(1, totalEggs+1):
            cache[eggs][0] = 0
            cache[eggs][1] = 1


        """
        If we have 1 egg...no matter what floors we get, our approach will
        be to do 'floorAmount' drops...this is because we want to start from
        floor 1, drop...then go to floor 2, drop...and so on until we get to
        in the worst case 'floorAmount'
        Remember, we want to know the minimum amount of drops that will always
        work. So we want to MINIMIZE...to the absolute LEAST...worst...amount
        of drops so that our drop count ALWAYS works
        Any worse then the MINIMIZED WORST will be suboptimal
        """
        # THE SECOND (EGG 1) ROW WILL BE THE VALUE OF THE NUMBER OF FLOORS
        # NO NEED TO SET THE 0TH ROW 0 BC IT IS BY DEFAULT 0
        for floor in range(1,totalFloors+1):
            cache[1][floor] = floor


        """
        Solve the rest of the subproblems now that we have base cases defined
        for us
        """
        
        # HERE WE ARE SOLVING OUR N*K SUBPROBLEMS
        for eggs in range(2,totalEggs +1):
            for floor in range(2,totalFloors+1):

                """
                Initialize the answer to this subproblem to a very large
                value that will be easily overtaken and provide a hard upper
                comparison wall
                """
                cache[eggs][floor] = float('inf')

                """
                We do a theoretical test on every floor from 1 to the 'floor'
                amount for this subproblem.
                At each 'attemptFloor' we express both possibilities described below
                """
                # EACH SUBPROBLEM HAS TO TRY DROPPING THE EGG AT EVERY FLOOR
                for attemptFloor in range(1,floor+1):


                    #  We want to know the cost of the 2 outcomes:
                    #  1.) We drop an egg and it breaks.
                    #   We move 1 floor down. We have 1 less egg.
                    #  2.) We drop an egg and it doesn't break.
                    #  We have this many floors left: the difference between the total floors and our current
                    #  floor. We have the same number of eggs.

                    costOfWorstOutcome = max(cache[eggs - 1][attemptFloor - 1], cache[eggs][floor - attemptFloor])

                    """
                    After we get the cost of the WORST outcome we add 1 to that worst outcome
                    to simulate the fact that we are going to do a test from THIS subproblem.
                    The answer to this problem is 1 PLUS the cost of the WORST SITUATION that
                    happens after our action at this subproblem.
                    """
                    accountingForDroppingAtThisSubproblem = 1 + costOfWorstOutcome

                """
                    Did we reach a BETTER (lower) amount of drops that guarantee that we can
                    find the pivotal floor where eggs begin to break?
                """
                    cache[eggs][floor] = min(cache[eggs][floor], accountingForDroppingAtThisSubproblem)


            """
            Remember we added +1 so we are indexed off of 1 now. We can reap our answer from
            cache[totalEggs][totalFloors] instead of cache[totalEggs - 1][totalFloors - 1]
            """
        return cache[totalEggs][totalFloors]



class Solution2:
    def superEggDrop(self, K: int, N: int) -> int:
        
        totalEggs, totalFloors = K,N
        cache = [[0 for _ in range(N+1)] for _ in range(K + 1)]

        # If we have 0 floors we need 0 trials, no matter the egg amount given
        # If we have 1 floor we need 1 trial, no matter the egg amount given
        # THE FIRST CELL IN ALL ROWS WILL BE 0, THE SECOND CELL IN ALL ROWS WILL BE 1
        for eggs in range(1, totalEggs+1):
            cache[eggs][0] = 0
            cache[eggs][1] = 1
 
        # THE SECOND (EGG 1) ROW WILL BE THE VALUE OF THE NUMBER OF FLOORS
        # NO NEED TO SET THE 0TH ROW 0 BC IT IS BY DEFAULT 0
        for floor in range(1,totalFloors+1):
            cache[1][floor] = floor

        
        # HERE WE ARE SOLVING OUR N*K SUBPROBLEMS
        for eggs in range(2,totalEggs +1):
            for floor in range(2,totalFloors+1):

                """
                Initialize the answer to this subproblem to a very large
                value that will be easily overtaken and provide a hard upper
                comparison wall
                """
                cache[eggs][floor] = float('inf')

              
                # EACH SUBPROBLEM HAS TO TRY DROPPING THE EGG AT EVERY FLOOR
                for attemptFloor in range(1,floor+1):

                    costOfWorstOutcome = max(cache[eggs - 1][attemptFloor - 1], cache[eggs][floor - attemptFloor])
                    accountingForDroppingAtThisSubproblem = 1 + costOfWorstOutcome
 
                    cache[eggs][floor] = min(cache[eggs][floor], accountingForDroppingAtThisSubproblem)

            """
            Remember we added +1 so we are indexed off of 1 now. We can reap our answer from
            cache[totalEggs][totalFloors] instead of cache[totalEggs - 1][totalFloors - 1]
            """
        return cache[totalEggs][totalFloors]

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        # If there are no floors, then no trials needed. OR if there is one floor, one trial needed. 
        if (totalFloors == 1 or totalFloors == 0):  return totalFloors 

        # We need k trials for one egg and k floors 
        if (totalEggs == 1): return totalFloors

        min_ = float('inf') 

        # Consider all droppings from 1st floor to kth floor and return the minimum of these values plus 1. 
        for floorToDropFirstEgg in range(1, totalFloors + 1): 

            res = max(eggDrop(totalEggs - 1, floorToDropFirstEgg - 1),  eggDrop(totalEggs, totalFloors - floorToDropFirstEgg)) 
            min_ = min(min_, res)

        return min_ + 1



class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
 

        cache = [[0 for _ in range(N+1)] for _ in range(K+1)]
        def rec(totalEggs,totalFloors):

            # If there are no floors, then no trials needed. OR if there is one floor, one trial needed. 
            if (totalFloors == 1 or totalFloors == 0):  return totalFloors 

            # We need k trials for one egg and k floors 
            if (totalEggs == 1): return totalFloors

            # IF THE ANSER IS CACHED, THEN USE IT
            if cache[totalEggs][totalFloors]: return cache[totalEggs][totalFloors]
            
            # if the value is not in the cache, then compute it
            min_ = float('inf') 

            # Consider all droppings from 1st floor to kth floor and return the minimum of these values plus 1. 
            for floorToDropFirstEgg in range(1, totalFloors + 1): 
                
                res = max(rec(totalEggs - 1, floorToDropFirstEgg - 1),  rec(totalEggs, totalFloors - floorToDropFirstEgg)) + 1
                min_ = min(min_,res)
                
            cache[totalEggs][totalFloors] = min_
            return cache[totalEggs][totalFloors]
        
 
        return rec(K,N)
    

class Solution:
def superEggDrop(self, K: int, N: int) -> int:
    
    # create the cache
    cache = [[0 for _ in range(N+1)] for _ in range(K+1)]
    
    #Initialize base case if there is only 1 floor
    for row in cache:
        row[1] = 1
    # Initialize the base case if there is only 1 egg
    for floor in range(len(cache[0])):
        cache[1][floor] = floor
        
    
    #We must solve every single subproblem
    for numOfEggs in range(2, len(cache)):
        for floor in range(2, len(cache[0])):
            
            cache[numOfEggs][floor] = float('inf')
            
            #the problem is EGG(i,j) - so drop the egg on each floor and take the minimum
            for droppedFloor in range(1,floor+1):
                
                #The egg either breaks, and we use 1 less floor, or the egg doesnt break, and we use Floors - droppedFloor floors
                # only take this floor if it is smaller than the other subproblems
                cache[numOfEggs][floor] = min(cache[numOfEggs][floor], 1 + max(cache[numOfEggs-1][droppedFloor-1], cache[numOfEggs][floor-droppedFloor]))
                
    return cache[-1][-1]

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        
        cache = [[0 for _ in range(N+1)] for _ in range(K+1)]
        
        def rec(eggs, floors):
            
            if floors == 0 or floors == 1 or eggs == 1: return floors
            
            #check the cache
            if cache[eggs][floors]: return cache[eggs][floors]
            
            cache[eggs][floors] = float('inf') # set hard upper bound
        
            #drop the egg at every spot
            for floorToDropFirstEgg in range(1,floors+1):
                cache[eggs][floors] = min(cache[eggs][floors], 1 + max(rec(eggs-1, floorToDropFirstEgg -1), rec(eggs, floors - floorToDropFirstEgg)))
            
            #return the lowest value from all the subproblems
            return cache[eggs][floors]
            
        
        return rec(K,N)

        
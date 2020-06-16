

def maxProduct(nums):

    maximum=big=small=nums[0]

    for current in nums[1:]:

        # WE NEED TO TRACK THE BIGGEST AND SMALLEST NUMBERS BC THE NEXT NUMBER MAY ALSO BE NEGATIVE AND MAKE THE NEGATIVE NUMBER MASSIVE
        big, small =max(current, current*big, current*small), min(current, current*big, current*small)

        # WHEN COMPARING TO THE MAXIMUM WE IGNORE THE "SMALL" BC IT IS NEGATIVE. THE IMPORTANCE OF KEEPING "SMALL"
        # FOR THE NEXT ITERATION IS BECAUSE "SMALL" MAY BE NEGATIVE AND BECOME HUGE "NEXT ITERATION" - NOT THIS ONE
        maximum=max(maximum, big)

    return maximum
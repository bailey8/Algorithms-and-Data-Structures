def maxProduct(nums):
    maximum=big=small=nums[0]
    for n in nums[1:]:
        # Current biggest can be biggest*small or biggest*bi cause next num might be negative
        big, small=max(n, n*big, n*small), min(n, n*big, n*small)
        maximum=max(maximum, big)
    return maximum
def twoSum(arr,target):
    dic = {}
    for i,num in enumerate(arr):
        if target-num in dic:
            return [i,dic[target-num]]
        dic[num] = i



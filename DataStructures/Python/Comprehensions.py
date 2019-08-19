# arr = [9,8,7,6,5]

# for i, value in enumerate(arr,):
#     print(i,value)

# dic = {'a':1,'b':5}
# print(max(dic.values()))

# arr = [1,2,2,3,3,3,3,3,4,4,4,4,4,4,5,5,5]
# from collections import Counter, defaultdict
# a = Counter(arr)
# print(a)

# a = defaultdict(list)
# a[88] = 100
# print(a.values)

# a = [1,2,3,4,5]
# print(tuple(a))

# print({i:j for i,j in enumerate([1,2,3,4,5])})
a = [1,2,3]
b = [0,0,0]
# for i,j in zip(a,b):
#     print(i,j)

# p1 = [1,2]
# p2 = [2,2]

# squared = [a**2 + b**2 for a,b in zip(p1,p2) if a == 1 and a !=2]

# def fun(i):
#     return i*2

# print([fun(i+1) for i in range(5)])

# print(squared)


list = [9,2,3,4]

print(list.sort())
print(sorted(list)[:2])
print([i for  _, i in [[1,2],[3,4],[5,6]]])
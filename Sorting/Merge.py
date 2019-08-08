
# def merge(list1,list2):
#     i=0;j=0
#     full = []
#     while i<len(list1) and j<len(list2):
#         if list1[i] < list2[j]:
#             full.append(list1[i])
#             i +=1
#         else:
#             full.append(list2[j])
#             j += 1
#     while i< len(list1):
#         full.append(list1[i])
#         i += 1
#     while j < len(list2):
#         full.append(list2[j])
#         j += 1
#     return full

def merge(l,r):
    i = j = 0
    full = []
    while i< len(l) and j < len(r):
        if l[i] <= r[j]:
            full.append(l[i])
            i +=1
        else:
            full.append(l[j])
            j +=1
    while i < len(l):
        full.append(l[i])
        i +=1
    while j < len(r):
        full.append(r[j])
        j +=1
    return full

 


a = merge([1,2],[3,4])

print(a)

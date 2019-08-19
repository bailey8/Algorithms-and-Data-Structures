import heapq

heap = []
data = [9,8,7,6,5]

#First element used
for item in data:
    heapq.heappush(heap,[item,99,1000])

print(heap)
# for item in data:
#     heapq.heappush(heap,(item,99))

# Transform list into heap in linear time using sift-down
heapq.heapify(data)
print(data)


from queue import PriorityQueue

q = PriorityQueue()
q.put((1,99))
q.put((2,98))
q.put((3,97))
print(q.get())




# 1) Loop through all nodes and check if they are visited first
        # -- Every Loop (connected component) update the "component count"
# 2) When you visit a node, update its visited status
        # -- Link the node to the specific component its in
# 3) call DFS on all edge nodes in adjacency list for current node
from collections import defaultdict
class Solution:
    def overlap(self, a, b):
        return a[0] <= b[-1] and b[0] <= a[-1]

    # generate graph where there is an undirected edge between intervals u
    # and v iff u and v overlap.
    def build_graph(self, intervals):
        graph = defaultdict(list)

        #For every Interval
        for i, interval in enumerate(intervals):
            #Add every other interval that overlaps as an edge on BOTH intervals
            for j in range(i+1, len(intervals)):
                #Only add other 
                if self.overlap(interval, intervals[j]):
                    graph[interval].append(intervals[j])
                    graph[intervals[j]].append(interval)

        return graph


    # merges all of the nodes in this connected component into one interval.
    def merge_nodes(self, nodes):
        min_start = min(node[0] for node in nodes)
        max_end = max(node[-1] for node in nodes)
        return [min_start, max_end]

    # gets the connected components of the interval overlap graph.
    def get_components(self, graph, intervals):
        visited = set()
        COMP_NUM = 0
        COMP_NODES = defaultdict(list)

        def mark_component_dfs(start):
            stack = [start]
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    COMP_NODES[COMP_NUM].append(node)
                    #For all neighbors of the vertex - add to stack
                    stack.extend(graph[node])

        # mark all nodes in the same connected component with the same integer.
        for interval in intervals:
            if interval not in visited:
                mark_component_dfs(interval)
                COMP_NUM += 1

        return COMP_NODES, COMP_NUM

    def merge(self, intervals):
        graph = self.build_graph(intervals)
        COMP_NODES, COMP_NUM = self.get_components(graph, intervals)

        # all intervals in each connected component must be merged.
        return [self.merge_nodes(COMP_NODES[comp]) for comp in range(COMP_NUM)]


class Solution2:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][-1] < interval[0]:
                merged.append(interval)
            else:
            # otherwise, there is overlap, so we merge the current and previous
            # intervals.
                merged[-1][-1] = max(merged[-1][-1], interval[-1])
        return merged


a = [1,2,3]
b =[a]
print(b)

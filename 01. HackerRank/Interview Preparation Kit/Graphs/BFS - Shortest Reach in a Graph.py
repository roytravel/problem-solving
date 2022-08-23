from collections import defaultdict
from collections import deque

# solution
class Graph:
    def __init__(self, n, m):
        self.graph = defaultdict(list)
        self.n_node = n
        self.n_edge = m
        
    def connect(self, x, y):
        self.graph[x].append(y)
        self.graph[y].append(x)
        
    def find_all_distances(self, start):
        queue = deque([start])
        dists = defaultdict(int)
        visit = set()
        visit.add(start)
        while queue:
            s = queue.popleft()
            for x in self.graph[s]:
                if x not in visit:
                    visit.add(x)
                    queue.append(x)
                    dists[x] = dists[s] + 6
        
        for i in range(1, n+1):
            if i == start:
                continue
            if i in dists.keys():
                print (dists[i], end = ' ')
            else:
                print (-1, end = ' ')
        print()

# half success
# class Graph:
#     def __init__(self, n, m):
#         self.graph = defaultdict(list)
#         self.n_node = n
#         self.n_edge = m
        
#     def connect(self, x, y):
#         self.graph[x].append(y)
#         self.graph[y].append(x)
        
#         self.graph[x].sort()
#         self.graph[y].sort()
        
        
#     def find_all_distances(self, start):
#         queue = deque([start])
#         dists = defaultdict(int)
#         visit = set()
#         visit.add(start)
#         dist = 6
#         while queue:
#             s = queue.popleft()
#             temp = []
#             for x in self.graph[s]:
#                 if x not in visit:
#                     visit.add(x)
#                     dists[x] = dist
#                     queue.append(x)
#                     temp.append(True)
#                 else:
#                     temp.append(False)
            
#             if len(self.graph[s]) != temp.count(False):
#                 dist += 6
        
#         for i in range(1, n+1):
#             if i == start:
#                 continue
#             elif i not in dists.keys():
#                 print (-1, end = ' ')
#             else:
#                 print (dists[i], end = ' ')
#         print ()
        
        
t = int(input()) # test case
for i in range(t):
    n, m = [int(value) for value in input().split()] # num of node and edge
    graph = Graph(n, m)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x,y) 
    s = int(input())
    graph.find_all_distances(s)

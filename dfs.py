x = [1,2,3,4,5,6,7,8,9,10]
y = [ [[1,2], [1,4], [1,7]], \
      [[2,1],[2,3],[2,4]], \
      [[3,2], [3,4], [3,5], [3,8]], \
      [[4,1], [4,2], [4,3],[4,5]], \
      [[5,3], [5,4], [5,6], [5,9]], \
      [[6,5], [6,7],[6,9]], \
      [[7,1], [7,6]], \
      [[8,3],[8,9],[8,10]], \
      [[9,6],[9,8], [9,10]], \
      [[10,8],[10,9]] \
    ]

NOTVISITED = 0
VISITED = 1 

trackVisited = [NOTVISITED for elem in x]
traversal = [0 for elem in x]
visitedList = []

def getIndex(node):
    return x.index(node)
    
def visited(node):
    return trackVisited[getIndex(node)] == VISITED

def dfs(graph,source):
    idx = getIndex(source)
    if (trackVisited[idx] == VISITED):
        return
    trackVisited[idx] = VISITED
    visitedList.append(source)
    for adjNodeIdx in range(len(y[idx])):
        adjNode = y[idx][adjNodeIdx][1] 
        if( visited(adjNode) == False):
            dfs(graph,adjNode)

dfs(y,1)

print visitedList
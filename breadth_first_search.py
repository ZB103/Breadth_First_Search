from random import randint

def breadth_search(arr, target):
    #Visited[] records whether a node has been
    #visited range 1-5; 1 for visited 0 for not visited
    visited = [0 for i in range(6)]
    #Queue[] records neighbors that
    #need to be visited for the current node
    queue = []
    
    #For each row (node), check whether it is the target.
    i = 0
    while i != target:
        #Otherwise, record neighbors that have not been already visited
        for j in range(6):
            #if has neighbor and neighbor is not visited
            if arr[i][j] == 1 and visited[j] == 0:
                #if is not already in queue
                isQueued = False
                for k in range(len(queue)):
                    if queue[k] == j:
                        isQueued = True
                if not isQueued:
                    #add to queue
                    queue.append(j)
    
        #Check whether all of the nodes have been visited
        #and whether queue is empty.
        #If so, exit. (The value was not in the list)
        allNodesVisited = True
        for j in range(len(visited)):
            if visited[j] == 0:
                allNodesVisited = False
        if allNodesVisited or len(queue) == 0:
            return False
        
        #Mark node as visited
        visited[i] = 1
        #move to next i
        i = queue[0]
        queue.pop(0)
    return True

def create_graph():
    rows = 6
    columns = 6
    arr = [[0 for i in range(columns)] for j in range(rows)]
    #columns
    for i in range(0,5):
        #rows
        for j in range(1, 6):
            #assign random number
            arr[i][j] = randint(0,1)
            #flip symmetrical row/column
            arr[j][i] = arr[i][j]
    #every node needs a path to at least one other node
    for i in range(1,6):
        if not breadth_search(arr, i):
            x = randint(0,i-1)
            arr[i][x] = 1
            arr[x][i] = arr[i][x]
    #no node can have a path to itself
    for i in range(6):
        arr[i][i] = 0
    return arr


#create and print graph matrix
graph = create_graph()
print("Graph Matrix:")
print("   0, 1, 2, 3, 4, 5 ")
for i in range(6):
    print()
    print(str(i) + " " + str(graph[i]))
print()

#find and record search process for randomly chosen value
target = randint(0,6)
print("Searching for " + str(target) + ", starting from 0")
if(breadth_search(graph, target)):
    print("Target " + str(target) + " was found! Exiting search.")
else:
    print("Target " + str(target) + " was NOT found in the graph. Exiting search.")
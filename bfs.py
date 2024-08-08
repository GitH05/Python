graph={
    "a":["b","d"],
    "b":[],
    "c":[],
    "d":["e","g"],
    "e":["c"],
    "f":[],
    "g":["f"]
}

def bfs(graph,source):  #define a method for the dfs traversal 
    queue=[]            #using an empty queue for the traversal 
    queue.append(source)#adding the source node into the queue    

    while queue:        #until the queue exist/not-empty
        node =queue.pop(0)#pop() the queue element/node__as it FIFO delete the first element
        # '0' is used to pop() from the first/front
        print(node,end=" ")#print the pop() element/node
        for neighbour in graph[node]:#for each neighbour of poped() node
            queue.append(neighbour)  #append all the neighbour into the queue and continue the above process
bfs(graph,"a")
# print("\n",graph["a"]
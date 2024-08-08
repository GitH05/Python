graph={
    "a":["b","d"],
    "b":[],
    "c":[],
    "d":["e","g"],
    "e":["c"],
    "f":[],
    "g":["f"]
}

def dfs(graph,source):  #define a method for the dfs traversal 
    stack=[]            #using an empty stack for the traversal 
    stack.append(source)#adding the source node into the stack    

    while stack:        #until the stack exist/not-empty
        node =stack.pop()#pop() the stack element/node
        print(node,end=" ")#print the pop() element/node
        for neighbour in graph[node]:#for each neighbour of poped() node
            stack.append(neighbour)  #append all the neighbour into the stack and continue the above process
dfs(graph,"a")
# print("\n",graph["a"]
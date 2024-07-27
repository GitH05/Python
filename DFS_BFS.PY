#GRAPH:collection of nodes/vertex and edges.
#DFS:Approach a particular path and use stack as a memory.
#BFS:Approach all the neighbours path and use queue as a memory
graph={
    "a":["b","c"],
    "b":[],
    "c":["e","f"],
    "d":[],
    "e":["d"],
    "f":["g"]
}
#now creating a function for the DFS using graph and a root-node as a source
def DFS(graph,root):
    stack=[] #initialising a empty stack to holde the root element(starting point)
    stack.append(root)  #adding the root element in the empty stack

    while stack:
        node=stack.pop(-1)    #poping the root element and it's neighbours through stack and continue
        print(node,end=" ")     #display all the poped elements and it's neighbours through stack 

        for neighbour in graph[root]:   #iterating all the adjascent of the root element---to find the near by node
            stack.append(neighbour)     #adding all the neighbours to it's respective source/root element and continuing the while loop  
print("graph:",graph)
print("DFS")
DFS(graph,"a")      #putting "a" as the source/root element.
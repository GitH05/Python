# similar to the path_directed_graph ,the difference is only that it can come back to visit the neighbour elements;
#to avoid the visiting of the previous elements we use new variable as visited and declare it out to the iteration;
graph={
    "a":["b","c"],
    "b":["d","f"],
    "c":[],
    "d":["i","g"],
    "e":["h"],
    "f":["e"],
    "g":["h"],
    "h":[],
    "i":[]
}
def path(src,des,vis,graph):
    if src==des:
        return True
    vis.add(src)
    
    print(vis)
    boolvar=False
    for neighbour in graph[src]:
       if neighbour not in vis:
            boolvar=boolvar or path(neighbour,des,vis,graph)
    return boolvar
print("graph:",graph)
src=str(input("Enter the source from the above graph:"))
des=str(input("Enter the destination from the above graph:"))
if src not in graph:
    print("Invalid Source!")
if des not in graph:
    print("Invalid Destination!")

vis=set()
print(path(src,des,vis,graph))
# Declaring that a path exist between the 'source' and the 'destination' of the graph: true/false
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
def path(src,des,graph):
    if src==des:        #source=destination then states true
        return True
    boolvar=False
    for neighbour in graph[src]:        #finding the adjascent elements of the source element
        boolvar=boolvar or path(neighbour,des,graph)      #if source exist==true, else false (continue for all the neighbours)
    return boolvar
src=str(input("Enter the source:"))
des=str(input("Enter the destination:"))

if src not in graph:
         print("Invalid Source")
if des not in graph:
         print("Invalid Destination")    
    

print(path(src,des,graph))
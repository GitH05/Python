'''check if the path exist between source and destination(undirected graph)'''
graph ={
    "a":["b","c"],
    "b":["a","f","d"],
    "c":["a"],
    "d":["b","g","i"],
    "e":["f","h"],
    "f":["b","e"],
    "g":["d","h"],
    "h":["e","h"],
    "i":["d"]
}
def path(src,dest,graph,visited):
    print("Path exist between:",src,"and",dest)
    if src==dest:
        return True
    
    visited.add(src)
    ans=False

    for neighbour in graph[src]:
        if neighbour not in visited:
            ans=ans or path(neighbour,dest,graph,visited)
    return ans
visited=set()
src=input("enter the source:")
dest=input("enter the destination:")
print(path(src,dest,graph,visited))
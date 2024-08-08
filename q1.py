'''check if path exists between source and destination('directed and acyclic graph)'''
''' 

     f__>e   
     ^
     |    
     a__>b__>d__>g__>h
     |       |
     ^       ^
     c       i
     
     
   
   '''

'''
source="a"
destination="g"
#algorithm:
-if src==dest,return true
-use a bool var to keep track of the dfs call
-make call to the neighbour
-return answer   
'''
graph={
    "a":["b","c"],
    "b":["f","d"],
    "c":[],
    "d":["g","i"],
    "e":["h"],
    "f":["e"],
    "g":["h"],
    "h":[],
    "i":[]
}

def path(src,dest,graph):
    if src==dest:
        return True
    
    ans=False
    for neighbour in graph[src]:
        ans=ans or path(neighbour,dest,graph)
        # print(path(neighbour,dest,graph),":",neighbour,end=",")
        if ans==True:
            print("Thus path exist:",neighbour)
        else:
            print("path not exist:",neighbour)
    # return ans
    # print(path(neighbour,dest,graph),":",neighbour,end=",")
print("Check path existence:")
src=input("enter the source:")
dest=(input("enter the destination:"))
print(path(src,dest,graph))
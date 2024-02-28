graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
visited = []
queue = []

def bfs(visited,graph,node):
   visited.append(node)
   queue.append(node)
   
   while queue:
       closenode=queue.pop(0)     
       print("closing the nodde",closenode)   
       for neighbour in graph[closenode]:
           if neighbour not in visited:
               visited.append(neighbour)
               queue.append(neighbour)

    
            
            
bfs(visited,graph,'A')    

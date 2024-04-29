graph = {
    'A' : ['B','C'],
    'B' : ['C','A'],
    'C' : ['B','A','E','D'],
    'D' : ['C','E'],
    'E' : ['D','C'],
    
}
goal_state = 'F'
visited = set()
colors = ["red","green","orange","blue"]
colored = {}
possibilities = ()
def give_color(node,color):
    for i in graph[node]:
        
        if  colored.get(i) == color:
            return False
        else:
            pass
    return True


def completed_coloring():
    if len(colored) == len(graph):
            possibilities.append(colored.copy())  # Store a copy of the colored dictionary
            colored.clear  # Backtrack after storing the coloring
            return True
        
    return False
def dfs(visited ,graph,node):
    if node not in visited:
        print("visiting the node",node)
        
        visited.add(node)
        for i in colors:
             if (give_color(node,i)):
                 print(colored)
                 
                 colored[node]=i
                 '''for neighbour in graph[node]:
                    dfs(visited,graph,neighbour)'''
                 dfs(visited,graph,next_node(node)) 
                 if len(colored) == len(graph):  # Check if all nodes are colored
                    possibilities.append(colored.copy())# Recursive call to
                    colored.clear
                
                 
    '''for neighbour in graph[node]:
            dfs(visited,graph,neighbour)'''
            
def dfs1(visited ,graph,node):
    if node not in visited:
        print("visiting the node",node)
        
        visited.add(node)
        for i in colors:
             if (give_color(node,i)):
                 print(colored)
                 colored[node]=i
                 for neighbour in graph[node]:
                    dfs(visited,graph,neighbour)
                 #dfs(visited,graph,next_node(node)) 
                 if len(colored) == len(graph):  # Check if all nodes are colored
                    possibilities.append(colored.copy())# Recursive call to
                 colored.clear
                
                 
    '''for neighbour in graph[node]:
            dfs(visited,graph,neighbour)'''
        
def next_node(node):
    nodes = list(graph.keys())
    index = nodes.index(node)
    return nodes[(index + 1) % len(nodes)]

dfs(visited,graph,'A')
print(colored)

for i in possibilities:
    print(i)








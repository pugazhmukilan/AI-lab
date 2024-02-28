graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set()

def dfs(visited ,graph,node):
    if node not in visited:
        print("visiting the node",node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)


dfs(visited,graph,'A')

'''
PROCEDURE:
1) intilizing the graph structuring it 
2)creating a visited set 
3)create a function for dfs
4)parameters should be visited set,graph,node
5)first it will check wehter the node is visited or not 
6)if not then that node will be added to the visited
7)now the function will check the neighbouing nodes of the given node and then use dfs for it and the process
continues.....
'''
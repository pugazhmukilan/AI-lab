graph = {
    'A': ['B', 'C'],
    'B': ['C', 'A'],
    'C': ['B', 'A', 'E', 'D'],
    'D': ['C', 'E'],
    'E': ['D', 'C']
}

colors = ["red", "green", "orange", "blue"]
possible_colorings = []

def is_safe(node, color, colored):
    for neighbor in graph[node]:
        if neighbor in colored and colored[neighbor] == color:
            return False
    return True

def dfs(node, colored):
    if node not in colored:
        for color in colors:
            if is_safe(node, color, colored):
                colored[node] = color
                dfs(next_node(node), colored)
                if len(colored) == len(graph):  # Check if all nodes are colored
                    possible_colorings.append(colored.copy())
                colored.pop(node)

def next_node(node):
    nodes = list(graph.keys())
    index = nodes.index(node)
    return nodes[(index + 1) % len(nodes)]

dfs('A', {})
for i in possible_colorings:
    print(i)

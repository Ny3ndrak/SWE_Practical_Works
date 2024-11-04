#EXERCISES

# 1. Implement a method to find the shortest path between two vertices using BFS
from collections import deque

def bfs_shortest_path(graph, start, goal):

    visited = set()

    queue = deque([[start]])
    
    while queue:
        # Get the first path from the queue
        path = queue.popleft()
        
        # Get the last node from the path
        node = path[-1]
        
        # Check if the node is the goal
        if node == goal:
            return path
        
        # If the node is not visited
        elif node not in visited:
            # Mark the node as visited
            visited.add(node)
            
            # Get the neighbors of the node
            for neighbor in graph.get(node, []):
                # Create a new path
                new_path = list(path)
                new_path.append(neighbor)
                # Add the new path to the queue
                queue.append(new_path)
  
    return None

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start = 'A'
goal = 'F'
print(bfs_shortest_path(graph, start, goal)) 

#2.Add a method to detect cycles in the graph.
def detect_cycle_directed(graph):
    def dfs(node):
        if node in visiting:
            return True
        if node in visited:
            return False
        visiting.add(node)
        for neighbor in graph.get(node, []):
            if dfs(neighbor):
                return True
        visiting.remove(node)
        visited.add(node)
        return False

    visited = set()
    visiting = set()

    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

# Example usage
graph_directed = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['C'],
    'E': []
}

print(detect_cycle_directed(graph_directed))  # Output: True (Cycle: C -> E -> D -> C)

#3.Implement Dijkstra's algorithm to find the shortest path in a weighted graph.

import heapq

def dijkstra(graph, start):
    
    priority_queue = [(0, start)]
    shortest_paths = {start: (None, 0)}
    
    while priority_queue:
        (current_distance, current_node) = heapq.heappop(priority_queue)
        
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if neighbor not in shortest_paths or distance < shortest_paths[neighbor][1]:
                shortest_paths[neighbor] = (current_node, distance)
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

def shortest_path(graph, start, end):
    paths = dijkstra(graph, start)
    route = []
    if end not in paths:
        return None
    
    while end is not None:
        route.append(end)
        next_node = paths[end][0]
        end = next_node
    
    route = route[::-1]
    return route, paths[route[-1]][1]

# Example usage
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start = 'A'
end = 'D'
path, distance = shortest_path(graph, start, end)
print(f"The shortest path from {start} to {end} is {path} with a total distance of {distance}.")

#4.Create a method to determine if the graph is bipartite.
from collections import deque

def is_bipartite(graph):
    color = {}
    
    for node in graph:
        if node not in color:
            queue = deque([node])
            color[node] = 0
            while queue:
                current = queue.popleft()
                for neighbor in graph[current]:
                    if neighbor not in color:
                        color[neighbor] = 1 - color[current]
                        queue.append(neighbor)
                    elif color[neighbor] == color[current]:
                        return False
    return True

# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

print(is_bipartite(graph))  # Output: True

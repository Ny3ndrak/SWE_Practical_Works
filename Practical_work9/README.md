In this lab, i've implemented a graph data structure and basic graph traversal algorithms in Python. I've practiced creating a Graph class, implementing DFS and BFS, finding all paths between two vertices, and checking if a graph is connected.

These fundamental graph algorithms form the basis for solving many complex problems in computer science. As i worked on the additional exercises, i gained a deeper understanding of graph theory and its applications.




# EXERCISE EXPLANATION

# 1.Implement a method to find the shortest path between two vertices using BFS
Graph Representation: The graph is represented as a dictionary where each node has a list of adjacent nodes.
Queue Initialization: The queue is initialized with a path containing the start node.

BFS Loop:
Dequeue the first path and get the last node.
If the last node is the goal, return the path.
If the last node has not been visited, mark it as visited and enqueue new paths with its neighbors.
Return the Path: If the goal is reached, the path is returned. If the queue is empty and the goal is not reached, return None.

# 2.Add a method to detect cycles in the graph.

Directed Graph:

DFS Function:
Uses two sets (visited and visiting) to track nodes.
If a node is in visiting, a cycle is detected.
After visiting all neighbors, moves the node to visited.

Cycle Detection:
Iterates through all nodes, running DFS from each unvisited node.
Returns True if a cycle is found.

Undirected Graph:

DFS Function:
Similar approach to the directed graph but tracks the parent node to avoid false cycle detection.
If a neighbor is visited and not the parent, a cycle is detected.

Cycle Detection:
Iterates through all nodes, running DFS from each unvisited node.
Returns True if a cycle is found.

# 3.Implement Dijkstra's algorithm to find the shortest path in a weighted graph.

Priority Queue:
Uses heapq to manage the priority queue, allowing for efficient retrieval of the smallest distance node.

Dijkstra Function:
Initializes the priority queue and the shortest path dictionary.
Pops the node with the smallest distance from the queue.
Updates the shortest path if a shorter path is found to a neighboring node.
Pushes the updated distances of neighboring nodes back into the queue.

Shortest Path Function:
Uses the results of the Dijkstra function to construct the shortest path from the start node to the end node.

Traverses the path dictionary from the end node to the start node to build the route.
Reverses the route to get the correct order from start to end.

Example Usage:
Defines a sample graph with weighted edges.
Finds the shortest path from node 'A' to node 'D' using the shortest_path function.
Prints the shortest path and the total distance.

# 4.Create a method to determine if the graph is bipartite.

Color Dictionary:
Keeps track of the color assigned to each node. Nodes can be colored with 0 or 1.

BFS Initialization:
For each uncolored node, start a BFS. This ensures disconnected components are also checked.
Initialize the color of the starting node to 0 and add it to the queue.

BFS Loop:
Dequeue a node and check its neighbors.
If a neighbor is not colored, color it with the opposite color (1 - current color) and enqueue it.
If a neighbor is already colored and has the same color as the current node, the graph is not bipartite.

Return Result:
If no conflicts are found, the graph is bipartite.
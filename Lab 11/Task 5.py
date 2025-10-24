from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}
    
    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list:
            self.adjacency_list[vertex1] = []
        if vertex2 not in self.adjacency_list:
            self.adjacency_list[vertex2] = []    
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)   
    def bfs(self, start_vertex):
        if start_vertex not in self.adjacency_list:
            return []
        visited = set()
        queue = deque([start_vertex])
        result = []
        while queue:
            current_vertex = queue.popleft()
            if current_vertex not in visited:
                visited.add(current_vertex)
                result.append(current_vertex)
                
                neighbors = self.adjacency_list[current_vertex]
                unvisited_neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]
                queue.extend(unvisited_neighbors)
        return result
    def dfs_recursive(self, start_vertex, visited=None, result=None):
        if visited is None:
            visited = set()
            result = []
        
        if start_vertex not in self.adjacency_list:
            return result
        
        if start_vertex not in visited:
            visited.add(start_vertex)
            result.append(start_vertex)
            
            neighbors = self.adjacency_list[start_vertex]
            unvisited_neighbors = [neighbor for neighbor in neighbors if neighbor not in visited]
            
            for neighbor in unvisited_neighbors:
                self.dfs_recursive(neighbor, visited, result)
        
        return result

# Test
if __name__ == "__main__":
    graph = Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F')]
    
    for edge in edges:
        graph.add_edge(edge[0], edge[1])
    
    print(f"Graph: {dict(graph.adjacency_list)}")
    print(f"BFS from A: {graph.bfs('A')}")
    print(f"DFS from A: {graph.dfs_recursive('A')}")
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, edges):
        """Add a vertex and its associated edges to the graph."""
        self.vertices[name] = edges

    def shortest_path(self, start, end):
        """Find the shortest path using Dijkstra's algorithm."""
        shortest_paths = {vertex: (float('infinity'), None) for vertex in self.vertices}
        current_distance = 0
        current_vertex = start

        while current_vertex != end:
            for neighbour, weight in self.vertices[current_vertex].items():
                new_distance = current_distance + weight
                if new_distance < shortest_paths[neighbour][0]:
                    shortest_paths[neighbour] = (new_distance, current_vertex)

            next_destinations = {vertex: shortest_paths[vertex] for vertex in self.vertices.keys()
                                 if vertex not in shortest_paths}
            if not next_destinations:
                return "Path not found."
            current_vertex = min(next_destinations, key=lambda k: next_destinations[k][0])
            current_distance = shortest_paths[current_vertex][0]

        path = []
        while current_vertex:
            path.append(current_vertex)
            next_vertex = shortest_paths[current_vertex][1]
            current_vertex = next_vertex
        return path[::-1]

# Sample graph
g = Graph()
g.add_vertex('A', {'B': 1, 'C': 4})
g.add_vertex('B', {'A': 1, 'C': 2, 'D': 5})
g.add_vertex('C', {'A': 4, 'B': 2, 'D': 1})
g.add_vertex('D', {'B': 5, 'C': 1})
print("Shortest path from A to D:", g.shortest_path('A', 'D'))
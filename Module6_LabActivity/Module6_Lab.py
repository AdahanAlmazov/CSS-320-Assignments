class Graph:
    def __init__(self):
        #Initialize the instance with an empty dictionary
        self.graph = {}
        
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        
    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        else:
            raise ValueError("One or both vertices do not exist in the graph.")
        
    def display(self):
        for vertex, neighbors in self.graph.items():
            print(f"{vertex}: {neighbors}")
            
def main():
    my_graph = Graph()
    my_graph.add_vertex("A")
    my_graph.add_vertex("B")
    my_graph.add_vertex("C")
    my_graph.add_edge("A", "B")
    my_graph.add_edge("B", "C")
    my_graph.add_edge("A", "C")
    my_graph.display()
    
    
if __name__ == '__main__':
    main()
        
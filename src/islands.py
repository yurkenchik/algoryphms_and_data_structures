import csv

def read_graph_from_csv(file_name):
    """
    Reads graph data from a CSV file.

    :param file_name: The name of the CSV file containing graph data.
    :return: The number of vertices and a list of edges.
    """
    vertices = 0
    edges = []

    with open(file_name, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            start_vertex, end_vertex, weight = map(int, row)
            vertices = max(vertices, start_vertex, end_vertex)
            edges.append((start_vertex, end_vertex, weight))

    return vertices + 1, edges

class DisjointSet:
    def __init__(self, vertices):
        """
        Initializes the Disjoint Set object.

        :param vertices: The number of vertices in the set.
        """
        self.rank = [0] * (vertices + 1)  # Initialize ranks for each vertex.
        self.parent = [i for i in range(vertices + 1)]  # Initialize parent nodes for each vertex.

    def search(self, node):
        """
        Returns the root parent node for the given node using path compression.

        :param node: The node to find the root parent for.
        :return: The root parent node for the given node.
        """
        if self.parent[node] == node:
            return self.parent[node]
        return self.parent[node] == self.search(self.parent[node])

    def union(self, left_part, right_part):
        """
        Unites two parts (sets).

        :param left_part: The first element to be united.
        :param right_part: The second element to be united.
        """
        left_root = self.search(left_part)
        right_root = self.search(right_part)

        if left_root != right_root:
            if self.rank[left_root] < self.rank[right_root]:
                self.parent[left_root] = right_root
            elif self.rank[left_root] > self.rank[right_root]:
                self.parent[right_root] = left_root
            else:
                self.parent[right_root] = left_root
                self.rank[left_root] += 1

def minimal_length_of_cables_counter(vertices, edges):
    """
    Computes the minimal length of cables required to connect all vertices in the graph.

    :param vertices: The number of vertices in the graph.
    :param edges: The list of graph edges in the format (start_vertex, end_vertex, weight).
    :return: The minimal length of cables and the minimum spanning tree in the format (length, spanning_tree).
    """
    result = []  # Stores the edges of the minimal spanning tree.
    current_edge_index = 0
    connected_vertices_counter = 0
    edges = sorted(edges, key=lambda weight: weight[2])  # Sort the graph edges by weight.
    disjoint_set = DisjointSet(vertices)  # Initialize the disjoint set.

    while connected_vertices_counter < vertices - 1 and current_edge_index < len(edges):
        start_point, end_point, weight = edges[current_edge_index]
        current_edge_index += 1
        if disjoint_set.search(start_point) != disjoint_set.search(end_point):
            connected_vertices_counter += 1
            result.append([start_point, end_point, weight])  # Add edge to the minimal spanning tree.
            disjoint_set.union(start_point, end_point)  # Union the sets of start and end points.

    minimal_length_of_cables = sum(edge[2] for edge in result)  # Calculate the total length of cables.
    return minimal_length_of_cables, result

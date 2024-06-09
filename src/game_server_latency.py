from avl_priority_queue import *
import heapq

def parse_data_from_file(path):
    with open(path, "r", encoding="UTF-8") as file:
        data = file.readlines()

    number_of_vertexes, number_of_edges = map(int, data[0].split())
    client_nodes = set(map(int, data[1].split()))
    adjacency_list = {node: [] for node in range(1, number_of_vertexes + 1)}

    for i in range(2, number_of_edges + 2):
        start_node, end_node, latency = map(int, data[i].split())
        adjacency_list[start_node].append((end_node, latency))
        adjacency_list[end_node].append((start_node, latency))

    return adjacency_list, client_nodes

def dijkstra(adjacency_list, client_nodes, node_number, priority_queue_tree: AvlTree) -> int:
    distances = {node: float("inf") for node in adjacency_list}
    distances[node_number] = 0

    priority_queue_tree.insertion_by_priority(None, node_number, 0)

    while priority_queue_tree.root:
        current_distance, current_node = priority_queue_tree.root.priority, priority_queue_tree.root.value

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in adjacency_list[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                priority_queue_tree.insertion_by_priority(None, neighbor, distance)

    shortest_paths = {node: distances[node] for node in client_nodes}

    return max(shortest_paths.values())

def best_server_place(adjacency_list, client_nodes):
    router_nodes = [router for router in adjacency_list.keys() if router not in client_nodes]

    result = []
    for router in router_nodes:
        priority_queue_tree = AvlTree()
        max_latency = dijkstra(adjacency_list, client_nodes, router, priority_queue_tree)
        result.append((max_latency, router))

    return min(result)
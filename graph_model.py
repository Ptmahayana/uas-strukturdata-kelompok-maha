import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_node(self, node):
        if node not in self.adjacency_list:
            self.adjacency_list[node] = []

    def add_edge(self, from_node, to_node, weight):
        self.add_node(from_node)
        self.add_node(to_node)
        self.adjacency_list[from_node].append((to_node, weight))
        # Undirected graph (bisa diarahkan jika perlu)
        self.adjacency_list[to_node].append((from_node, weight))

    def dijkstra(self, start, end):
        pq = [(0, start, [start])]
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start] = 0

        while pq:
            current_dist, current_node, path = heapq.heappop(pq)
            if current_node == end:
                return current_dist, path

            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency_list[current_node]:
                distance = current_dist + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor, path + [neighbor]))

        return float('inf'), []
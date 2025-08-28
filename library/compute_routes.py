#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
from heapq import heapify, heappop, heappush


class Graph():
    def __init__(self, graph: dict = {}):
        self.graph = graph

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:
            self.graph[node1] = {}
        self.graph[node1][node2] = weight

    def get_neighbors(self, node):
        return self.graph.get(node, {})

    def shortest_distances(self, source: str):
        # Initialize the values of all nodes with infinity
        distances = {node: float("inf") for node in self.graph}
        distances[source] = 0

        # Initialize a priority queue
        pq = [(0, source)]
        heapify(pq)

        # Create a set to hold visited nodes
        visited = set()

        # While the priority queue isn't empty
        while pq:
            # Get the node with the min distance
            current_distance, current_node = heappop(pq)

            # Skip already visited nodes
            if current_node in visited:
                continue
            visited.add(current_node)

            # Calculate the distance from current_node to the neighbor
            for neighbor, weight in self.graph[current_node].items():
                tentative_distance = current_distance + weight
                if tentative_distance < distances[neighbor]:
                    distances[neighbor] = tentative_distance
                    heappush(pq, (tentative_distance, neighbor))

        predecessors = {node: None for node in self.graph}
        for node, distance in distances.items():
            for neighbor, weight in self.graph[node].items():
                if distances[neighbor] == distance + weight:
                    predecessors[neighbor] = node

        return distances, predecessors

    def shortest_paths(self, source: str):
        # Generate the predecessors dict
        _, predecessors = self.shortest_distances(source)

        paths = {}
        for target in self.graph.keys():
            if target == source:
                continue

            paths[target] = []
            current_node = target

            # Backtrack from the target node using predecessors
            while current_node:
                paths[target].append(current_node)
                current_node = predecessors[current_node]

            # Reverse the path and return it
            paths[target].reverse()

        return paths


def main():
    module = AnsibleModule(argument_spec={
        "host": {"type": "str", "required": True},
        "graph": {"type": "dict", "required": True},
    })

    host = module.params["host"]
    graph = module.params["graph"]

    # Create graph object
    g = Graph()
    for source in graph:
        for target in graph[source]["targets"]:
            g.add_edge(source, target, 1)

    # Compute shortest paths from the host
    paths = g.shortest_paths(host)

    # Extract next hops for each target
    result = {}
    for target in g.get_neighbors(host).keys():
        result[target] = []
        for path in paths.values():
            if path[1] == target:
                result[target].extend(graph[path[-1]]["locals"])

    module.exit_json(changed=False, result=result)


if __name__ == "__main__":
    main()

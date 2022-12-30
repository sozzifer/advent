from typing import Dict, Set, List
from collections import defaultdict
from itertools import permutations

# ChrisPenner Advent-Of-Code-Polyglot
# Store distances
distances = {}

# Get all possible places
places = set()

with open('2015/day9.txt') as f:
    for line in f:
        parts = line.split(' ')
        # Unpack values
        frm, _, to, _, amount = parts
        amount = int(amount.strip())
        # Store distance between each set of places
        distances[frm, to] = distances[to, frm] = amount
        # Add to our set of valid places
        places.add(frm)
        places.add(to)

# Get every possible route
possibilities = permutations(places)
# Store route distances as we compute them
totals = []

# Calculate total distance for every route
for route in possibilities:
    total = 0
    for i, frm in enumerate(route):
        if i == len(route) - 1:
            break
        # Get the next element
        to = route[i+1]
        total += distances[(frm, to)]
    totals.append(total)

part1 = min(totals)
part2 = max(totals)


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph: Dict[int, Set] = defaultdict(set)
        self.visited = defaultdict(lambda: False)

        self.make_graph(edges)

        self.visited_nodes = 0
        self.total_nodes = len(self.graph.keys())

    def make_graph(self, _edges) -> None:
        self.edges.extend(_edges)

        for u, v in self.edges:
            self.graph[u].add(v)
            self.graph[v].add(u)

    def visit(self, node):
        self.visited[node] = True
        self.visited_nodes += 1

    def un_visit(self, node):
        self.visited[node] = False
        self.visited_nodes -= 1

    def all_nodes_are_visited(self) -> bool:
        return self.visited_nodes == self.total_nodes

    def get_hamiltonian_path(self, start) -> List[List[int]]:
        self.visit(start)

        all_paths = []

        if self.all_nodes_are_visited():
            all_paths.append([start])

        for node in self.graph[start]:
            if self.visited[node]:
                continue
            paths = self.get_hamiltonian_path(node)
            for path in paths:
                if path:
                    path.append(start)
                    all_paths.append(path)

        self.un_visit(start)
        return all_paths


# if __name__ == '__main__':
#     with open("2015/day9.txt") as f:
#         data = f.read().split("\n")
#     edges = []
#     for line in data:
#         line = line.split(" ")
#         edges.append((line[0], line[2], int(line[4])))

#     graph = Graph(edges)
#     hamiltonian_path = graph.get_hamiltonian_path(start="Tristram")

#     for path in hamiltonian_path:
#         print("->".join(map(str, reversed(path))))


# class Graph():
#     def __init__(self):
#         """
#         self.edges is a dict of all possible next nodes
#         e.g. {'X': ['A', 'B', 'C', 'E'], ...}
#         self.weights has all the weights between two nodes,xwith the two nodes as a tuple as the key
#         e.g. {('X', 'A'): 7, ('X', 'B'): 2, ...}
#         """
#         self.edges = defaultdict(list)
#         self.weights = {}

#     def add_edge(self, from_node, to_node, weight):
#         # Note: assumes edges are bi-directional
#         self.edges[from_node].append(to_node)
#         self.edges[to_node].append(from_node)
#         self.weights[(from_node, to_node)] = weight
#         self.weights[(to_node, from_node)] = weight


# graph = Graph()

# for edge in edges:
#     graph.add_edge(*edge)

# def dijsktra(graph, initial, end):
#     # shortest paths is a dict of nodes whose value is a tuple of (previous node, weight)
#     shortest_paths = {initial: (None, 0)}
#     current_node = initial
#     visited = set()

#     while current_node != end:
#         visited.add(current_node)
#         destinations = graph.edges[current_node]
#         weight_to_current_node = shortest_paths[current_node][1]

#         for next_node in destinations:
#             weight = graph.weights[(current_node, next_node)] + weight_to_current_node
#             if next_node not in shortest_paths:
#                 shortest_paths[next_node] = (current_node, weight)
#             else:
#                 current_shortest_weight = shortest_paths[next_node][1]
#                 if current_shortest_weight > weight:
#                     shortest_paths[next_node] = (current_node, weight)

#         next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
#         if not next_destinations:
#             return "Route Not Possible"
#         # next node is the destination with the lowest weight
#         current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

#     # Work back through destinations in shortest path
#     path = []
#     while current_node is not None:
#         path.append(current_node)
#         next_node = shortest_paths[current_node][0]
#         current_node = next_node
#     # Reverse path
#     path = path[::-1]
#     return path

# print(dijsktra(graph, "Straylight", "Faerun"))
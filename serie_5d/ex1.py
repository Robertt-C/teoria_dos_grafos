import networkx as nx
import matplotlib.pyplot as plt
from itertools import permutations

class AdjacencyList:
    def __init__(self, vertices, edges):
        self.vertices = vertices
        self.edges = edges
        self.adjacency_list = {vertice: [] for vertice in vertices}
        for u, v in edges:
            self.adjacency_list[u].append(v)
            self.adjacency_list[v].append(u)
    
    def display_adjacency_list(self):
        self.render_graph()
        print("Lista de adjacência:")
        for v, neighbors in self.adjacency_list.items():
            print(f"Vértice {v}: {neighbors}")
    
    def render_graph(self):
        graph = nx.Graph()
        graph.add_nodes_from(self.vertices)
        graph.add_edges_from(self.edges)
        pos = nx.circular_layout(graph)
        nx.draw(graph, with_labels=True, pos=pos)
        plt.show()

def is_connected(grafo):
    visitados = set()

    def dfs(v):
        visitados.add(v)
        for vizinho in grafo.adjacency_list[v]:
            if vizinho not in visitados:
                dfs(vizinho)

    inicio = None
    for v in grafo.vertices:
        if grafo.adjacency_list[v]:  
            inicio = v
            break

    if inicio is None:
        return True  

    dfs(inicio)


    for v in grafo.vertices:
        if grafo.adjacency_list[v] and v not in visitados:
            return False

    return True


def is_eulerian(grafo):
    if not is_connected(grafo):
        return False  # Se não é conexo → não pode ser Euleriano
    for v in grafo.vertices:
        if len(grafo.adjacency_list[v]) % 2 != 0:
            return False
    return True


def has_hamiltonian_cycle(grafo):
    if not is_connected(grafo):
        return False  # Se não for conexo → nem tenta as permutações

    verts = grafo.vertices
    for perm in permutations(verts):
        ciclo = True
        for i in range(len(perm)):
            u = perm[i]
            v = perm[(i + 1) % len(perm)]
            if v not in grafo.adjacency_list[u]:
                ciclo = False
                break
        if ciclo:
            return True
    return False

def graph_intersection(g1, g2):
    vertices_intersect = set(g1.vertices) & set(g2.vertices)
    edges_intersect = [edge for edge in g1.edges if edge in g2.edges or (edge[1], edge[0]) in g2.edges]
    return AdjacencyList(list(vertices_intersect), edges_intersect)

def main():
    print("Criando grafos de exemplo:")
    
    G1_vertices = [1, 2, 3, 4, 5, 6]
    G1_edges = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 1), (2, 5)]

    G2_vertices = [3, 4, 5, 6, 7]
    G2_edges = [(3, 4), (4, 5), (5, 6), (6, 7)]

    G1 = AdjacencyList(G1_vertices, G1_edges)
    G2 = AdjacencyList(G2_vertices, G2_edges)

    print("\nGrafo G1:")
    G1.display_adjacency_list()

    print("\nGrafo G2:")
    G2.display_adjacency_list()
    
    print("\nA) G1 é um grafo de Euler?", "Sim" if is_eulerian(G1) else "Não")
    print("É conexo?", "Sim" if is_connected(G1) else "Não")
    
    print("\nB) Interseção entre G1 e G2:")
    inter = graph_intersection(G1, G2)
    inter.display_adjacency_list()
    print("Interseção é Euleriano?", "Sim" if is_eulerian(inter) else "Não")
    print("Interseção é conexo?", "Sim" if is_connected(inter) else "Não")
    
    print("\nC) G1 possui circuito Hamiltoniano?", "Sim" if has_hamiltonian_cycle(G1) else "Não")
    print("É conexo?", "Sim" if is_connected(G1) else "Não")

if __name__ == "__main__":
    main()

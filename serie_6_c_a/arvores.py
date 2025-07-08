import sys
from collections import deque

sys.path.insert(0, "../serie_3/codigos")

from estruturas_dados import Grafo


def e_arvore(grafo: Grafo) -> bool:
    if grafo.numero_arestas() != grafo.numero_nos() - 1:
        return False

    if not grafo.nos:
        return False

    nos = list(grafo.nos)
    inicio = nos[0]
    visitados = set()
    fila = deque([inicio])

    if not grafo.lista_adjacencia:
        grafo.cria_lista_adjacencia()

    while fila:
        atual = fila.popleft()
        if atual not in visitados:
            visitados.add(atual)
            for vizinho in grafo.lista_adjacencia[atual]:
                if vizinho not in visitados:
                    fila.append(vizinho)

    # Se visitou todos os nós, é conexo
    return len(visitados) == grafo.numero_nos()

def e_subgrafo_arvore(G: Grafo, A1: Grafo) -> bool:
    if not e_arvore(A1):
        return False

    return G.e_subgrafo(A1.nos, A1.arestas)

def e_arvore_abrangencia(G: Grafo, A1: Grafo) -> bool:
    if not e_subgrafo_arvore(G, A1):
        return False
    return A1.nos == G.nos

def encontrar_centros(A: Grafo) -> list[str]:
    if not e_arvore(A):
        return []

    if A.numero_nos() <= 2:
        return A.nos

    if not A.lista_adjacencia:
        A.cria_lista_adjacencia()

    graus = {}
    folhas = []

    for no, vizinhos in A.lista_adjacencia.items():
        grau = len(vizinhos)
        graus[no] = grau

        if grau == 1:
            folhas.append(no)

    vertices_restantes = A.numero_nos()
    while vertices_restantes > 2:
        novas_folhas = []
        for folha in folhas:
            vertices_restantes -= 1
            for vizinho in A.lista_adjacencia[folha]:
                graus[vizinho] -= 1
                if graus[vizinho] == 1:
                    novas_folhas.append(vizinho)
        folhas = novas_folhas

    return folhas

def excentricidades(A: Grafo):
    excentricidades = {}

    if not e_arvore(A):
        return excentricidades

    if not A.lista_adjacencia:
        A.cria_lista_adjacencia()

    lista_adjacencia = A.lista_adjacencia

    for vertice_inicial in lista_adjacencia:
        distancias = {v: -1 for v in lista_adjacencia}
        fila = deque([(vertice_inicial, 0)])
        distancias[vertice_inicial] = 0
        max_distancia = 0

        while fila:
            vertice_atual, dist_atual = fila.popleft()
            max_distancia = max(max_distancia, dist_atual)

            for vizinho in lista_adjacencia[vertice_atual]:
                if distancias[vizinho] == -1:
                    distancias[vizinho] = dist_atual + 1
                    fila.append((vizinho, dist_atual + 1))

        excentricidades[vertice_inicial] = max_distancia

    return excentricidades


if __name__ == "__main__":
    # Exemplo de uso
    g = Grafo()
    g.adiciona_no("A")
    g.adiciona_no("B")
    g.adiciona_no("C")
    g.adiciona_no("D")
    g.adiciona_aresta(("A", "B"))
    g.adiciona_aresta(("B", "C"))
    g.adiciona_aresta(("C", "D"))

    a1 = Grafo()
    a1.adiciona_no("A")
    a1.adiciona_no("B")
    a1.adiciona_no("C")
    a1.adiciona_aresta(("A", "B"))
    a1.adiciona_aresta(("B", "C"))

    print(e_arvore(g))  # Deve retornar True
    print(e_subgrafo_arvore(g, a1))  # Deve retornar True
    print(e_arvore_abrangencia(g, a1))  # Deve retornar False
    print(f"Centro(s): {encontrar_centros(g)}")
    print(f"Excentricidades: {excentricidades(g)}")
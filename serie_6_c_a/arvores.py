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